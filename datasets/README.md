# Synthetic educational datasets

All values and identifiers below were invented directly as small UTF-8 text files for this course by Mahan Davari's course-development workflow, 2026-10-21. No sequence database, experiment, organism or external data source was used. Construction method: manually choose short DNA strings or nonnegative numbers that make hand checks easy. These original dataset contents are dedicated to CC0 1.0: [license](https://creativecommons.org/publicdomain/zero/1.0/). They are educational examples only, with no experimental evidential value.

## Session 07: sequence files

Shared directory: session-07. Sequence length is in bases on one represented strand; counts are letters; GC percentage = (G+C)/length*100 for valid nonempty ATGC DNA. No ambiguity symbols, internal whitespace, inferred function or species. CSV fields id and sequence are text. FASTA's first header token is ID; description words are not retained by our limited reader.

| File | Contents and purpose |
| --- | --- |
| [sequence.txt](session-07/sequence.txt) | atgcAT plus newline: normalize to ATGCAT, length6, GC33.333...%. |
| [sequences.csv](session-07/sequences.csv) | Header id,sequence; Toy_A=ATGCAT, Toy_B=GCGC. Same DNA as the FASTA for format comparison. |
| [sequences.fasta](session-07/sequences.fasta) | Two synthetic IDs, descriptions and wrapped sequence lines. Toy_A length6 A2 T2 G1 C1; Toy_B length4 G2 C2. |
| [homework.fasta](session-07/homework.fasta) | Seed_A=ATGC, Seed_B=AATT, Seed_C=GCGCGC. Lengths4,4,6; GC50,0,100%. |
| [empty.txt](session-07/empty.txt) | Deliberately zero bytes: empty existing-file error. |
| [invalid.txt](session-07/invalid.txt) | ATNG: invalid text-sequence fixture; N is outside our subset. |
| [invalid.fasta](session-07/invalid.fasta) | Bad=ATN: invalid-symbol FASTA fixture. |
| [duplicate.fasta](session-07/duplicate.fasta) | Same ID twice: explicitly rejected, never overwritten. |
| [no_header.fasta](session-07/no_header.fasta) | ATGC without a header: explicitly rejected. |

missing.fasta is deliberately absent; use it only to test FileNotFoundError. Blank FASTA lines are ignored; end whitespace is trimmed; lower case is normalized. Headers/records must be nonempty and IDs unique. Multi-line and multi-record input is supported. Descriptions are discarded by design, not interpreted as measurements. This is a teaching subset, not a production parser. No invalid record is silently skipped.

## Session 08: expression-like tables

Shared directory: session-08. A gene is a DNA region involved in a functional product. A sample is material measured in an experiment; here all samples and gene labels are fictional. **Rows = genes; numeric columns = samples; gene_id = text metadata.** Values are manually chosen, simulated expression-like measurements in arbitrary units (AU). They are not RNA-seq counts or normalized experimental expression. Zero is a defined zero value; blank is an unspecified missing measurement, not zero. No treatment groups, biological replicates, random sampling assumptions or significance model are supplied.

| File | Construction and checks |
| --- | --- |
| [expression.csv](session-08/expression.csv) | Gene_A/B/C/D by Sample_A/B/C. A=[10,18,4,0], B=[12,20,blank,0], C=[14,22,8,0]. One missing B measurement. Shape4x4 includes gene_id. A mean8, median7, sample SD sqrt(184/3) AU. B mean32/3 uses three observed values. |
| [homework.csv](session-08/homework.csv) | New genes P/Q/R/S by Sample_D/E/F. D=[2,8,0,6], E=[4,blank,0,8], F=[6,12,0,10]. One missing E measurement. D mean4 median4 sample SD sqrt(40/3) AU; E observed mean4. |

Pandas defaults to skipping missing values for mean/median/SD; show observed count and compare skipna=False. Sample SD uses n-1 (ddof=1), unlike NumPy's default ddof=0. Descriptive summaries are arithmetic on the invented numbers. Different means do not establish significant differential expression or a biological effect.

Keep this folder beside sessions when downloading. No dataset download or internet is needed after the folder and software are ready.

## Sessions 09-10 and final project

[Session 09 data](session-09/README.md) documents the original synthetic chart tables, fields, units, expected values and CC0 provenance. Session 10 reuses the synthetic Session 07 FASTA examples to compare manual reading with SeqIO. The [final project fixtures](../final-project/data/README.md) are kept with the assignment for clear input/output navigation; they include valid varied DNA and intentional error cases. No experimental dataset is used.
