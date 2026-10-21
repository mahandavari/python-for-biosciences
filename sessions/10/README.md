# Session 10 - Introduction to Biopython and Final Project

Exactly 120 live minutes. Complete Sessions 01-09 first. Open the whole student-course folder in VS Code. Use the environment from [Session 08](../08/02_ENVIRONMENT.md) with the course requirements installed. No earlier notebook state is needed.

1. Read [00_SESSION_GUIDE.md](00_SESSION_GUIDE.md).
2. Open [01_LESSON.ipynb](01_LESSON.ipynb), select the environment's kernel, restart and run in order.
3. From the course root run `python "sessions/10/02_DEMO.py"` for Seq and SeqIO. Read [09_COMMON_ERRORS.md](09_COMMON_ERRORS.md) if blocked.
4. Build and run [03_PRACTICE.py](03_PRACTICE.py) in the 70-105 block using the same command pattern. It is a small guided example, not the completed final project.
5. Attempt [04_EXERCISES.md](04_EXERCISES.md) and [07_ASSESSMENT.md](07_ASSESSMENT.md).
6. Read [08_PROJECT_INTRODUCTION.md](08_PROJECT_INTRODUCTION.md) and [05_HOMEWORK.md](05_HOMEWORK.md), then follow the [final project](../../final-project/README.md).
7. After an attempt, open [ordinary lesson answers](solutions/06_SOLUTIONS.md) and [their notebook](solutions/06_SOLUTIONS.ipynb). These do not solve the final project.

[dna_tools.py](dna_tools.py) copies the Session 06 functions so scripts can import them without special path setup. Keep it beside the scripts. Those helpers normalize text. This lesson explicitly trims end whitespace and converts to uppercase, then validates the simplified project alphabet.

All data are synthetic educational examples. From the course root the guided script saves outputs/session10_initial/initial_summary.csv; from another terminal folder it saves below that folder. The notebook saves below the course root. The printed path identifies the location. Offline: read expected values and predict on paper, then retry after fixing the kernel. No remote service, microphone or webcam is needed.
