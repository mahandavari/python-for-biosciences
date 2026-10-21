# Complete practice 2-3: read synthetic inputs, write new files, read them back.
from pathlib import Path
import csv

course_root = Path(__file__).resolve().parents[3]
data_folder = course_root / "datasets" / "session-07"
output_folder = Path.cwd() / "outputs"
output_folder.mkdir(exist_ok=True)
with open(data_folder / "sequence.txt", encoding="utf-8") as handle:
    sequence = handle.read().strip().upper()
with open(output_folder / "practice_sequence.txt", "w", encoding="utf-8") as handle:
    handle.write(sequence + "\n")
with open(output_folder / "practice_sequence.txt", encoding="utf-8") as handle:
    print("Read back:", handle.read().strip())

rows = []
with open(data_folder / "sequences.csv", newline="", encoding="utf-8") as handle:
    for record in csv.DictReader(handle):
        rows.append([record["id"], len(record["sequence"])])
output_path = output_folder / "practice_lengths.csv"
with open(output_path, "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["id", "length"])
    writer.writerows(rows)
with open(output_path, newline="", encoding="utf-8") as handle:
    for record in csv.DictReader(handle):
        print(record["id"], int(record["length"]))
