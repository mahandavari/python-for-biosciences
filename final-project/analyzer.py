"""Student starter: synthetic DNA homework. Complete one TODO at a time."""
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parent / "data" / "sequences.fasta"
OUTPUT_FOLDER = Path.cwd() / "outputs" / "final-project"
MOTIF = "ATA"


def normalize_dna(text):
    """TODO: uppercase/trim ends; raise ValueError for empty or non-ACGT text."""
    return None


def count_bases(sequence):
    """TODO: return a dictionary with A, T, G, C counts using a loop."""
    return None


def motif_positions(sequence, motif):
    """TODO: return a list of overlapping zero-based starts after validation."""
    return None


def read_records(path):
    """TODO: use SeqIO; reject empty data/IDs and duplicate IDs; keep order."""
    return None


def analyze_records(records, motif):
    """TODO: reuse your functions and return result dictionaries for all records."""
    return None


def save_report(rows, path):
    """TODO: write the exact CSV header, two-decimal GC and semicolon starts."""
    return None


def save_plots(rows, folder):
    """TODO: create and save both labeled plots from numeric result values."""
    return None


def main():
    # TODO: validate motif, read/analyze ALL records, then write/print results.
    # Catch ValueError and OSError with a useful message; do not skip bad records.
    print("Starter only: complete the TODOs using 01_PROJECT_SPEC.md.")


if __name__ == "__main__":
    main()
