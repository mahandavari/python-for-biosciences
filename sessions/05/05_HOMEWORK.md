# Session 05 homework: several synthetic DNA records

Create `05_sequence_summaries.py`. Store these invented examples in this insertion order, using unique IDs: Seed_A -> ATGC; Seed_B -> AATT; Seed_C -> GCGCGC; Seed_D -> AT. Strings represent one strand; length units are bases. No experimental data is used.

Choose suitable collections and explain each choice in a short note. Use loops and taught structures, without functions or libraries. Normalize DNA, reject/skip empty strings and any symbol outside A/T/G/C, and save a summary under the original identifier for each accepted sequence. Print ID, length, all four counts and GC percentage. Report longest and shortest; first accepted input wins equal-length ties. Report unique identifiers or symbols using a set. No file reading/writing is required; input data is in code.

Self-check: Seed_A length4 A1 T1 G1 C1 GC50.0; Seed_B length4 A2 T2 G0 C0 GC0.0; Seed_C length6 A0 T0 G3 C3 GC100.0; Seed_D length2 A1 T1 G0 C0 GC0.0. Longest Seed_C 6; shortest Seed_D 2. All four identifiers and symbols are unique members of their sets. Replace the data with {"First":"AT","Second":"GC"}: First wins both ties. Test {} -> no valid sequences; {"Bad":"N","Good":"gc"} -> Bad skipped, Good both extremes with GC100.0. Restore the homework data before submission.

Submit the script and structure-choice note through the teacher's chosen channel. Success: every row matches, IDs are retained, ties deterministic, invalid strings never divided, synthetic label and limits stated. If blocked, submit your attempt plus a specific error. [Reference](solutions/06_SOLUTIONS.md).
