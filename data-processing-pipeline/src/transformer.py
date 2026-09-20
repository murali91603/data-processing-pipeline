"""Data transformation functions."""

import logging
import pandas as pd


def transform_data(df: pd.DataFrame, salary_threshold: float) -> pd.DataFrame:
    df = df.copy()

    df["salary_category"] = df["salary"].apply(
        lambda salary: "High" if salary >= salary_threshold else "Low"
    )

    def age_group(age: int) -> str:
        if age <= 0:
            return "Unknown"
        if age < 18:
            return "Under 18"
        if age <= 25:
            return "18-25"
        if age <= 35:
            return "26-35"
        if age <= 50:
            return "36-50"
        return "51+"

    df["age_group"] = df["age"].apply(age_group)

    # Keep the output consistently ordered.
    output_columns = [
        "id", "name", "age", "age_group", "salary",
        "salary_category", "department"
    ]
    df = df[output_columns]

    logging.info("Data transformation completed.")
    return df


def validate_output(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Pipeline produced an empty output.")

    if df["salary"].isna().any():
        raise ValueError("Output contains missing salary values.")

    if df["age"].isna().any():
        raise ValueError("Output contains missing age values.")

    logging.info("Output validation passed.")
