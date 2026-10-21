# Session 07 practice

1. Guided, 10-25: print Path.cwd(); build a relative outputs path and resolve it. Explain relative/absolute and why a folder with spaces is valid.
2. Guided then independent, 25-45: read datasets/session-07/sequence.txt with a context manager; normalize and report length. Write a new outputs/practice.txt, read it back. Never overwrite an input.
3. Independent, 25-45: read sequences.csv with DictReader. Write ID and length for each record with csv.writer. Set UTF-8/newline correctly. Read it independently and compare both rows.
4. Guided, 45-60: draw the two FASTA headers and wrapped lines from sequences.fasta. Reconstruct IDs and full sequences. Explain the description and our supported subset.
5. Guided then independent, 60-75: predict errors for missing.fasta (absent), empty.txt, invalid.fasta and int('four'). Catch only FileNotFoundError and ValueError and print helpful messages.
6. Independent, 75-105: run 02_DEMO.py from a folder with spaces. Locate outputs/demo_report.csv. Use a second reader and check the header, both IDs, counts, lengths and GC. Run twice and compare contents.
7. Independent, 105-115: try duplicate.fasta and no_header.fasta. Explain why duplicate IDs must not overwrite a prior record. Explain why errors are raised before opening the report.

[Separate answers](solutions/06_SOLUTIONS.md).
