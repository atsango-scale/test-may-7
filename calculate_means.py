import pandas as pd
import sys

def calculate_column_means(csv_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Calculate means for each column
        means = df.mean(numeric_only=True)
        
        print("\nMean values for each column:")
        print("-" * 30)
        for column, mean in means.items():
            print(f"{column}: {mean:.2f}")
            
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate_means.py <csv_file>")
        sys.exit(1)
        
    csv_file = sys.argv[1]
    calculate_column_means(csv_file) 