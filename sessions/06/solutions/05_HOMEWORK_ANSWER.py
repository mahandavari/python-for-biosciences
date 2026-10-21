import homework_dna

for sequence in ["ATATAT", "ATGC"]:
    motif = "ATA"
    if sequence == "ATGC":
        motif = "GC"
    print(sequence, len(sequence), homework_dna.count_nucleotides(sequence))
    print(homework_dna.calculate_gc_content(sequence))
    print(homework_dna.find_motif_positions(sequence, motif))

assert homework_dna.validate_dna("AT")
assert not homework_dna.validate_dna("N")
assert not homework_dna.validate_dna("")
assert homework_dna.calculate_gc_content("gc") == 100.0
assert homework_dna.find_motif_positions("ATATAT", "ATA") == [0, 2]
print("Five homework checks passed.")
