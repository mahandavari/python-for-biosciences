# Session 04 homework: one synthetic DNA report

Create `04_dna_report.py`, a terminal script asking for a DNA string and a motif. Use only conditions, loops, strings and taught built-ins. Do not use functions, lists, files or libraries. Print length in bases, A/T/G/C counts, GC percentage, each zero-based motif position and total matches. Explain the algorithm in a short text note.

Both entries: strip end whitespace and uppercase. Reject empty DNA or any DNA character outside A/T/G/C (including N and internal spaces). Do not compute GC for rejected DNA. Reject empty motif or non-A/T/G/C motif; the valid DNA summary may still print. A longer motif is accepted and gives zero matches. Include overlaps by moving one position per step. All examples are invented for teaching; motif presence proves no function.

Main test: DNA `atgcATAT`, motif `ata`. Expect normalized ATGCATAT, length 8, A=3,T=3,G=1,C=1, GC=25.0, position 4, count 1. Also test ATATAT/ATA -> 0 and 2, count 2; AT/ATG -> zero; empty DNA -> error; ATN -> error; valid DNA/empty motif -> motif error. Include a comment labeling synthetic data. Submit script and note through the teacher's chosen channel. Success: all outputs match, no division by zero, overlap and coordinate rules are stated. If blocked, include your attempt and exact error. [Reference](solutions/06_SOLUTIONS.md).
