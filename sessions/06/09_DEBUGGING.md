# Debug a synthetic DNA counter in VS Code

1. Open the whole course folder. Open sessions/06/03_DEBUG_ME.py; save a copy for repair. Check the copy keeps its .py ending.
2. Use Python: Select Interpreter from the Command Palette. Ensure the Microsoft Python and Python Debugger extensions are enabled. See setup if missing.
3. Click the left gutter beside `observed = count_a(sequence)`. A filled red dot is a breakpoint. Clicking again removes it. Place another inside the loop on the if line.
4. Choose Run > Start Debugging (F5), then Python Debugger > Python File if prompted. Debug the currently open Python file. No launch.json is needed for this local example. Menu names may vary by extension version.
5. The highlighted line is the next statement to execute, not a line already completed. Expand VARIABLES to inspect sequence. Hover over a name to inspect it too. At the outer call, observed does not exist yet.
6. Press Step Into (F11) at the call to enter count_a. CALL STACK shows the active function above its caller. Selecting a frame shows that frame's variables; local a_count belongs to the function.
7. Step Over (F10) executes the current statement and pauses at the next one. On a function call it normally executes the call as one step, though a breakpoint inside can still stop it. Watch a_count, position and sequence as the loop repeats.
8. Write down visited positions. For ATGA they are 0, 1, 2; the A at index 3 is never checked. Before changing code, explain which upper boundary caused this.
9. Continue (F5) runs until the next breakpoint or program end. Stop (Shift+F5) ends a session. Remove the inner breakpoint if it interrupts too often. Save your repair and start again.
10. Run the repaired file normally too. Add assertions for final-index A, single A, all A and no A. Compare against hand counts. See the separate solution only after trying.

Checklist: correct saved file and interpreter; reachable breakpoint; expected input; next line versus completed line; correct stack frame; loop boundary; one small repair; rerun checks. A hollow breakpoint may be unbound: confirm the running file matches the open file. If F keys control hardware, use toolbar buttons. ModuleNotFoundError: keep the local files together and avoid module-name collisions. No GUI interaction is claimed by these instructions; text was checked against the [official VS Code debugging documentation](https://code.visualstudio.com/docs/python/debugging).
