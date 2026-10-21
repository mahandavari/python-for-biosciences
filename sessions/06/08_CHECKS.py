import dna_tools

assert dna_tools.validate_dna("ATGC") is True
assert dna_tools.validate_dna("  aTgc  ") is True
assert dna_tools.validate_dna("ATN") is False
assert dna_tools.validate_dna("") is False
assert dna_tools.validate_dna("AT GC") is False
assert dna_tools.count_nucleotides("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}
assert dna_tools.count_nucleotides("") is None
assert dna_tools.calculate_gc_content("ATGC") == 50.0
assert dna_tools.calculate_gc_content("AT") == 0.0
assert dna_tools.calculate_gc_content("gc") == 100.0
assert dna_tools.calculate_gc_content("N") is None
assert dna_tools.calculate_gc_content("") is None
assert dna_tools.find_motif_positions("ATATAT", "ATA") == [0, 2]
assert dna_tools.find_motif_positions("AAAAA", "AAA") == [0, 1, 2]
assert dna_tools.find_motif_positions("ATGC", "TT") == []
assert dna_tools.find_motif_positions("AT", "ATG") == []
assert dna_tools.find_motif_positions("AT", "") is None
assert dna_tools.find_motif_positions("AT", "N") is None
print("18 DNA checks passed.")
