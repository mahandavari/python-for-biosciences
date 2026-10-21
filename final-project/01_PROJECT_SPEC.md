# Project specification

DNA is represented here by one strand of base letters. A FASTA header starts with
`>`; its first whitespace-separated word is the record identifier. Later header
text is a description. Sequence lines can wrap. SeqIO joins these lines into a Seq.
Convert it with `str(record.seq)` for your own functions. Do not use a library GC
calculator or motif counter in place of the algorithms you learned.

## Inputs and explicit policy

Default: [data/sequences.fasta](data/sequences.fasta), exact motif `ATA`.
Normalize case to uppercase; function inputs trim end whitespace as in Session 06.
Reject empty DNA, empty motifs and every character outside A/C/G/T. Internal spaces
in function inputs are rejected. N and other IUPAC ambiguity symbols can be valid
biological sequence notation; this project deliberately accepts a smaller alphabet.
SeqIO parses FASTA layout and may remove whitespace in sequence lines. Therefore
validation applies to the resulting sequence, not the raw typography of the file.
Use the supplied conventional FASTA layout; checking every malformed FASTA dialect
is outside scope. Detect a file whose first nonblank line does not start with `>`.
Header IDs must be nonempty and unique; descriptions are not IDs. Reject duplicates,
including equal first words with different descriptions. Do not overwrite or skip them.
Ignore blank layout lines. Preserve input record order and ID spelling.

If the parser rejects blanks before the first header, use a text handle and find the
first nonblank line before parsing. `handle.tell()` records a file position;
`handle.readline()` reads one line (empty text at end); `handle.seek(position)` returns
to a saved position. Save the position before the first header, seek back to it,
then pass the handle to SeqIO.parse. These extend the file methods from Session 07.

Validate the motif and all records before opening output files. On invalid input,
stop the entire run with a useful message naming the problem (and record if known).
No partial report and no silent symbol replacement. Empty file/no records and missing
file are errors. An OS write failure must give a useful message; rollback after a
hardware/write failure is not required. Only the three named output files may be
overwritten on a successful rerun. Output folder creation uses mkdir(parents=True,
exist_ok=True), as taught in Session 07.

## Functions and processing

Write normalize_dna(text), count_bases(sequence), motif_positions(sequence, motif),
read_records(path), analyze_records(records, motif), save_report(rows, path),
and save_plots(rows, folder), or equally clear student-authored equivalents.
Use loops/dictionaries for A/T/G/C counts and a window loop moving one base for motifs.
Include the final possible start. Search the supplied strand only; no reverse-strand
or approximate search. ATATAT/ATA gives [0, 2]. Empty/invalid motifs are errors;
longer or absent valid motifs give [] and count 0. GC% = (G+C)/length*100 only
for validated nonempty DNA. Counts must sum to length. Calculate with full precision,
then format terminal and CSV GC to exactly two decimal places (Python f-string .2f
formatting, which rounds; do not truncate). Use numeric full-precision GC for plots.

Use Bio.SeqIO.parse for all records, a set for duplicate IDs, a list of dictionaries
for result rows, csv.DictWriter with newline='' and UTF-8 for reports. Explain any
alternative taught approach in your README. Core calculations must be your own.

## Required outputs and acceptance

Print one line per record with ID, length, four counts, GC, motif count and starts.
CSV header exactly: `id,length,A,T,G,C,gc_percent,motif_count,motif_positions`.
Save positions as zero-based integers joined by semicolons; no brackets. No matches
is an empty field. DictReader then reads each field as text. Use `str(position)`
and `';'.join(...)`; build the strings in an ordinary loop if needed.

Create a bar chart of GC percentage by ID, y-axis 0-100%, and a scatter plot of
sequence length (bases) against GC (%), y-axis 0-100%. Use descriptive titles,
readable labels and contrasting marks. Save PNGs at 150 dpi or better and close
figures after saving. Use at least (8, 5) inch figures. A legend is useful only if
more than one series is present. Do not connect unordered records by lines.
Files: outputs/final-project/report.csv, gc_by_id.png and length_vs_gc.png.
Small datasets make plots descriptive only. Association does not establish causality;
GC and an exact motif match do not identify species, regulation or biological function.

Acceptance: match all documented expected results and edge cases, create both
labeled plots, handle predictable errors, run twice reproducibly, and explain your
code and scientific limits. No GUI, database, API, advanced statistics or ML required.
