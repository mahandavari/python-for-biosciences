# Common errors and recovery

| Symptom | Check and action |
| --- | --- |
| No module named Bio | Biopython is the package name; Bio is the import name. Install course requirements with the intended Session 08 environment, select its kernel and restart. |
| No module named dna_tools | Keep local dna_tools.py beside the scripts. Run the notebook setup from course root or this session folder. |
| File not found | Extract the whole course including datasets/session-07. Check spelling, extension and printed paths. |
| Only one record appears | Use a loop over SeqIO.parse or list(...) inside the open-file block for multiple records. |
| Empty parsing result | Reject no records before opening an output. A FASTA header begins with >. |
| N or internal spaces rejected | Trim end whitespace and uppercase first. N/internal spaces still fail this project's subset. General FASTA is broader; Seq does not enforce our policy. |
| Duplicate IDs | Compare record.id, not description. Reject all input before writing; never silently overwrite records. |
| Reverse complement seems reversed | DNA strands run in opposite directions. Swap A/T and C/G, then reverse to represent the other strand in the same 5-prime to 3-prime direction. |
| GC too small | Percent is (G+C)/length times 100. Reject empty DNA first. |
| Blank CSV rows on Windows | Use newline="" when opening output for csv.writer. |
| Notebook needs yesterday's state | Restart Kernel and Run All. |

Offline expected values: Toy_A=atgcAT (6 bases), Toy_B=GCGC (4 bases). Guided CSV rows: Seed_A,4,50.0; Seed_B,4,0.0; Seed_C,6,100.0. Trace by hand and retry with [setup troubleshooting](../../setup/04_TROUBLESHOOTING_AND_CHECKLIST.md). No network is needed after downloading software/files.
