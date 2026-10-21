# Synthetic educational DNA. Run this file, keeping dna_tools.py beside it.
import dna_tools
import statistics

sequence = "ATGCATAT"
print("Valid:", dna_tools.validate_dna(sequence))
print("Counts:", dna_tools.count_nucleotides(sequence))
print("GC percentage:", dna_tools.calculate_gc_content(sequence))
print("Motif starts:", dna_tools.find_motif_positions(sequence, "ATA"))
print("Mean length:", statistics.mean([4, 6, 8]))
