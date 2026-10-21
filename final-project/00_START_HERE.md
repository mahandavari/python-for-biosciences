# Start the final project

Prerequisites: Sessions 01-10, especially functions (06), files and errors (07),
environments/tables (08), plotting (09), and Seq/SeqIO (10).
Allow about 4-6 hours of homework, with extra repair time if needed.
Work in small steps; ask the teacher after recording a failing input and error.

1. Read [the specification](01_PROJECT_SPEC.md), [expected results](02_EXPECTED_RESULTS.md)
   and [rubric](03_RUBRIC.md).
2. Open the whole downloaded student-course folder in VS Code. Use the Session 08
   environment: `python -m pip install -r requirements.txt` from that folder.
   Use `.\.venv\Scripts\python.exe` instead of `python` if activation is blocked.
   Use the same interpreter for every command. No Anaconda or network data is needed.
3. Open [analyzer.py](analyzer.py). Keep the default input and motif `ATA` for your
   first complete run. Read each TODO and implement/test one function at a time.
   [04_TEST_PLAN.md](04_TEST_PLAN.md) describes checks before integration.
4. From the student-course root run `python final-project/analyzer.py`.
   The untouched starter prints a TODO message and writes nothing. After completion
   it must print a readable summary and write `outputs/final-project/report.csv`,
   `gc_by_id.png`, and `length_vs_gc.png`.
5. Run `python final-project/05_CHECKS.py` after implementing the first three functions.
   This small starting check intentionally fails on uncompleted TODOs. Add your own
   tests from the test plan. Check invalid files without losing existing output.
6. Complete [the submission checklist](06_SUBMISSION.md). Read ordinary lesson
   solutions only after an attempt; the final assignment has no distributed full solution.

Input paths use the saved script location. Output paths use the working directory:
always run from the student-course root for the locations stated above.
All software/data must be downloaded before offline work. Offline: trace the expected
tables on paper, record blockers, then retry execution when your environment works.
Do not upload your environment or the whole course folder.
