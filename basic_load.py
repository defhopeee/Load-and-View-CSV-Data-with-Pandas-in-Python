# basic_load.py
import pandas as pd

# Load dataset
df = pd.read_csv('sample_data.csv')

# Show first 5 rows
print(df.head())

# Summary info
print(df.info())
