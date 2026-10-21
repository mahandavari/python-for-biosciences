# Session 10 ordinary lesson answers

Attempt exercises first. [Reference notebook](06_SOLUTIONS.ipynb) runs the short ordinary tasks and one-column extension. It is not the final-project solution.

1. AAGC has length 4, first A, slice AAG, string AAGC and reverse complement GCTT. Seq represents sequence text and supports operations; it does not enforce our uppercase A/C/G/T policy. A Seq can contain other symbols.
2. Toy_A has description `Toy_A synthetic educational record`, sequence atgcAT and length 6; Toy_B has GCGC and length 4. ID is the first header token; the description includes the full header text. SeqIO joins wrapped lines and preserves lowercase. Homework IDs are Seed_A/Seed_B/Seed_C, with ATGC/AATT/GCGCGC and lengths 4/4/6.
3. ATGC and atgc pass after normalization. N, empty text and internal spaces fail. FASTA parsing is broader and may remove formatting whitespace. Duplicate Same rejects the whole batch before writing output. Never silently skip it.
4. Input is the synthetic homework FASTA. Process validates all records and calls our own counts/GC functions. Output is one CSV. Seed_A G1+C1 over 4 gives 50%; Seed_B gives 0%; Seed_C gives 100%. Headers: record_id,length_bases,gc_percent. Rows: Seed_A,4,50.0; Seed_B,4,0.0; Seed_C,6,100.0. Rejecting before opening output preserves any earlier report on a validation error.
5. Add `counts["G"]` to each stored row and `g_count` to the header in the same position. Values are 1,0,3. The notebook demonstrates this small extension. Keep counts inside the loop so each record starts fresh.
6. Missing features include complete A/T/G/C CSV columns, motif positions/counts, two saved project charts and the full test/error documentation. A kernel mismatch explains a missing Bio import. Supported statement: Seed_C has a higher GC percentage than these other invented sequences. This does not prove function, species or biological importance.

Assessment key, one point each: (1) sequence text object; no policy validation; (2) Toy_A and record.seq; (3) ATGC, yes broader alphabets; (4) no, validate all first, preserve existing output; (5) length4, A2, GC50%, no function inference; (6) any two missing features listed above and the final-project package submission instructions.
