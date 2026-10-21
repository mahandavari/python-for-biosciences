# Session 05 practice

Use your own cells or script. Synthetic inputs only; predict, run and compare.

1. Guided (10-30): create ["AT","GC","AT"]. Print index 0 and slice [:2]. Explain why repeated AT is retained.
2. Independent (10-30): replace the first item with ATAT, append TT, remove GC. Print the list and length; join ["CC"] using + without changing the original.
3. Guided (30-50): create a fixed tuple (10.0,12.0) in mm; access each value. Explain why a tuple suits a fixed pair and why item assignment would fail.
4. Independent (30-50): create {"One":"AT","Two":"GC"}. Print Two's value, change it to GCGC, add Three mapped to TT. Explain duplicate-key replacement.
5. Guided then independent (30-50): create set("AATG"); print size; add C; test C membership; remove C. Explain why there is no first set element by index.
6. Independent (50-65): predict the alias/copy cells. Choose a structure for an ordered changing group, a fixed pair, ID lookup, and unique symbols. For the ID dictionary, compare "One" in mapping with "AT" in mapping and "AT" in mapping.values().
7. Guided then independent (65-80): loop over keys and values. Create a nested summary for One with length=2 and gc_percent=0.0; retrieve length in two steps. Explain why each pair of brackets uses a key.
8. Guided then independent (80-110): build the multi-sequence script in parts. Compare every row with the notebook table. Change only input data to {"First":"AT","Second":"GC"}, then {}, then {"Bad":"ATN","Empty":"","Good":"  gc  "}. Explain ties, skipped records and count reset placement. Restore the original after experiments.

Debug during final block: diagnose >= in the longest test, a missing counts reset, and using summaries[0]. [Separate answers](solutions/06_SOLUTIONS.md).
