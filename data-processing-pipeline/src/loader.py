"""Data loading functions for CSV, JSON, and API sources."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import requests


def load_csv(file_path: str) -> pd.DataFrame:
    logging.info("Loading CSV file: %s", file_path)
    return pd.read_csv(file_path)


def load_json(file_path: str) -> pd.DataFrame:
    logging.info("Loading JSON file: %s", file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = data.get("data", data)

    if not isinstance(data, list):
        raise ValueError("JSON input must contain a list of records or a 'data' list.")

    return pd.DataFrame(data)


def load_api(url: str, timeout: int = 10) -> pd.DataFrame:
    logging.info("Loading data from API: %s", url)
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    data: Any = response.json()

    if isinstance(data, dict):
        data = data.get("data", data)

    if isinstance(data, dict):
        data = [data]

    if not isinstance(data, list):
        raise ValueError("API response must be a JSON object or list of objects.")

    return pd.DataFrame(data)


def load_data(input_format: str, source: str) -> pd.DataFrame:
    input_format = input_format.lower().strip()

    if input_format == "csv":
        return load_csv(source)
    if input_format == "json":
        return load_json(source)
    if input_format == "api":
        return load_api(source)

    raise ValueError("Unsupported input format. Use: csv, json, or api.")
