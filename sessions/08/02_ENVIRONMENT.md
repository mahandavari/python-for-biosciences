# Session 08 environment setup

A package supplies code beyond Python's standard library. pip installs packages for one interpreter. A virtual environment keeps a project's packages separate. Use the Python version checked during course setup; the course combination was tested with Python 3.12.14 on Windows. This is a tested combination, not a claim to be the newest release.

Before class, download the complete folder and finish notebook setup. In VS Code open the student-course folder, then a PowerShell terminal at that folder. Run commands one at a time:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip --version
python -m pip install -r requirements.txt
python -m pip check
python -c "import sys, numpy, pandas; print(sys.executable); print(numpy.__version__, pandas.__version__)"
```

Use your working `py` command to create the environment if python is unavailable. `-m` runs a module with the named interpreter; requirements.txt lists exact direct package versions. Expected imports: NumPy 2.2.6, Pandas 2.2.3. The executable should be inside this course's .venv. Do not recreate an existing working .venv without checking with the teacher. `deactivate` leaves the environment; it does not delete it.

If PowerShell blocks Activate.ps1, keep the policy unchanged and use explicit paths:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -c "import sys, numpy, pandas; print(sys.executable); print(numpy.__version__, pandas.__version__)"
```

In the Command Palette choose Python: Select Interpreter, then this folder's .venv/Scripts/python.exe. This selects the script interpreter. In each notebook use Select Kernel > Python Environments and select the same environment; this is a separate choice. Restart the kernel and run the first version cell. Terminal success alone does not prove the notebook uses it. ipykernel from requirements supplies notebook support; VS Code extensions install separately.

ModuleNotFoundError: compare sys.executable in terminal and notebook, install through that exact interpreter and restart the kernel. A missing .venv selection: use Enter interpreter path and browse to its python.exe. pip not found: ensure `python -m pip` refers to the interpreter you intended. Do not install into a random system Python or change global PATH. A network failure is different from an incompatible wheel; preserve the complete error.

Initial installation needs internet or pre-downloaded matching wheels. Teacher preparation, outside live time: from a working compatible Windows/Python machine run `python -m pip download -r requirements.txt -d wheelhouse`. Transfer the full wheelhouse and course folder. Install offline using `python -m pip install --no-index --find-links wheelhouse -r requirements.txt` in the intended environment. Wheels must match Windows architecture/Python version. Do not copy a venv between machines. Offline wheel installation has not been tested in this stage; if packages are unavailable, trace notebook expected outputs during class and repair after class. Spend only the locked 20-minute segment on the demo/checkpoints, keeping longer downloads outside class.

References: [Python venv](https://docs.python.org/3.12/library/venv.html), [pip install](https://pip.pypa.io/en/stable/cli/pip_install/), [VS Code environments](https://code.visualstudio.com/docs/python/environments).

The complete course requirements also install Matplotlib 3.11.2 for Session 09 and Biopython 1.88 for Session 10. After updating the downloaded folder, repeat the requirements command in this same environment. Check `python -c "import matplotlib, Bio; print(matplotlib.__version__, Bio.__version__)"`; expected 3.11.2 and 1.88. Installing them here prepares later lessons; no plotting or Biopython concepts are required in Session 08.
