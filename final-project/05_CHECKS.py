"""Starting checks, not a full test suite. Run after completing core TODOs."""
from analyzer import normalize_dna, count_bases, motif_positions

assert normalize_dna(" atgc ") == "ATGC"
assert count_bases("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}
assert motif_positions("ATATAT", "ATA") == [0, 2]
assert motif_positions("AT", "GCG") == []
print("Four starting checks passed. Add the rest of 04_TEST_PLAN.md.")
