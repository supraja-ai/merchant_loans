import pandas as pd
import numpy as np

# 1. Load the dataset
# Replace 'data.csv' with your actual dataset file. Ensure the CSV is in your working directory.
import os

if os.path.exists('dataset.csv'):
    df = pd.read_csv('dataset.csv')
    print("Data Preview:")
    print(df.head())
else:
    raise FileNotFoundError("The file 'dataset.csv' was not found in the working directory.")

# 2. Inspecting Data
# Check the overall structure and look for missing values.
print("\nData Information:")
print(df.info())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 3. Data Cleaning
# For numeric columns, you might fill missing values with the mean (customize as needed).
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    if df[col].isnull().any():
        mean_value = df[col].mean()
        df[col].fillna(mean_value, inplace=True)
        print(f"Filled missing values in '{col}' with mean: {mean_value:.2f}")

# Optionally, for categorical columns you might fill with the mode:
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    if df[col].isnull().any():
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)
        print(f"Filled missing values in '{col}' with mode: {mode_value}")

# 4. Data Exploration and Feature Engineering
# Generate summary statistics using Pandas.
print("\nSummary Statistics:")
print(df.describe())

# Create a new column as an example (e.g., a ratio of two features if applicable).
if 'column_A' in df.columns and 'column_B' in df.columns:
    df['ratio'] = df['column_A'] / df['column_B']
    print("\nNew column 'ratio' added. Preview:")
    print(df[['column_A', 'column_B', 'ratio']].head())

# 5. Grouping and Aggregation
# Suppose you have a column 'category' that you want to analyze.
if 'category' in df.columns and 'value' in df.columns:
    grouped = df.groupby('category').agg({
        'value': [np.mean, np.std, np.min, np.max]
    })
    print("\nGrouped statistics by 'category':")
    print(grouped)

# 6. Utilizing NumPy for Additional Analysis
# Example: Calculate the average of a feature directly using NumPy.
if 'feature' in df.columns:
    feature_array = np.array(df['feature'])
    avg_feature = np.mean(feature_array)
    std_feature = np.std(feature_array)
    print(f"\nUsing NumPy: Average of 'feature' is {avg_feature:.2f} with a standard deviation of {std_feature:.2f}")

# 7. Sorting and Indexing
# Sort the data based on a particular feature to identify trends.
if 'feature' in df.columns:
    df_sorted = df.sort_values(by='feature', ascending=False)
    print("\nData sorted by 'feature' (descending):")
    print(df_sorted.head())
