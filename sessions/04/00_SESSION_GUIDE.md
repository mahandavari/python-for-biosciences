# Session 04 live guide

Loops, Strings, and Sequence Processing. Open [the notebook](01_LESSON.ipynb) first. Outcome: a beginner-built DNA sequence counter and exact overlapping motif search.
The topic labels and time boundaries below match the locked course schedule.

| Time | Learning purpose and screen demonstration | Student action/checkpoint | Expected result |
| --- | --- | --- | --- |
| 00-10 | Review. Trace guarded GC (3 min); predict branches (3); check/repair (4). | Explain why zero total skips division. | A valid branch protects the formula. |
| 10-30 | Strings, indexing, slicing, useful string methods. Explain and demonstrate (8); predict slices (4); Practice 1 and pause (8). | Mark positions and normalize mixed case. | Zero-based positions; stop excluded. |
| 30-50 | for, while, range. Live-code short loops (8); trace counters (4); Practice 2/repair (8). | Print characters, update a while counter. | A terminating while; range excludes stop. |
| 50-65 | Character traversal and nucleotide counting. Build A counter (4); expand four counters (5); Practice 3/pause (6). | Trace counters for ATGCAT. | A=2,T=2,G=1,C=1. |
| 65-80 | Motif search with indexing and loops. Trace windows (5); build search (5); Practice 4/pause (5). | Find ATA in ATATAT; include final start. | Positions 0 and 2, count 2. |
| 80-105 | DNA string analysis and GC calculation. Explain validation rules (4); build 02_DEMO.py (9); Practice 5-6 and repair (12). | Run mixed case, empty and invalid DNA. | Count only accepted A/T/G/C strings; guard division. |
| 105-115 | break, continue, edge cases. Demonstrate loop control (3); Practice 7 and trace edge cases (4); check (3). | Compare stopping with skipping. | Empty motif rejected; long motif gives zero matches. |
| 115-120 | Assessment. Attempt (3); check and set homework (2). | Explain an off-by-one mistake. | Last legal window is searched. |

Total: 120 contiguous minutes. All demonstrations, coding pauses, independent tasks and repairs fit inside these blocks. Homework is outside class. Enlarge the font; reveal one small code cell at a time. Ask students to predict before running. Use chat, reactions or private notes; no microphone or webcam is required.

Stop repairs at the block boundary. Offline: use the downloaded notebook text, diagrams and expected outputs to trace the algorithm on paper. If only Jupyter fails, use the script. Record a specific blocker and retry after class. No live download or external data service is needed after setup. Run scripts as whole programs; notebook cells share memory, so Restart Kernel then Run All checks the saved learning sequence.
