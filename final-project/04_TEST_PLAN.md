# Test plan

Use assert for programmer checks, try/except for expected user/file errors.
An assertion is not a replacement for runtime validation. Start with 05_CHECKS.py;
add tests to your own checks.py. Use copied fixtures in a scratch folder for edits.

| Input / action | Expected behavior |
| --- | --- |
| ATGC | A1 T1 G1 C1, length4, GC50.00 |
| atgc with end spaces | normalize to ATGC |
| AATT / GCGC | GC0.00 / 100.00 |
| ATATAT / ATA | [0,2], count2 |
| AAAAA / AAA | [0,1,2], count3 |
| ATGC / GC | [2], includes last legal start |
| AT / AT | [0] |
| AT / GCG or GC | [], count0 |
| Empty/space-only DNA; ATN; AT GC | ValueError with useful message |
| Empty motif or motif N | ValueError, no output change |
| data/empty.fasta | no records error |
| data/empty_record.fasta | empty DNA error naming Empty |
| data/invalid.fasta | restricted alphabet error naming Bad |
| data/duplicate.fasta | duplicate identifier Same error |
| data/no_header.fasta | missing FASTA header error |
| missing.fasta (not supplied) | missing file message |
| data/single.fasta | Solo, ATGC, one result |
| data/sequences.fasta | all five rows in 02_EXPECTED_RESULTS.md; wrapped/mixed-case input |
| successful rerun | same CSV bytes and chart values |
| invalid run after valid run | existing three output files remain unchanged |

Open CSV using csv.DictReader to compare exact header/order/values. Parse positions
by semicolons, treating the empty field as zero starts. Count must equal number of
starts. Visually check both axes/titles and the 0-100% GC scale; a file's existence
alone does not prove a correct chart. Record actual checks and any remaining limits.
