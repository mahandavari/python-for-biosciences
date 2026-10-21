# Run from any writable folder; creates only outputs/practice.txt and practice.csv.
from pathlib import Path
import csv

output_folder = Path.cwd() / "outputs"
output_folder.mkdir(exist_ok=True)
with open(output_folder / "practice.txt", "w", encoding="utf-8") as handle:
    handle.write("Synthetic DNA: ATGC\n")
with open(output_folder / "practice.txt", encoding="utf-8") as handle:
    print(handle.read().strip())
with open(output_folder / "practice.csv", "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["id", "length"])
    writer.writerow(["Toy", 4])
with open(output_folder / "practice.csv", newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        print(row["id"], int(row["length"]))
