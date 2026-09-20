# Python Data Processing Pipeline

## Project Overview

A Python-based data processing pipeline that reads raw data, cleans and transforms it, handles missing and invalid values, validates the results, and generates structured output.

## Features

- CSV data processing
- JSON data processing
- API support
- Missing value handling
- Data type conversion
- Invalid data handling
- Duplicate removal
- Data transformation
- Output validation
- Logging
- Configuration management

## Technologies

- Python
- Pandas
- Requests
- JSON
- Git & GitHub
## Project Workflow

Raw Data → Load → Clean → Transform → Validate → Structured Output


##  Project Structure

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
│   ├── loader.py
│   ├── cleaner.py
│   ├── transformer.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
Run the Project
Bash

pip install -r requirements.txt
python src/main.py
 Output
Processed data is generated at:

data/output.csv

Execution logs are stored at:

logs/pipeline.log

 Task Objective
This project fulfills Task 2 – Data Processing Pipeline by implementing data ingestion, cleaning, transformation, edge-case handling, logging, configuration management, and structured output generation.

 Author
Murali Krishna
B.Tech Computer Science Engineering


