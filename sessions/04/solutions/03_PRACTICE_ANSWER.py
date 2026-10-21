# Synthetic educational DNA string; no biological meaning is inferred.
sequence = "ATGCAT"
for base in sequence:
    print(base)
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
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
if len(sequence) > 0:
    print("GC percentage:", (g_count + c_count) / len(sequence) * 100)

# Synthetic pattern search; fixed inputs make this cell repeatable.
sequence = "ATATAT".strip().upper()
motif = "ATA".strip().upper()
if len(motif) == 0:
    print("Invalid: empty motif.")
else:
    match_count = 0
    for position in range(len(sequence) - len(motif) + 1):
        window = sequence[position:position + len(motif)]
        if window == motif:
            print("Match position:", position)
            match_count = match_count + 1
    print("Match count:", match_count)
