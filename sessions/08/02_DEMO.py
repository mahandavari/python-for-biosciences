# Synthetic expression-like values in arbitrary units; no experimental evidence.
from pathlib import Path

course_root = Path(__file__).resolve().parents[2]
data_path = course_root / "datasets" / "session-08" / "expression.csv"
filter_column = "Sample_A"
threshold = 10


import pandas as pd

table = pd.read_csv(data_path)
print(table.head())
print("Shape:", table.shape)
print(table.dtypes)
print("Missing values:")
print(table.isna().sum())
selected = table[table[filter_column] >= threshold]
print("Filtered genes:", selected["gene_id"].tolist())
sorted_table = table.sort_values(filter_column, ascending=False)
print("Sorted genes:", sorted_table["gene_id"].tolist())
values = table[filter_column]
print("Mean:", values.mean())
print("Median:", values.median())
print("Min:", values.min(), "Max:", values.max())
print("Sample SD:", values.std())
