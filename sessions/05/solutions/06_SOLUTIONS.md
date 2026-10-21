# Session 05 answers

Try first. Run [03_PRACTICE_ANSWER.py](03_PRACTICE_ANSWER.py) for compact collection examples; the lesson's small cells are full references for each mutation. [06_SOLUTIONS.ipynb](06_SOLUTIONS.ipynb) has fixed-input, runnable collection and multi-sequence answers. [05_HOMEWORK_ANSWER.py](05_HOMEWORK_ANSWER.py) is the separate complete homework script.

1. First AT; slice ['AT','GC']; list retains duplicates by design.
2. After replacement/append/remove: ['ATAT','AT','TT'], length 3. Addition with ['CC'] returns ['ATAT','AT','TT','CC']; original stays unchanged. remove selects the first equal value, not an index.
3. Tuple access gives 10.0 and 12.0. A fixed pair has stable positions; tuple item assignment fails because its stored references are immutable. It can still contain a mutable object in other examples.
4. Two initially GC, then GCGC; mapping ends {'One':'AT','Two':'GCGC','Three':'TT'}. Reassigning Two replaces its value; it does not create a duplicate key. Distinct IDs can have the same DNA value.
5. Initial unique-symbol count 3. Adding C makes C membership True; removal returns count to 3. Sets have no positional index/order contract.
6. Alias changes original to ['TT','GC']; a slice copy leaves original ['AT','GC'] while copy is ['TT','GC']. Choose list, tuple, dictionary, set respectively. Membership gives True,False,True: dictionary membership tests keys; values() exposes values. Copy is shallow.
7. Direct dictionary iteration or keys() visits One then Two; lookup prints their DNA. values() visits AT then GC. `record = summaries["One"]` then `print(record["length"])` gives 2; the first lookup gets a dictionary, the second a scalar.
8. Demo_A 6 A2 T2 G1 C1 about33.33%; Demo_B 2 A1 T1 G0 C0 0%; Demo_C 6 A1 T1 G2 C2 about66.67%; Demo_D 4 A2 T2 G0 C0 0%. Longest Demo_A (first of equal maximum); shortest Demo_B. For First/Second both length2, First wins both. Empty mapping prints No valid sequences. Bad and Empty are skipped; Good normalizes to GC, length2, G1 C1, GC100%, both extremes. The full script and notebook show the implementation.

Final debugging: use > for longest and < for shortest, retaining equality. Reset counts inside the outer ID loop but before the inner base loop. Use a known ID key rather than summaries[0]. A single sequence can be both shortest and longest.

Homework outputs are in the homework brief and solution notebook. A dictionary connects unique IDs to DNA, a nested dictionary saves named summary fields, and a set holds unique symbols. No independent biological conclusion follows. Inputs already have unique nonempty string IDs; duplicate literal keys would overwrite a record before the algorithm runs. Prevent that when preparing data.

Assessment: 1. list for mutable ordered group, tuple for fixed pair, dictionary for ID lookup, set for uniqueness. 2. True,False: keys versus values. 3. Repeated A collapses; sets have no positional indexing. 4. [07_ASSESSMENT_ANSWER.py](07_ASSESSMENT_ANSWER.py) prints 2. 5. First wins both; strict > prevents replacement on longest equality. One point per numbered question.
