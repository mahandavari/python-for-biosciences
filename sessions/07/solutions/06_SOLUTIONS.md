# Session 07 explained answers

[Reference notebook](06_SOLUTIONS.ipynb) runs text/CSV reads, all error fixtures and exact homework row checks. [03_PRACTICE_ANSWER.py](03_PRACTICE_ANSWER.py) is the full text/CSV writing and independent readback answer for tasks 2-3. It prints Read back: ATGCAT, Toy_A 6 and Toy_B 4; output files are named practice_sequence.txt and practice_lengths.csv under cwd/outputs. [file_tools.py](file_tools.py) is a self-contained reference copy so the solution runner needs no imports from other sessions.

1. Path.cwd() is the working folder; a relative outputs path starts there, resolve gives its absolute form. Quote shell paths with spaces.
2. sequence.txt -> ATGCAT, length6. The context manager closes the handle. The lesson's 03_TEXT_CSV.py is a full executable writing reference, producing outputs/practice.txt and practice.csv.
3. Toy_A length6, Toy_B length4. DictReader uses header keys; writerow writes one row. Use newline='' to avoid newline translation problems and UTF-8 for text.
4. Header IDs Toy_A and Toy_B; remaining words are descriptions. Wrapped lines join to ATGCAT and GCGC. FASTA has no CSV column structure.
5. Missing file -> FileNotFoundError; empty existing file -> ValueError No FASTA records; ATN -> ValueError Invalid DNA symbols; int('four') -> ValueError from conversion. Narrow handlers preserve unexpected bugs.
6. Demo header id,length,A,T,G,C,gc_percent; Toy_A,6,2,2,1,1,33.33333333333333 and Toy_B,4,0,0,2,2,100.0. Two runs overwrite the same named report with equal bytes. Input resolution follows __file__, outputs follow cwd.
7. Duplicate identifier: Same; Sequence before first header. Both fail explicitly. Building all rows before opening output avoids truncating an existing report on an invalid input record; OS write failures are outside that guarantee.

Homework: run [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) from course root with `python "sessions/07/solutions/05_HOMEWORK_ANSWER.py"`. It imports the adjacent reference module and writes outputs/homework_report.csv. Rows match the homework brief and notebook asserts. Read with csv.DictReader, compare all seven fields and require exactly three rows. Scientific interpretation: only composition of these invented strings, no experimental inference.

Assessment (one point each): 1. cwd; no. 2. close on block exit; correct CSV newline handling. 3. >; ATGC. 4. Absent path versus present content rejected by our reader. 5. w truncates existing output; validate first to prevent partial invalid-data reports.
