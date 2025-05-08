# CSV Column Mean Calculator

A simple Python script that calculates the mean value for each numeric column in a CSV file.

## Features
- Reads any CSV file
- Automatically identifies and processes numeric columns
- Ignores non-numeric columns
- Provides formatted output with means rounded to 2 decimal places
- Includes error handling for common issues

## Requirements
- Python 3.x
- pandas library (>= 2.0.0)

## Installation
1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script by providing your CSV file as an argument:
```bash
python calculate_means.py your_data.csv
```

## Sample Data
A sample CSV file (`sample_data.csv`) is included for testing purposes. To test the script with sample data:
```bash
python calculate_means.py sample_data.csv
```