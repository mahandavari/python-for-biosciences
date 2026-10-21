# 2. Install Python and VS Code on Windows 10/11

Use a normal user account. Ask your school administrator if installations are restricted. No Anaconda or Git installation is needed.

## Install standard Python

Use the official [Python Windows downloads](https://www.python.org/downloads/windows/). For this beginner course, choose the latest maintenance release of **Python 3.13**, with a normal Windows installer matching your computer (usually 64-bit). This is a maintained series with Windows installers; the author tested course execution separately on Python 3.12.14. Python 3.13 installation on your computer still needs the checks below. Do not choose an embeddable ZIP, source archive, pre-release or experimental free-threaded build. Python 3.14 also exists; this guide uses one stable installation route to keep the steps consistent.

1. Run the downloaded Python 3.13 Windows installer.
2. On its first screen, select **Add python.exe to PATH**. PATH is Windows' list of places to search for commands. This option lets a new terminal find Python.
3. Keep pip enabled. pip installs Python packages. Keep the Python launcher option if offered. The launcher provides the `py` command and can find installed Python versions. Administrator-only launcher installation is not required for the course.
4. Choose **Install Now** for your user account. Do not change unrelated system settings. Finish the installer.
5. Close old terminals and reopen PowerShell from the Start menu. An open terminal may still have the old PATH.

The newer Python install manager is another official route, but its screens differ. If you already have it, follow the official [Windows Python guide](https://docs.python.org/3/using/windows.html) and verify the selected runtime below. Do not install a second Python just because a command is missing.

## Verify Python and pip

Type each line in PowerShell, then press Enter. Do not type the surrounding code fences or a prompt such as `PS>`.

```powershell
python --version
python -c "print('Python is ready')"
python -m pip --version
```

The first command asks for Python's version (for example `Python 3.13.x`; `x` means a maintenance number). The second runs one short instruction; expect `Python is ready`. Here `-c` means run the following code. The third asks the selected Python to run its pip module and show its version and location; `-m` means run a module. Use `python -m pip` rather than an unrelated `pip` command so packages go to the same Python.

If `python` is not recognized, try:

```powershell
py --version
py -c "print('Python is ready')"
py -m pip --version
```

These do the same checks through the launcher. If they work, use `py` instead of `python` in later terminal commands. With the older launcher, `py --list-paths` lists installed versions and executable locations; the newer manager also offers `py list`. If neither works, select the interpreter in VS Code as described below and ask the teacher to help locate the installation. Do not assume it is absent.

If `python` opens Microsoft Store, search Windows Settings for **App execution aliases**. Check which `python.exe`/`python3.exe` alias is redirecting to the Store. If you installed Python by the normal installer, turn off only the conflicting Store aliases, reopen PowerShell, and retry. Do not disable a working install-manager alias blindly.

If pip is missing from your chosen standard Python, this command tries to add its bundled pip:

```powershell
python -m ensurepip --upgrade
```

`ensurepip` uses Python's included installer support. If it fails, use the original installer to Modify/Repair and enable pip, or ask for help. Do not download random repair scripts.

## Install and open VS Code

1. Download the Windows user installer from [Visual Studio Code](https://code.visualstudio.com/). Run it and follow the prompts. A desktop shortcut is optional.
2. Open VS Code. Choose **File > Open Folder** and select the extracted course folder from [Guide 1](01_TOOLS_AND_DOWNLOAD.md).
3. The **Explorer** at the left lists files. Click a filename to open it in the central **editor**. The tabs at the top switch open files.
4. Open **Extensions** at the left (the blocks icon). Search for **Python**, published by **Microsoft**, and install it. Extension identifier: `ms-python.python`.
5. Press **Ctrl+Shift+P** to open the Command Palette. Run **Python: Select Interpreter**. Select your installed Python. If it is missing, choose **Enter interpreter path** and browse to the `python.exe` you installed. Check the version and location, not just the first item.
6. Choose **Terminal > New Terminal**. This opens the integrated terminal below the editor. Use PowerShell. If VS Code offers automatic environment creation, it is not needed for these first two sessions; dedicated environment study comes in Session 08.

## Create and run a script

In Explorer, create a file named `my_first_program.py` inside `sessions/01`. Type:

```python
print("Python is ready")
```

Save with **Ctrl+S**. With this file open, choose **Run Python File in Terminal** (the play button near the editor's upper right). It uses the selected interpreter. Expect `Python is ready` in the terminal, then a new prompt. The command VS Code shows above the output is normal.

To run the supplied example yourself from a terminal whose current folder is the course root:

```powershell
python "sessions/01/02_DEMO.py"
```

This runs that file. Quotes keep a path with spaces together as one argument. If needed, use `py` instead of `python`. For an executable path with spaces, PowerShell needs `&` before its quoted path, for example `& "C:\Path To Python\python.exe" "sessions/01/02_DEMO.py"`. This is an example pattern; replace it with your own actual location. The run button avoids typing that location.

Check your location with `Get-Location` (show current folder) and `Get-ChildItem` (list its contents). You should see `sessions` and `setup` at the course root. Use **File > Open Folder** and create a new terminal there if the location is wrong. Do not type Python instructions directly at a PowerShell prompt. If you see `>>>`, you are inside interactive Python; type `exit()` and press Enter to return to PowerShell.

The [official VS Code Python guide](https://code.visualstudio.com/docs/languages/python) explains interpreter selection and file execution. Installation screens may change; use the checks above to confirm the result.
