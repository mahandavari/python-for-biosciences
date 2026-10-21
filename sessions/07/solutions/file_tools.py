"""Limited educational FASTA reader and validated CSV writer; synthetic DNA only."""
import csv

def validate_dna(sequence):
    """Check already-normalized nonempty A/T/G/C text."""
    if sequence == "":
        return False
    for base in sequence:
        if base not in "ATGC":
            return False
    return True

def read_fasta(path):
    """Read unique first-token IDs and wrapped DNA; raise ValueError on bad data."""
    records = {}
    current_id = None
    with open(path, encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if line == "":
                continue
            if line.startswith(">"):
                # Reject an empty previous record before moving to the next.
                if current_id is not None and records[current_id] == "":
                    raise ValueError("Empty sequence: " + current_id)
                header = line[1:].strip()
                if header == "":
                    raise ValueError("Empty FASTA header")
                current_id = header.split()[0]
                if current_id in records:
                    raise ValueError("Duplicate identifier: " + current_id)
                records[current_id] = ""
            else:
                if current_id is None:
                    raise ValueError("Sequence before first header")
                sequence_line = line.upper()
                if not validate_dna(sequence_line):
                    raise ValueError("Invalid DNA symbols: " + current_id)
                records[current_id] = records[current_id] + sequence_line
    if len(records) == 0:
        raise ValueError("No FASTA records")
    if records[current_id] == "":
        raise ValueError("Empty sequence: " + current_id)
    return records

def summarize_records(records):
    """Validate all records before output; return rows with counts and GC percent."""
    if len(records) == 0:
        raise ValueError("No records to report")
    rows = []
    for sequence_id in records:
        sequence = records[sequence_id]
        if sequence_id.strip() == "" or not validate_dna(sequence):
            raise ValueError("Invalid report record: " + sequence_id)
        counts = {"A": 0, "T": 0, "G": 0, "C": 0}
        for base in sequence:
            counts[base] = counts[base] + 1
        gc_percent = (counts["G"] + counts["C"]) / len(sequence) * 100
        rows.append([sequence_id, len(sequence), counts["A"], counts["T"],
                     counts["G"], counts["C"], gc_percent])
    return rows

def save_report(records, output_path):
    """Check every record before opening the output; overwrite only the named report."""
    rows = summarize_records(records)
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "length", "A", "T", "G", "C", "gc_percent"])
        writer.writerows(rows)
