# Session 10 practice

All sequences/files are synthetic educational examples. Try before opening answers.

1. **Seq, 10-30.** Predict length, first base, slice `[:3]`, string and reverse complement of `Seq("AAGC")`. Run a short cell. Does creating Seq validate the final project's policy?
2. **SeqIO, 30-50.** Read datasets/session-07/sequences.fasta with SeqIO. Print each ID, description, sequence and length. How are two lines joined? Is `synthetic` part of the ID? Is lowercase changed? Independently read homework.fasta and predict its three IDs first.
3. **Policy, 50-60.** Which strings pass A/C/G/T validation after trimming ends and converting to uppercase: `ATGC`, `atgc`, `ATN`, `""`, `AT GC`? Does successful parsing establish validity? What happens if two records have ID `Same`?
4. **Guided build, 70-105.** Follow 03_PRACTICE.py. First write input/process/output in three sentences. Read all records; reject empty/invalid/duplicate records; call existing functions; append rows; only then save CSV. Predict Seed_A's GC by hand. Open the saved file and compare all three rows.
5. **Independent change inside the guided block.** In a copy of the script add a `g_count` CSV column using the returned counts dictionary. Keep the other columns. Predict and verify all three G counts. This small change does not complete the final project.
6. **Progress review, 105-115.** Identify three final-project features still missing. Explain one file/kernel blocker and one descriptive statement supported by the invented data.

If blocked live, write predicted records/rows on paper and check notebook expected values. Save the programming attempt for later.
