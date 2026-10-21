# Reused unchanged from Session 06 for local imports. Explain normalization before use.
"""Small synthetic-DNA helpers. Inputs must be strings; only A/T/G/C accepted."""

def validate_dna(sequence):
    """Accept nonempty DNA after trimming ends and converting to upper case."""
    sequence = sequence.strip().upper()
    if sequence == "":
        return False
    for base in sequence:
        if base not in "ATGC":
            return False
    return True

def count_nucleotides(sequence):
    """Return counts, or None for invalid/empty DNA."""
    sequence = sequence.strip().upper()
    if not validate_dna(sequence):
        return None
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in sequence:
        counts[base] = counts[base] + 1
    return counts

def calculate_gc_content(sequence):
    """Return GC percent, or None for invalid/empty DNA."""
    sequence = sequence.strip().upper()
    counts = count_nucleotides(sequence)
    if counts is None:
        return None
    return (counts["G"] + counts["C"]) / len(sequence) * 100

def find_motif_positions(sequence, motif):
    """Return zero-based overlapping starts; None if either input is invalid."""
    sequence = sequence.strip().upper()
    motif = motif.strip().upper()
    if not validate_dna(sequence) or not validate_dna(motif):
        return None
    positions = []
    # Move by one so overlapping matches remain visible.
    for position in range(len(sequence) - len(motif) + 1):
        if sequence[position:position + len(motif)] == motif:
            positions.append(position)
    return positions
