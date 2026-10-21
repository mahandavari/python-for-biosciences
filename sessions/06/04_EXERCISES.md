# Session 06 practice

1. Guided, 10-30: define and call show_ready. Then write double_count(count) returning twice its argument. Save and reuse double_count(3); show 6 and 12. Explain parameter versus argument.
2. Independent, 10-30: compare a function that only prints len(sequence) with one returning it. Store both results; explain None. Avoid arithmetic on None.
3. Guided then independent, 30-45: trace add_flanks with a default and explicit flank. Predict add_flanks(2,3). Set outer length=20; prove it stays 20. Add a docstring.
4. Guided, 45-60: run 02_DEMO.py using dna_tools.py. Import statistics and calculate mean of [4,6,8]. Explain the dot and why neither import needs pip.
5. Independent, 60-80: combine the four DNA helpers for GCGC/GC. Record validity, all counts, GC, starts. Compare invalid N, empty DNA, empty motif, absent motif and motif longer than DNA. Explain None versus [].
6. Guided diagnosis then independent repair, 105-115: copy 03_DEBUG_ME.py; trace the visited positions for ATGA. Repair it. Add three asserts for A, AAAA, TT. Run 08_CHECKS.py and explain why its asserts do not validate real user input.

[Answers](solutions/06_SOLUTIONS.md).
