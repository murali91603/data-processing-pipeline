# Data Processing Pipeline

## Task 2 - Data Processing Pipeline

A Python data processing pipeline that reads raw data from CSV, JSON, or an API, cleans and transforms the data, handles missing and invalid values, validates the result, and writes structured output.

## Features

- CSV input support
- JSON input support
- REST API input support
- Missing-value handling
- Data type conversion
- Invalid numeric-value handling
- Negative-value edge-case handling
- Duplicate removal
- Data transformation
- Output validation
- Logging
- JSON-based configuration management
- Sample input and output data

## Project Structure

```text
data-processing-pipeline/
├── config/
│   └── config.json
├── data/
│   ├── input.csv
│   ├── input.json
│   └── output.csv
├── logs/
│   └── pipeline.log
├── src/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── loader.py
│   ├── main.py
│   └── transformer.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- Git (for GitHub submission)

## Installation

Open a terminal in the project folder:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Pipeline

From the project root:

```bash
python src/main.py
```

The pipeline will:

1. Read `data/input.csv`.
2. Convert invalid numeric values to missing values.
3. Handle missing values.
4. Handle invalid negative age/salary values.
5. Remove duplicate records.
6. Create `salary_category`.
7. Create `age_group`.
8. Validate the final data.
9. Save the result to `data/output.csv`.
10. Write execution logs to `logs/pipeline.log`.

## Sample Input

The included CSV contains examples of:

- Missing age
- Invalid salary
- Missing department
- Duplicate records
- Negative age
- Non-numeric age

This demonstrates the pipeline's edge-case handling.

## Sample Output

After running the pipeline, `data/output.csv` contains structured records similar to:

```csv
id,name,age,age_group,salary,salary_category,department
1,Murali,21,18-25,35000.0,Low,IT
2,Ravi,0,Unknown,45000.0,Low,IT
3,Priya,22,18-25,0.0,Low,HR
4,John,25,18-25,50000.0,High,Unknown
5,Sneha,24,18-25,60000.0,High,Finance
6,Murali,21,18-25,35000.0,Low,IT
7,Arjun,0,Unknown,70000.0,High,IT
8,Divya,0,Unknown,55000.0,High,HR
```

## Configuration

Edit `config/config.json` to change:

- Input format
- Input file
- Output file
- Log file
- Required columns
- Missing-value defaults
- Salary threshold

### Using JSON input

Change:

```json
"input_format": "json",
"input_file": "data/input.json"
```

Then run:

```bash
python src/main.py
```

### Using an API

Change:

```json
"input_format": "api",
"input_file": "https://example.com/api/data"
```

The API must return JSON containing either a list of records or a single JSON object.

## Logging

The pipeline logs:

- Pipeline start/end
- Input loading
- Number of records
- Cleaning operations
- Duplicate count
- Transformation completion
- Validation result
- Output location
- Errors and exceptions

Logs are stored in:

```text
logs/pipeline.log
```

## Technologies

- Python
- Pandas
- Requests
- JSON
- REST API
- Git/GitHub

## Author

Murali
