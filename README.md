# Python for Biosciences - From Zero to Scientific Programming

By Mahan Davari. A beginner Python course with biological examples: ten live online sessions, 120 minutes each, 20 hours total. No programming or bioinformatics experience is needed. All ten sessions and the final project assignment are included.

You will learn to write and debug small programs, validate DNA strings, search motifs, process files, summarize tables and make clear charts. The final homework combines these skills in a DNA Sequence Analyzer.

## Download, open and begin

Open the [public course repository](https://github.com/mahandavari/python-for-biosciences), choose **Code > Download ZIP**, then **Extract All** in Windows File Explorer. No Git installation, Git commands or GitHub account is needed for a public ZIP. A teacher-supplied complete folder is also suitable for offline access.

In VS Code, choose **File > Open Folder** and open the extracted folder containing `00_START_HERE.md`, `setup` and `sessions`. Keep every subfolder together. Begin with [00_START_HERE.md](00_START_HERE.md), then follow [setup](setup/README.md). If blocked, use [troubleshooting and the checklist](setup/04_TROUBLESHOOTING_AND_CHECKLIST.md).

## Sessions

Start each session's README for its file order. Session 01 uses `.py` scripts and written notes. Sessions 02-10 also use `.ipynb` notebooks in VS Code; run their cells from the top with the selected Python kernel. Attempt exercises and assessment before reading the separate `solutions` folder. Complete homework after class.

| Session | Main topic |
| --- | --- |
| [01](sessions/01/README.md) | Programming ideas, folders, Python, VS Code and your first script |
| [02](sessions/02/README.md) | Variables, types, input/output, arithmetic and first notebook |
| [03](sessions/03/README.md) | Conditions, Boolean logic and numeric validation |
| [04](sessions/04/README.md) | Strings, loops, DNA counts and overlapping motifs |
| [05](sessions/05/README.md) | Lists, tuples, dictionaries, sets and sequence summaries |
| [06](sessions/06/README.md) | Functions, scope, local modules, debugging and basic tests |
| [07](sessions/07/README.md) | TXT, CSV, FASTA, predictable errors and saved reports |
| [08](sessions/08/README.md) | Environments, packages, NumPy and Pandas |
| [09](sessions/09/README.md) | Matplotlib, chart choice, labels and PNG export |
| [10](sessions/10/README.md) | Biopython Seq/SeqIO and an initial integrated program |

After Session 10, complete the [DNA Sequence Analyzer assignment](final-project/00_START_HERE.md) as homework. Its TODO starter is deliberately incomplete. The complete final project solution is not distributed.

## Software and tested environment

Use Windows 10/11, Python and VS Code with Microsoft's Python and Jupyter extensions. [Python setup](setup/02_WINDOWS_PYTHON_AND_VSCODE.md) explains the Python 3.13 installer route and version checks. A working Python 3.12 installation can also be used; course execution was tested on Python 3.12.14. The Python 3.13 installer workflow has not been tested on a fresh computer.

Session 01 needs only Python. Before Session 02, follow [minimal notebook setup](setup/03_NOTEBOOKS.md) for ipykernel 7.4.0. In Session 08, use the [environment guide](sessions/08/02_ENVIRONMENT.md) and [requirements.txt](requirements.txt): the tested direct versions are ipykernel 7.4.0, NumPy 2.2.6, Pandas 2.2.3, Matplotlib 3.11.2 and Biopython 1.88. Repeat the requirements installation in that environment if your course download changes.

## Data, offline study and limits

All [datasets](datasets/README.md) are synthetic educational examples. They are not experimental evidence. GC percentages, exact motif matches, descriptive summaries and toy charts do not establish biological function or scientific discoveries. Necessary biology and computational limits are explained in the lessons. [Asset records](assets/README.md) give the original diagrams' provenance and reuse terms.

Initial software downloads and package installation need internet. After setup, the downloaded notes, expected outputs, scripts, diagrams and notebooks support offline practice. During class, use chat checkpoints or record predictions on paper if execution is blocked; no microphone or webcam is required. Ask the teacher for the homework submission channel.

All 43 Python files and 18 notebooks were checked on Python 3.12.14, including a new isolated environment installed from requirements.txt. The starter checks intentionally fail until the TODOs are completed. A fresh Windows installation, VS Code graphical workflow, offline wheel installation and a human beginner timing study have not been verified. Follow the setup checks on your own computer. No course-wide reuse license has been selected; the explicit CC0 terms for the original datasets and specified artwork apply only to those contributions.
