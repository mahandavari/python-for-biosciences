# 3. Prepare notebooks before Session 02

Complete [Python and VS Code setup](02_WINDOWS_PYTHON_AND_VSCODE.md) first. Session 01 needs only scripts. Session 02 needs this minimal notebook setup; full package/environment study stays in Session 08.

## Extension and kernel

1. In VS Code Extensions, install **Jupyter**, published by **Microsoft** (`ms-toolsai.jupyter`). Keep the Python extension enabled too.
2. In the integrated PowerShell terminal at the course root, run:

```powershell
python -m pip install ipykernel==7.4.0
python -m pip show ipykernel
```

Use `py` instead if that is your working command. The first command installs only `ipykernel`, the Python notebook kernel, for minimal Session 02 readiness. The second shows its version and location. Save the full `requirements.txt` installation and environment study for Session 08, when NumPy and Pandas are taught. Installing needs internet; allow time before class. No browser Jupyter server or Anaconda is needed. If permission is denied or Python is school-managed, ask the teacher/administrator rather than running as administrator.

3. Open `sessions/02/01_LESSON.ipynb`. This file format stores text, code cells and outputs together.
4. At the notebook's upper right, choose **Select Kernel > Python Environments** (or **Select Another Kernel** first), then choose the same Python used for package installation. The editor interpreter and notebook kernel can differ; check both.
5. Click the first code cell's play triangle. Expect `Notebook is ready`. A number such as `[1]` means execution finished; `[*]` or a busy indicator means it is running.

The [official kernel guide](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) confirms that ipykernel is the Python package needed for local notebook execution in VS Code. The extension is installed separately in VS Code.

## Cells and order

A **Markdown cell** displays explanations, headings and links. A **code cell** contains Python. Click inside a code cell and press **Shift+Enter** to run it and move on. You can also use its play triangle. Running one cell does not run the cells above it automatically.

The kernel remembers names you create. Running cell 5 before cell 2 may fail because a name does not exist yet. Editing an earlier value does not update later results until you run those cells again. Execution numbers show when cells ran, not their place in the file.

Use **Restart Kernel**, confirm the restart, then **Run All** to check the notebook from a fresh state in top-to-bottom order. A restart clears remembered variables; it does not erase saved code. Some cells in our lesson ask for input. During Run All, enter a response in VS Code's input box and press Enter so execution can continue. Do not share private information. Save your work with **Ctrl+S**.

For your own short homework notebook, choose **File > New File > Jupyter Notebook**, add Markdown with **+ Markdown** and code with **+ Code**, select your kernel, then save with an `.ipynb` ending. Use the homework instructions for the name and content. Restart and Run All before submitting.

## If the kernel is missing

Check that the file ends in `.ipynb`, both extensions are enabled, Python itself runs, and `python -m pip show ipykernel` succeeds for the selected Python. Choose a local **Python Environment**, not an existing remote server. If VS Code asks to install ipykernel, use the intended interpreter. Reload VS Code after installation if the list is stale. A wrong interpreter often causes `ModuleNotFoundError` (Python cannot find a package).

If a cell seems stuck, check for an unanswered input box at the top of VS Code. Use **Interrupt** to stop work; restart the kernel if necessary, then run from the top. Do not repeatedly press Run while an input request is waiting.

Offline fallback: read the notebook's Markdown and expected outputs, write predicted answers on paper, and follow the screen share. Use the matching script for the GC example if scripts work. Record the missing-kernel message for help after class. Reading outputs is practice, not proof that your kernel works.

More help: [official notebook guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
