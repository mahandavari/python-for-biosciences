# Session 08 explained answers

[Reference notebook](06_SOLUTIONS.ipynb) runs every practice and the full homework. [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) is the same homework workflow as a portable script; run from course root with `python "sessions/08/solutions/05_HOMEWORK_ANSWER.py"`. Select the environment from 02_ENVIRONMENT.md first.

1. Array shape(3,), integer dtype, first1, slice[3,5], mean3 mm, sum9 mm.
2. List operations concatenate/repeat [2,4,6,2,4,6]. Array operations give [4,8,12]; +1 gives[3,5,7]. List+1 has no concatenation partner list.
3. Series uses gene labels; DataFrame has gene_id and numeric columns with default row labels0/1/2. All columns must have equal length.
4. Shape(4,4); A/C integer, B floating with NaN, IDs text. loc[0,'gene_id'] gives Gene_A; iloc[0,1] gives10. Filter>=4 retains A/B/C; ascending order C/A/B. Keep gene_id when filtering.
5. A mean8, median7, min0, max18, sample SD sqrt(184/3)=7.83156 AU. B observed n3, mean32/3=10.66667 AU; no-skip mean NaN. One blank B value. NumPy ordinary mean propagates NaN.
6. A>=10 keeps Gene_A/Gene_B; descending IDs Gene_B/Gene_A/Gene_C/Gene_D. Interpret only these fictional values, with explicit units and observed counts.

Homework: D mean4 median4 min0 max8 sample SD sqrt(40/3)=3.65148 AU. E mean4 uses n3; skipna=False gives NaN. Missing is not zero. The script shows info/dtypes, selected columns, loc/iloc, filtered and sorted IDs and all summaries. No biological significance follows.

Assessment key (one point each): 1. Invoke pip with the intended Python, select that script interpreter and notebook kernel, compare sys.executable and restart. 2. [2,4,2,4] versus [4,8]. 3. Labeled one-column Series versus rectangular DataFrame; loc uses labels, iloc positions. 4. Mean8 median7, sample SD divides squared deviations by n-1=3. 5. isna marks missing, count counts observed, mean skips missing by default, no-skip returns NaN; no significance claim is supported.
