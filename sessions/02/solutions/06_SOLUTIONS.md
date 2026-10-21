# Session 02 answers

Try [practice](../04_EXERCISES.md), [homework](../05_HOMEWORK.md) and [assessment](../07_ASSESSMENT.md) first. You can run these scripts with the Python run button. Open the solution notebook in VS Code, select your kernel and Run All.

## Practice

[03_PRACTICE_ANSWER.py](03_PRACTICE_ANSWER.py) contains runnable answers. Its output, in order:

```text
Demo A <class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
12.5
10
14
20
3.5
3
1
8
Mean length (mm): 10.0
Total bases: 80
GC percentage: 25.0
```

1. Quotes make `sample_name` text (str). Whole 3 is int, 12.5 is float and True is bool.
2. float turns numeric text into a decimal number. int turns `"8"` into 8, so adding 2 produces 10. input returns text even when you type digits; numeric operations need numeric values.
3. Multiplication comes before addition; parentheses group addition first. `/` divides, `//` gives floor division, `%` gives the remainder, and `**` is a power. The three lengths sum to 30.0 mm; dividing by 3 gives 10.0 mm.
4. The original demo gives 100 and 50.0%. Changed counts give 80 and 25.0%, because (10 + 10) / 80 * 100 = 25. A total of zero would make division undefined. Counts alone do not show the sequence order.
5. [06_SOLUTIONS.ipynb](06_SOLUTIONS.ipynb) includes a complete fixed-count repeat and a fixed-value homework reference. Restart and Run All succeeds because definitions appear before use. The optional input run 0, 0, 5, 5 gives total 10 and 100.0%.

## Homework

[05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) converts three input strings with float, adds the numbers, divides the total by 3 and prints a unit label. Parentheses ensure the whole total is divided. Expected final lines for the two requested runs are `Mean length (mm): 12.0` and `Mean length (mm): 4.0`. Prompts appear before the final line.

The notebook reference in [06_SOLUTIONS.ipynb](06_SOLUTIONS.ipynb) states the units, synthetic origin and assumptions, and uses fixed values for repeatable execution. Numeric input is assumed; invalid text raises ValueError. Formal validation is in Session 03.

## Assessment (five points)

1. `type(12.5)` shows `<class 'float'>`; input returns str.
2. `count = int("8")` stores integer 8.
3. 14 and 20.
4. Total 10; GC percentage 60.0. Counts must be nonnegative whole numbers and total must be greater than zero.
5. Restart Kernel, then Run All, answering input prompts. This removes old memory and reruns in order. Editing alone does not recompute later cells.

[07_ASSESSMENT_ANSWER.py](07_ASSESSMENT_ANSWER.py) verifies the numeric quiz answers; its output is 8, `<class 'float'>`, 14, 20, `Total bases: 10`, `GC percentage: 60.0`, each on its own line.
