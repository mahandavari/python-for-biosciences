# Session 09 homework: three clear charts

Create `09_visualization_homework.ipynb` for the new synthetic table [homework.csv](../../datasets/session-09/homework.csv). Allow about 60-90 minutes after class. Complete it using Sessions 01-09 only. The table has six fictional sequence IDs, lengths in bases and GC percentages; it has no actual sequence strings or experimental evidence. Read the [data definitions](../../datasets/session-09/README.md).

1. State the question, input columns, row meaning and synthetic limitations. Read with Pandas. Show shape/dtypes and missing counts. Keep IDs with values.
2. Make at least three appropriate plots: GC percentage by identifier (bar); distribution of lengths with bins [0,5,10,15,20,25] (histogram); length versus GC percentage (scatter). A line joining these unordered IDs is not suitable.
3. Give every plot a clear synthetic title, readable axes with units, and a sensible scale. Bars start at zero; percentages stay within 0-100. Save PNGs with descriptive filenames under your `outputs` folder and display the figures in the notebook.
4. For each plot write four short sentences: what is shown; why this chart type fits; what can be concluded descriptively; what cannot be concluded scientifically. A legend is useful only when it identifies a real series distinction.
5. Restart the kernel and run all cells. Check that each exported PNG exists and is readable. Submit the notebook, three PNGs and your interpretation through the teacher's channel. Keep software environments, caches and unrelated files out of the submission.

Self-check: shape(6,3); zero missing values; HW_C=(10 bases,60%); HW_F=(20 bases,100%); histogram counts [0,2,2,1,1], totaling6. No significance, causality, gene function or species inference is possible from this invented table. [Answers after an attempt](solutions/06_SOLUTIONS.md).
