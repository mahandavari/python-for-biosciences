# 4. Troubleshooting and pre-class checklist

Copy the last error message into class chat if you need help. Do not include private folders, account details or passwords. You can participate by typing a predicted output; no microphone or webcam is required.

| Symptom | Likely cause | Practical fix |
| --- | --- | --- |
| `python` is not recognized | Terminal cannot find Python | Reopen terminal, try `py --version`, then follow [Python setup](02_WINDOWS_PYTHON_AND_VSCODE.md); check before reinstalling |
| Microsoft Store opens | A Store execution alias takes priority | Check the conflicting alias in Windows Settings as explained in Guide 2 |
| Script runs with the wrong version | Wrong editor interpreter | Ctrl+Shift+P > Python: Select Interpreter; then use Run Python File in Terminal |
| No Python run button | Missing/disabled Python extension or wrong file type | Enable Microsoft's Python extension and save as `.py` |
| No notebook kernel | Missing ipykernel, Python or extensions | Follow [notebook setup](03_NOTEBOOKS.md); choose the Python where ipykernel is installed |
| Cell does not finish | Kernel busy or waiting for `input()` | Answer input box; otherwise Interrupt, Restart Kernel, then run in order |
| `NameError` in notebook | Earlier cell was skipped or name misspelled | Check spelling; restart and run from the top |
| `ModuleNotFoundError` | Package missing in this kernel | Check selected Python; use that interpreter's `-m pip` and reselect the kernel |
| Cannot open a path with spaces | Path split into several arguments | Quote the whole file path; for a quoted executable path in PowerShell use `&` before it |
| Python says it cannot open file | Wrong current folder | Use Get-Location and Get-ChildItem; open course root and a new terminal there |
| Code appears as plain text | File is really `.py.txt` or `.ipynb.txt` | In File Explorer enable View > Show > File name extensions (Windows 11), or View > File name extensions (Windows 10); rename carefully |
| Terminal will not open | Terminal profile or window problem | Terminal > Select Default Profile > PowerShell, then New Terminal; if unavailable use Windows PowerShell from Start while seeking help |
| Lesson or asset missing after download | ZIP not extracted, partial copy or extra outer folder | Extract All again; locate 00_START_HERE.md; keep the complete folder tree |
| `SyntaxError` | Python cannot read the instruction | Match quotes and parentheses; use straight quotes, not curly text-editor quotes |
| `ValueError` after number input | Text cannot become the requested numeric type | Enter `12.5` for float, `12` for int; use a decimal point and omit units |
| `ZeroDivisionError` | Denominator is zero | For Session 02 use a positive total nucleotide count; validation comes in Session 03 |

## Before Session 01

- [ ] I extracted the full course folder and can find `00_START_HERE.md`.
- [ ] I opened that folder in VS Code and can see Explorer and the terminal.
- [ ] Python's version check works with `python` or `py`.
- [ ] I selected that interpreter in VS Code and enabled the Python extension.
- [ ] I saved and ran a `.py` file; its message appeared in the terminal.
- [ ] I know how to share a short error or checkpoint in chat without private information.
- [ ] I downloaded the lessons and can read them if my connection drops.

## Before Session 02

- [ ] The Jupyter extension and ipykernel are ready.
- [ ] I selected a local Python kernel in `sessions/02/01_LESSON.ipynb`.
- [ ] I ran its first code cell and saw `Notebook is ready`.
- [ ] I can restart the kernel and know that input cells wait for my reply.

If behind during class, spend at most the current checkpoint on a repair. Then read expected outputs, answer by chat or on paper, and note the blocker. Retry after class using these guides. The lesson continues inside its scheduled time; you do not need to catch up by skipping explanations.
