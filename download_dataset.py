from datasets import load_dataset
import pandas as pd

# Load the IMDb dataset
dataset = load_dataset("imdb")

# Convert both 'train' and 'test' parts of the dataset to pandas DataFrames
train_df = pd.DataFrame(dataset['train'])
test_df = pd.DataFrame(dataset['test'])

# Define file paths for the CSV files
train_csv_file_path = "imdb_train_dataset.csv"
test_csv_file_path = "imdb_test_dataset.csv"

# Saving the DataFrames to CSV files
train_df.to_csv(train_csv_file_path, index=False)
test_df.to_csv(test_csv_file_path, index=False)

# Output the paths to confirm the files were created
print(f"Train dataset CSV file saved to: {train_csv_file_path}")
print(f"Test dataset CSV file saved to: {test_csv_file_path}")