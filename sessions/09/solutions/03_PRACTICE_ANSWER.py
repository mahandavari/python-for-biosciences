# Synthetic educational data only. These answers follow an independent attempt.
from pathlib import Path

import pandas as pd
import matplotlib

# Agg saves images without opening a window; notebooks use inline display.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

course_root = Path(__file__).resolve().parents[3]
data_folder = course_root / "datasets" / "session-09"
output_folder = course_root / "outputs" / "session-09" / "practice"
output_folder.mkdir(parents=True, exist_ok=True)
genes = pd.read_csv(data_folder / "measurements.csv")
sequences = pd.read_csv(data_folder / "sequence_summary.csv")
time_series = pd.read_csv(data_folder / "time_series.csv")

# Task 2: IDs determine the categories; values determine the heights.
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(genes["gene_id"], genes["measurement_au"], color="navy")
ax.set_xlabel("Fictional gene identifier")
ax.set_ylabel("Measurement (AU)")
ax.set_title("Synthetic gene measurements")
ax.set_ylim(bottom=0)
fig.savefig(output_folder / "practice_genes.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Task 3: wider bins give counts 3 and 5, still totaling 8 records.
fig, ax = plt.subplots(figsize=(7, 4))
counts, edges, patches = ax.hist(sequences["length_bases"], bins=[0, 10, 20],
                                color="teal", edgecolor="black")
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("Number of sequences")
ax.set_title("Synthetic lengths in wider bins")
ax.set_xticks([0, 10, 20])
ax.set_yticks([0, 1, 2, 3, 4, 5])
print("Task 3 histogram counts:", counts.tolist())
fig.savefig(output_folder / "practice_histogram.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Task 4: the full column includes NaN; do not fill or drop that point.
print("Task 4 missing values:", time_series.isna().sum().to_dict())
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(time_series["time_h"], time_series["cell_count"], marker="o", color="navy",
        label="Observed synthetic counts")
ax.set_xlabel("Time (h)")
ax.set_ylabel("Cell count (cells)")
ax.set_title("Synthetic cell counts; hour 4 is missing")
ax.set_xticks([0, 2, 4, 6, 8])
ax.set_ylim(bottom=0)
ax.legend()
fig.savefig(output_folder / "practice_time.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Task 5: keep matching rows in x and y.
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(sequences["length_bases"], sequences["gc_percent"], color="teal")
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic paired sequence measurements")
ax.set_ylim(-5, 105)
ax.set_yticks([0, 25, 50, 75, 100])
fig.savefig(output_folder / "practice_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Task 6: inspect the input before building two new charts.
print("Practical table:", sequences.shape)
print(sequences.dtypes)
print(sequences.isna().sum())
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(sequences["sequence_id"], sequences["gc_percent"], color="navy")
ax.set_xlabel("Fictional sequence identifier")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic GC content by sequence")
ax.set_ylim(0, 100)
fig.savefig(output_folder / "practical_gc.png", dpi=150, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(sequences["length_bases"], sequences["gc_percent"], color="teal")
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic sequence length and GC content")
ax.set_ylim(-5, 105)
ax.set_yticks([0, 25, 50, 75, 100])
fig.savefig(output_folder / "practical_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved six PNG charts to:", output_folder)
print("S08 has length18 and GC100%; this alone gives no biological function.")
