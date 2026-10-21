# Intentionally wrong synthetic-DNA program. Copy before repairing.
def count_a(sequence):
    a_count = 0
    for position in range(len(sequence) - 1):
        if sequence[position] == "A":
            a_count = a_count + 1
    return a_count

sequence = "ATGA"
observed = count_a(sequence)
print("Observed A:", observed)
print("Expected A: 2")
