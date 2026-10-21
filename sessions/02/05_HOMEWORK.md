# Session 02 homework: three-measurement calculator

Create `02_measurement_mean.py` in this session folder. Use only concepts taught today.

Problem: calculate the arithmetic mean of three fictional seedling lengths, all in millimetres. These are synthetic educational values, not experimental evidence. Ask for three numbers using input, convert each to float, store them in descriptive variables, add them, divide by 3 and print the mean with `mm` in its label. Include one comment explaining that the values are synthetic. Explain the meaning of mm in a short notebook Markdown cell.

Run with 10, 12 and 14: expect `Mean length (mm): 12.0`. Run again with 2.5, 3.5, 6.0: expect `Mean length (mm): 4.0`. Enter numbers with a decimal point and no units. Use nonnegative lengths. This program assumes valid numeric input; input validation comes in Session 03. Do not claim a treatment effect from three invented numbers.

Also create `02_measurement_mean.ipynb`. Add a Markdown cell stating the problem, units, synthetic origin and assumptions. Add a short code cell using the fixed values 10.0, 12.0, 14.0, then print their mean. Add another Markdown cell stating the expected result and why changing a cell does not automatically update later outputs. Restart the kernel, Run All and save. The fixed-value notebook is deliberately easy to rerun; the script practices interactive input.

Submit those two files through the teacher's chosen channel. Do not include environments or caches. Completion: three numeric inputs work, both checks match, the notebook runs from a fresh kernel, and units/provenance/limits are clear. If blocked, include a short error note with your attempt. See [reference solutions](solutions/06_SOLUTIONS.md) after trying.
