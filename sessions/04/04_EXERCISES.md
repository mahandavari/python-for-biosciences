# Session 04 practice

Use your own cells or script; all DNA is synthetic. Predict before running.

1. Guided then independent (10-30): for ATATAT, print index 0, index 5, [0:3], [2:5]. Explain excluded stop. Normalize `  atGc  ` with strip/upper; print length and A count.
2. Guided then independent (30-50): print each character of ATGCAT on its own line using for. Print 0,1,2 with while; update the counter. Use range to print each DNA index and character. Explain when each loop stops.
3. Guided then independent (50-65): count A in ATGCAT manually with a loop. Expand to A,T,G,C counters. Predict totals before running.
4. Guided then independent (65-80): implement the window search for ATA in ATATAT. Print each match position and final match count. Change to AAA in AAAAA. Explain shared characters, and why range needs +1. No lists yet.
5. Guided (80-105): build the DNA script in six parts. Run `  atGc  `/gc. Print all four base frequencies as count/length after validation, then check their sum is 1.
6. Independent (80-105): run empty DNA, ATN, AT GC, ATATAT/ATA, AT/ATG, ATGC/TT, ATGC/empty motif and ATGC/GN. State whether DNA is rejected, motif is rejected, or search succeeds with no match.
7. Independent (105-115): trace break and continue for ATNGC using the lesson. Explain why dropping N is inappropriate for the analyzer's rejection rule. Repair the missing +1 in a copy of the search. Test sequence=motif=ATGC to expose the error.

If behind, trace counters and windows on paper. [Separate answers](solutions/06_SOLUTIONS.md).
