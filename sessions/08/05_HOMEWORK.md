# Session 08 homework: a new expression-like table

Load datasets/session-08/homework.csv using Pandas. Rows are invented genes Gene_P/Q/R/S; numeric columns Sample_D/E/F are fictional samples with nonnegative expression-like measurements in arbitrary units (AU). Blank E for Gene_Q is missing for an unspecified reason. IDs are metadata; numbers are hand-selected classroom examples, not RNA-seq counts or experimental evidence.

Submit one notebook or script and a short summary through the teacher's channel. Show CSV loading, head/info/shape/dtypes; select gene_id and Sample_D; use a labeled and a positional row selection; filter D>=6 keeping IDs; sort D descending; report D mean/median/min/max/sample SD; inspect missing values/counts and E mean with/without skipping. State denominators and units. Do not fill missing data or require plots.

Self-check: shape(4,4); filtered Gene_Q/Gene_S; sorted Q,S,P,R; D=[2,8,0,6], mean4 median4 min0 max8 sample SD about3.65148 AU. E observed [4,0,8], mean4 with n=3; skipna=False -> NaN; exactly one blank. Explain why differing numbers do not demonstrate significant differential expression. Restart and run all before submission. [Reference](solutions/06_SOLUTIONS.md).
