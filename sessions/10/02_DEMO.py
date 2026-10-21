"""Seq and SeqIO on synthetic educational sequences; no external service."""
from pathlib import Path
from Bio.Seq import Seq
from Bio import SeqIO

# Seq stores sequence text; it does not check our project's simplified DNA policy.
sequence = Seq("ATGCAT")
print("Seq:", sequence)
print("Length (bases):", len(sequence))
print("First base:", sequence[0])
print("First three bases:", sequence[:3])
print("String:", str(sequence))
print("Reverse complement:", sequence.reverse_complement())

course_root = Path(__file__).resolve().parents[2]
input_path = course_root / "datasets" / "session-07" / "sequences.fasta"
try:
    with input_path.open(encoding="utf-8") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            print("ID:", record.id)
            print("Description:", record.description)
            print("Sequence:", str(record.seq))
            print("Length (bases):", len(record.seq))
except FileNotFoundError:
    print("Missing input. Extract the whole course folder, including datasets.")

# Expected IDs: Toy_A, Toy_B; text: atgcAT, GCGC. Case is preserved.
