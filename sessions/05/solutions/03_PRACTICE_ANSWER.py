# Synthetic educational examples, not measured records.
sequences = ["AT", "GC"]
sequences.append("ATAT")
sequences.remove("GC")
print(sequences)
pair = (10.0, 12.0)
print(pair[0])
print(pair[1])
dna_by_id = {"One": "AT", "Two": "GC"}
print(dna_by_id["Two"])
for sequence_id in dna_by_id:
    print(sequence_id, dna_by_id[sequence_id])
symbols = set("AATG")
print(len(symbols))
print("C" in symbols)
record = {"One": {"length": 2, "gc_percent": 0.0}}
print(record["One"]["length"])
