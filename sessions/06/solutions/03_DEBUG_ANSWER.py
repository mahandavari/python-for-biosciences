# Repaired synthetic-DNA counter: include every index.
def count_a(sequence):
    a_count = 0
    for position in range(len(sequence)):
        if sequence[position] == "A":
            a_count = a_count + 1
    return a_count

sequence = "ATGA"
observed = count_a(sequence)
print("Observed A:", observed)
print("Expected A: 2")

assert count_a("A") == 1
assert count_a("AAAA") == 4
assert count_a("TT") == 0
