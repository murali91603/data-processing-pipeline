"""Main entry point for the data processing pipeline."""

import json
import logging
from pathlib import Path

from cleaner import clean_data
from loader import load_data
from transformer import transform_data, validate_output


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config" / "config.json"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def setup_logging(log_file: str) -> None:
    log_path = PROJECT_ROOT / log_file
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True,
    )


def resolve_source(config: dict) -> str:
    source = config["input_file"]
    if config["input_format"].lower() in {"csv", "json"}:
        return str(PROJECT_ROOT / source)
    return source


def main() -> None:
    config = load_config()
    setup_logging(config["log_file"])

    logging.info("========== PIPELINE STARTED ==========")

    try:
        source = resolve_source(config)

        df = load_data(config["input_format"], source)
        logging.info("Loaded %d records.", len(df))

        cleaned_df = clean_data(df, config)

        transformed_df = transform_data(
            cleaned_df,
            float(config["salary_threshold"])
        )

        validate_output(transformed_df)

        output_path = PROJECT_ROOT / config["output_file"]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        transformed_df.to_csv(output_path, index=False)

        logging.info("Output saved to: %s", output_path)
        logging.info("========== PIPELINE COMPLETED ==========")

    except Exception:
        logging.exception("Pipeline failed.")
        raise


if __name__ == "__main__":
    main()
