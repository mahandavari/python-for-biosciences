# Original charts of synthetic educational data; no experimental evidence.
from pathlib import Path

import pandas as pd
import matplotlib

# Agg saves images without opening a window; notebooks use inline display.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

course_root = Path(__file__).resolve().parents[2]
data_folder = course_root / "datasets" / "session-09"
output_folder = course_root / "outputs" / "session-09" / "demo"
output_folder.mkdir(parents=True, exist_ok=True)

genes = pd.read_csv(data_folder / "measurements.csv")
sequences = pd.read_csv(data_folder / "sequence_summary.csv")
time_series = pd.read_csv(data_folder / "time_series.csv")
print("Missing time-series values:")
print(time_series.isna().sum())

# Bar heights compare named categories, with a zero baseline.
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(genes["gene_id"], genes["measurement_au"], color="navy")
ax.set_xlabel("Fictional gene identifier")
ax.set_ylabel("Measurement (AU)")
ax.set_title("Synthetic gene measurements")
ax.set_ylim(bottom=0)
fig.savefig(output_folder / "gene_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Histogram heights count records inside numeric intervals.
fig, ax = plt.subplots(figsize=(7, 4))
counts, edges, patches = ax.hist(
    sequences["length_bases"], bins=[0, 5, 10, 15, 20],
    color="teal", edgecolor="black"
)
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("Number of sequences")
ax.set_title("Synthetic sequence length distribution")
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_yticks([0, 1, 2, 3])
print("Histogram counts:", counts.tolist())
fig.savefig(output_folder / "length_histogram.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Keeping the missing row leaves an honest gap at hour 4.
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(time_series["time_h"], time_series["cell_count"],
        marker="o", color="navy", label="Observed synthetic counts")
ax.set_xlabel("Time (h)")
ax.set_ylabel("Cell count (cells)")
ax.set_title("Synthetic cell counts; hour 4 is missing")
ax.set_xticks([0, 2, 4, 6, 8])
ax.set_ylim(bottom=0)
ax.legend()
fig.savefig(output_folder / "time_line.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# Both columns keep the same row order to preserve pairs.
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(sequences["length_bases"], sequences["gc_percent"], color="teal")
ax.set_xlabel("Sequence length (bases)")
ax.set_ylabel("GC content (%)")
ax.set_title("Synthetic sequence length and GC content")
ax.set_ylim(-5, 105)
ax.set_yticks([0, 25, 50, 75, 100])
fig.savefig(output_folder / "length_gc_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Saved four PNG charts to:", output_folder)
print("Synthetic values describe only these invented records; no causality.")
