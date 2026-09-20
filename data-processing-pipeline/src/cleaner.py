"""Data cleaning and validation functions."""

import logging
import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [
        str(column).strip().lower().replace(" ", "_")
        for column in df.columns
    ]
    logging.info("Column names standardized.")
    return df


def validate_required_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def clean_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    df = standardize_columns(df)
    validate_required_columns(df, config["required_columns"])

    before = len(df)

    # Remove completely empty rows.
    df = df.dropna(how="all")

    # Convert numeric fields. Invalid values become NaN.
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # Edge-case handling: negative age/salary values are invalid.
    df.loc[df["age"] < 0, "age"] = pd.NA
    df.loc[df["salary"] < 0, "salary"] = pd.NA

    missing_values = config["missing_values"]
    for column, value in missing_values.items():
        if column in df.columns:
            df[column] = df[column].fillna(value)

    # Make age an integer after cleaning.
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0).astype(int)
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce").fillna(0).round(2)

    # Clean text fields.
    df["name"] = df["name"].astype(str).str.strip()
    df["department"] = (
        df["department"].astype(str).str.strip().replace("", "Unknown")
    )

    # Remove duplicate records.
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    logging.info("Rows before cleaning: %d", before)
    logging.info("Duplicate rows removed: %d", duplicate_count)
    logging.info("Rows after cleaning: %d", len(df))

    return df
