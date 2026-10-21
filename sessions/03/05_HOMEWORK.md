# Session 03 homework: educational measurement ranges

Create `03_measurement_ranges.py`. Ask for one fictional seedling length in mm (millimetres) using float(input(...)). A seedling is a young plant. These synthetic values are invented; no experimental conclusion follows. Assume a finite numeric entry; text errors are not handled until Session 07.

Use if/elif/else: negative -> `Invalid: length must be nonnegative.`; zero -> `Teaching range: zero`; above zero but below 10 -> short; 10 through 20 inclusive -> middle; above 20 -> long. Prefix each valid label with `Teaching range:`. These are arbitrary educational ranges, not normal biological ranges.

Test -1,0,9.5,10,20,20.5: expected invalid, zero, short, middle, middle, long. Include a synthetic-data comment. Add a short note explaining how boundary equality is handled and why this program does not handle every possible typed response. Submit the script and that note through the teacher's chosen channel; no environment folder. Success means the six checks match and the range rules are explained. If blocked, include a runnable attempt or saved code and the exact error. [Reference](solutions/06_SOLUTIONS.md).
