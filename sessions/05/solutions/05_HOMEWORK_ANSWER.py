# Synthetic educational DNA, invented for collection and arithmetic practice.
# Each identifier is unique. Dictionary insertion order sets the tie rule.
sequences = {"Seed_A": "ATGC", "Seed_B": "AATT", "Seed_C": "GCGCGC", "Seed_D": "AT"}
summaries = {}
unique_symbols = set()
longest_id = ""
shortest_id = ""
longest_length = 0
shortest_length = 0

for sequence_id in sequences:
    sequence = sequences[sequence_id].strip().upper()
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    valid_dna = True
    for base in sequence:
        if base in counts:
            counts[base] = counts[base] + 1
        else:
            valid_dna = False
    if len(sequence) == 0 or not valid_dna:
        print("Skipped invalid DNA:", sequence_id)
        continue
    sequence_length = len(sequence)
    gc_percent = (counts["G"] + counts["C"]) / sequence_length * 100
    summaries[sequence_id] = {"length": sequence_length, "A": counts["A"],
                              "T": counts["T"], "G": counts["G"], "C": counts["C"],
                              "gc_percent": gc_percent}
    for base in sequence:
        unique_symbols.add(base)
    # Strict comparison keeps the first accepted identifier on a length tie.
    if longest_id == "" or sequence_length > longest_length:
        longest_id = sequence_id
        longest_length = sequence_length
    if shortest_id == "" or sequence_length < shortest_length:
        shortest_id = sequence_id
        shortest_length = sequence_length

for sequence_id in summaries:
    record = summaries[sequence_id]
    print("Sequence:", sequence_id)
    print("Length:", record["length"])
    print("A:", record["A"], "T:", record["T"], "G:", record["G"], "C:", record["C"])
    print("GC percentage:", record["gc_percent"])

if len(summaries) == 0:
    print("No valid sequences.")
else:
    print("Longest:", longest_id, longest_length)
    print("Shortest:", shortest_id, shortest_length)
    print("Unique identifiers:", len(set(summaries)))
    # Check membership in a fixed order; set display order is not guaranteed.
    for base in "ATGC":
        if base in unique_symbols:
            print("Observed symbol:", base)
