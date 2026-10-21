"""Small guided workflow, not the full final project. Synthetic data only."""
import csv
from pathlib import Path
from Bio import SeqIO
import dna_tools

course_root = Path(__file__).resolve().parents[2]
input_path = course_root / "datasets" / "session-07" / "homework.fasta"
output_path = Path.cwd() / "outputs" / "session10_initial" / "initial_summary.csv"

try:
    # Store records so every input can be checked before any report is written.
    with input_path.open(encoding="utf-8") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
    if len(records) == 0:
        raise ValueError("No FASTA records found.")
    seen_ids = set()
    rows = []
    for record in records:
        if record.id == "" or record.id in seen_ids:
            raise ValueError("Empty or duplicate record ID: " + record.id)
        seen_ids.add(record.id)
        sequence = str(record.seq).strip().upper()
        if sequence == "" or not set(sequence).issubset(set("ACGT")):
            raise ValueError("Expected nonempty uppercase A/C/G/T DNA: " + record.id)
        counts = dna_tools.count_nucleotides(sequence)
        gc_percent = dna_tools.calculate_gc_content(sequence)
        print(record.id, "counts:", counts)
        rows.append([record.id, len(sequence), round(gc_percent, 2)])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["record_id", "length_bases", "gc_percent"])
        writer.writerows(rows)
    print("Saved:", output_path)
except FileNotFoundError:
    print("Missing input. Check the downloaded datasets folder.")
except ValueError as error:
    print("Input problem:", error)
except OSError as error:
    print("Cannot read or save this file:", error)
