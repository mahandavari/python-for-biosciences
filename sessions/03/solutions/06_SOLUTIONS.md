# Session 03 answers

Try practice, homework and assessment first. Run [03_PRACTICE_ANSWER.py](03_PRACTICE_ANSWER.py) for Practices 1-5 at reading=10; change the assigned value for the other checks. [06_SOLUTIONS.ipynb](06_SOLUTIONS.ipynb) supplies the zero guard and the full fixed-count GC repeat. The input version is [02_DEMO.py](../02_DEMO.py).

1. At 10: True, False, False, False, True, True for ==, !=, >, <, >=, <=. At 9: False, True, False, True, False, True. Equality is included by <= and >=.
2. At 10: True, False, False for inside/outside/not equal. At 21: False, True, True. and requires both conditions; or requires at least one; not reverses the result.
3. 10 prints Positive; 0 prints Not positive. The unselected branch is skipped.
4. 9 Below; 10 Inside; 20 Inside; 21 Above. The elif runs only after the below test fails.
5. -1 Invalid; 0 Zero; 10 Positive valid. The outer block is four spaces, inner block eight. The inner decision applies only to valid values.
6. Zero prints No bases, with no division. 4/10*100 gives 40.0. A positive total does not rule out a negative component.
7. All zero: Invalid: total must be positive. One negative: Invalid: counts must be nonnegative. AT-only: total 10, 0.0, low. GC-only: total 10, 100.0, high. At (3,3,2,2): total 10, 40.0, middle. At (2,2,3,3): total 10, 60.0, middle. Mixed (30,20,25,25): total 100, 50.0, middle. Bands are artificial. See the notebook reference for the complete algorithm and explanations.
8. Missing colon is a syntax error: add `:`. Wrong upper comparison is a logical error: use `<= 60` because 60 belongs to middle. A good test includes the boundary itself.

Homework: [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py). Run six times with -1,0,9.5,10,20,20.5. The final results are invalid, zero, short, middle, middle, long, with the requested labels. Negative is checked first, then zero; after those fail, <10 means positive short. The next <=20 includes 10 and 20. All higher values are long. No biological standard is implied. float conversion of words still raises ValueError; assume finite numeric inputs.

Assessment: (1) assignment versus equality test; (2) True, because both parts are True; (3) zero division is undefined and invalid branches must skip it; (4) [07_ASSESSMENT_ANSWER.py](07_ASSESSMENT_ANSWER.py), which prints Invalid for -1; (5) missing colon is syntax, misclassification is logic, and 60% belongs to middle. One point per numbered question.
