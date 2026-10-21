# Session 08 practice

Use fresh cells after the relevant teaching section. All inputs are invented.

1. Guided then independent, 30-50: create np.array([1,3,5]); print shape, dtype, first item, final slice, mean and sum. State units mm.
2. Independent, 30-50: predict list [2,4,6]+itself and *2, then array equivalents. Add1 to the array. Explain why list+1 is invalid.
3. Guided then independent, 50-75: create a Series with Gene_X/Gene_Y labels, then DataFrame with gene_id and Sample_X columns. Add Gene_Z=6 with matching column lengths. Describe the default row index versus gene_id metadata.
4. Independent, 50-75: read expression.csv; inspect head, info, shape, dtypes. Select Sample_A as a Series and gene_id/Sample_A as a frame. Use loc and iloc to get Gene_A and 10. Filter A>=4, then sort ascending. Keep IDs.
5. Guided then independent, 75-95: compute A mean, median, min/max and sample SD by hand then code. Print missing counts and observed B count. Compare B mean with skipna True/False. Explain why missing is not zero, and why NumPy mean behaves differently with NaN.
6. Independent, 95-110: complete the nine-minute practical workflow in the notebook, starting with the already loaded table. Produce filtered IDs, sorted IDs, missing counts and A summaries. Write two sentences on units, denominators and limits. No plots or significance tests.

[Separate runnable answers](solutions/06_SOLUTIONS.md).
