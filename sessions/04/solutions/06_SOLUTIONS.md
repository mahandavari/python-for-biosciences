# Session 04 answers

Try first. [03_PRACTICE_ANSWER.py](03_PRACTICE_ANSWER.py) runs character traversal, four-base counting, GC and overlapping search. [06_SOLUTIONS.ipynb](06_SOLUTIONS.ipynb) repeats the main algorithms and adds all four frequencies with fixed inputs. [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) is the complete interactive homework reference. It repeats the main algorithm so it can run alone.

1. A, T, ATA, ATA. Stop is excluded. Normalization gives ATGC, length 4, A count 1. Use `print(sequence[0])`, `print(sequence[5])`, `print(sequence[0:3])`, `print(sequence[2:5])` with sequence="ATATAT". `sequence = "  atGc  ".strip().upper()` stores the returned normalized string.
2. Character output is A,T,G,C,A,T on separate lines. `for position in range(len(sequence)):` then `print(position, sequence[position])` gives 0 A through 5 T. A while starting at 0 and adding 1 while <3 prints 0,1,2, then stops when 3<3 is False. for ends after its iterable is exhausted. See the lesson's runnable loop cells.
3. A=2,T=2,G=1,C=1; length 6; GC = 2/6*100, about 33.33%. Initialize counters before the loop and increment only the matching branch. Frequencies are 2/6,2/6,1/6,1/6; approximate decimals may not display an exact sum of 1 because of floating-point representation.
4. ATATAT/ATA gives starts 0 and 2, count 2. AAAAA/AAA gives 0,1,2, count 3. Each slice is compared at the next start, even if characters were part of an earlier match. Non-overlapping str.count would give 1 in both examples.
5. ATGC gives length 4, all counts 1, GC 50.0, gc at index 2, count 1. Each base frequency is 0.25; sum 1.0. See the solution notebook's frequency cell.
6. Empty/whitespace DNA rejected before division; ATN and AT GC rejected for invalid characters. ATATAT/ATA succeeds with two matches. AT/ATG and ATGC/TT succeed with zero. Empty motif rejected; GN motif rejected. Valid DNA counts still appear before a motif error. No partial summary is shown for invalid DNA.
7. break prints A,T then stops. continue skips N and prints A,T,G,C. The latter changes the input meaning, so do not use it to silently clean the analyzer's DNA. Add +1 to include start zero when sequence and motif are both ATGC; expected count 1 at 0.

Homework main case: ATGCATAT, length 8, A3,T3,G1,C1, 25.0%, position 4, count 1. Use the same guards/search as the script reference. Do not infer function or origin. Test failures reveal which algorithm step to revisit. Print positions separately; a positions list comes next session.

Assessment: 1. A and TG. 2. for visits an iterable; while repeats while a test is True; forgetting the update can prevent termination. 3. [07_ASSESSMENT_ANSWER.py](07_ASSESSMENT_ANSWER.py) prints A: 2. 4. Positions 0,2, count 2; count method excludes overlaps. 5. Range excludes stop, so +1 includes the last legal start; empty motif must be rejected explicitly. One point per numbered question.
