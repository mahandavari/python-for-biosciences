# Synthetic educational DNA only; no file or external dataset is used.
sequence = input("Synthetic DNA: ").strip().upper()
motif = input("Motif: ").strip().upper()
valid_dna = True
a_count = 0
t_count = 0
g_count = 0
c_count = 0
for base in sequence:
    if base == "A":
        a_count = a_count + 1
    elif base == "T":
        t_count = t_count + 1
    elif base == "G":
        g_count = g_count + 1
    elif base == "C":
        c_count = c_count + 1
    else:
        valid_dna = False

if len(sequence) == 0:
    print("Invalid: empty DNA.")
elif not valid_dna:
    print("Invalid: DNA must contain only A, T, G, C.")
else:
    sequence_length = len(sequence)
    print("Length:", sequence_length)
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)
    gc_percent = (g_count + c_count) / sequence_length * 100
    print("GC percentage:", gc_percent)
    valid_motif = True
    for base in motif:
        if base not in "ATGC":
            valid_motif = False
    if len(motif) == 0:
        print("Invalid: empty motif.")
    elif not valid_motif:
        print("Invalid: motif must contain only A, T, G, C.")
    else:
        match_count = 0
        # Include the last legal start; moving by one preserves overlaps.
        for position in range(len(sequence) - len(motif) + 1):
            if sequence[position:position + len(motif)] == motif:
                print("Match position:", position)
                match_count = match_count + 1
        print("Match count:", match_count)
