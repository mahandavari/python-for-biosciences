# New synthetic sequence summaries; no experimental evidence.
from pathlib import Path

import pandas as pd
import matplotlib

# Agg saves images without opening a window; notebooks use inline display.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

course_root = Path(__file__).resolve().parents[3]
data_path = course_root / "datasets" / "session-09" / "homework.csv"
output_folder = course_root / "outputs" / "session-09" / "homework-answer"
output_folder.mkdir(parents=True, exist_ok=True)
table = pd.read_csv(data_path)
print("Shape:", table.shape)
print(table.dtypes)
print("Missing values:")
print(table.isna().sum())

# A bar answers which fictional ID has each GC percentage.
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(table["sequence_id"], table["gc_percent"], color="navy")
ax.set_xlabel("Fictional sequence identifier")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic homework GC content by sequence")
ax.set_ylim(0, 100)
fig.savefig(output_folder / "homework_gc_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# A histogram groups numeric lengths, rather than comparing ID labels.
fig, ax = plt.subplots(figsize=(7, 4))
counts, edges, patches = ax.hist(
    table["length_bases"], bins=[0, 5, 10, 15, 20, 25],
    color="teal", edgecolor="black"
)
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("Number of sequences")
ax.set_title("Synthetic homework sequence lengths")
ax.set_xticks([0, 5, 10, 15, 20, 25])
ax.set_yticks([0, 1, 2])
print("Histogram counts:", counts.tolist())
fig.savefig(output_folder / "homework_length_histogram.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# A scatter answers how the two numeric values are paired in each row.
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(table["length_bases"], table["gc_percent"], color="teal")
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic homework length and GC content")
ax.set_ylim(-5, 105)
ax.set_yticks([0, 25, 50, 75, 100])
fig.savefig(output_folder / "homework_length_gc_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved three PNG charts to:", output_folder)
print("HW_D is longer than HW_C but has lower GC (50% versus 60%).")
print("The pattern is descriptive only; no causality or gene function follows.")
