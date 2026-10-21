# Session 06 explained answers

[Reference notebook](06_SOLUTIONS.ipynb) answers practice 1-5 with runnable cells. Task 1: count is the parameter, 3 the argument; double_count returns 6, then reuse gives 12. Task 2: a print-only call shows a value but returns None. Task 3: add_flanks(2,3)=8; outer length stays 20. Task 4: statistics.mean gives 6; import binds the module name and the dot selects its function. Run the lesson demo for the actual two-file import. Task 5: GCGC gives A0 T0 G2 C2, GC100%, positions[0,2]. Invalid DNA/motif gives None for analysis; valid absent/long motif gives [].

Task 6: [03_DEBUG_ANSWER.py](03_DEBUG_ANSWER.py) changes the loop to range(len(sequence)); ATGA gives 2, A gives1, AAAA gives4, TT gives0. Returning the count allows assertions and composition. Run with `python "sessions/06/solutions/03_DEBUG_ANSWER.py"` from course root.

Homework: [homework_dna.py](homework_dna.py) contains the reusable definitions; [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) imports it. Run the latter from the course root with its full relative path. Expected rows match the homework hand counts, followed by Five homework checks passed. The module performs no output or file access when imported.

Assessment key (one point each): 1. count parameter, 3 argument. 2. return supplies a value to the caller; print displays it and the function ends with None. 3. No, the local name belongs to that call. 4. Step Into/F11; highlighted line executes next. 5. [0,2]; assert may be disabled, so runtime guards must remain explicit.
