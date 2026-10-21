# Synthetic expression-like values in arbitrary units; no experimental evidence.
from pathlib import Path

course_root = Path(__file__).resolve().parents[3]
data_path = course_root / "datasets" / "session-08" / "homework.csv"
filter_column = "Sample_D"
threshold = 6


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


table.info()
print(table[["gene_id", "Sample_D"]])
print(table.loc[0, "gene_id"], table.iloc[0, 1])
print("Observed E:", table["Sample_E"].count())
print("E observed mean:", table["Sample_E"].mean())
print("E no-skip mean:", table["Sample_E"].mean(skipna=False))
print("Synthetic AU only; descriptive differences are not significance tests.")
