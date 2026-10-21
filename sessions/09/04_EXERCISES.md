# Session 09 practice

All data are synthetic. Attempt the tasks before opening answers. Add new cells after the relevant lesson section.

1. Independent, 10-25: choose a chart for gene categories, a collection of lengths, a count measured at ordered times, and paired length/GC values. Write x/y labels and units for each. Why should a line not connect arbitrary gene categories?
2. Guided, 25-50: build the gene bar chart one command at a time. Predict Gene_B=12 AU and Gene_C=4 AU first. Add a descriptive title, axes and a zero baseline. Save `practice_genes.png` with dpi=150, then display it. Explain what Figure and Axes represent and how saving differs from showing.
3. Independent, 50-70: for the eight sequence lengths, predict histogram counts for bins [0,5,10,15,20]. Then use [0,10,20], label both axes and save `practice_histogram.png`. Compare totals and describe how bin width changes the apparent distribution. Do not replace a histogram with one bar per ID.
4. Guided then independent, 70-85: read time_series.csv, print missing counts, draw the line with markers, and explain the gap at hour4. Save `practice_time.png`. State what would be misleading about inserting a zero at hour4. Do not drop the row and connect over it.
5. Independent, 70-85: identify the scatter coordinates for S01, S04 and S08, then plot all eight pairs. Save `practice_scatter.png`. Explain why the plotting inputs must come from matching rows. Does an upward pattern establish causality?
6. Practical, 85-110: read sequence_summary.csv again. Inspect shape/dtypes/missing counts. Guided: select sequence_id and gc_percent to plan a labeled bar chart. Independently finish it, then create a scatter chart of length against GC. Save `practical_gc.png` and `practical_scatter.png` under outputs/session-09. Use fresh Figure/Axes objects for each. State one descriptive observation and one unsupported conclusion for each. Compare two values against the CSV before saving.

Use the path and export commands from the lesson. If execution is blocked, sketch axes and values, record the exact error, and retry with the downloaded files. [Separate answers](solutions/06_SOLUTIONS.md).
