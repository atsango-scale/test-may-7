# CSV Column Mean Calculator

A tool that calculates the mean value for each numeric column in a CSV file. Available in both Python and C++ implementations.

## Features
- Reads any CSV file
- Automatically identifies and processes numeric columns
- Ignores non-numeric columns
- Provides formatted output with means rounded to 2 decimal places
- Includes error handling for common issues

## Python Version

### Requirements
- Python 3.x
- pandas library (>= 2.0.0)

### Installation
1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage
Run the script by providing your CSV file as an argument:
```bash
python calculate_means.py your_data.csv
```

## C++ Version

### Requirements
- C++11 compatible compiler
- Make (for building)

### Building
```bash
make
```

### Usage
Run the compiled program with your CSV file:
```bash
./calculate_means your_data.csv
```

## Sample Data
A sample CSV file (`sample_data.csv`) is included for testing purposes. To test either version:

Python:
```bash
python calculate_means.py sample_data.csv
```

C++:
```bash
./calculate_means sample_data.csv
```

## Cleaning up C++ Build
To remove the compiled binary:
```bash
make clean
```