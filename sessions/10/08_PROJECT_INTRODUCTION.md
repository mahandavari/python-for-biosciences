# From the initial workflow to the final project

The live lesson starts a DNA Sequence Analyzer. The full assignment is homework. Open the [final project package](../../final-project/README.md) at minute 60 and read its start document, brief, outputs, rubric and submission checklist.

The initial workflow reads synthetic FASTA, validates all records, reuses our own count/GC functions, stores rows and writes a small CSV. Homework adds the complete nucleotide-count report, exact motifs with overlapping zero-based starts, at least two suitable saved charts, predictable error handling, tests and run documentation. Student-authored functions perform core calculations; Biopython handles parsing.

Policy: after parsing, DNA strings must be nonempty A/C/G/T after trimming end whitespace and converting to uppercase. Normalize motifs the same way. Internal spaces and N remain invalid. IDs are the first header token, must be nonempty and unique; duplicates reject all input before output. FASTA itself can represent ambiguous DNA, RNA or proteins. Successful parsing does not establish project validity. SeqIO joins wrapped lines and can remove format whitespace, so this is a policy for parsed sequence text, not every raw formatting detail.

| Assessment category | Weight | What earns credit |
| --- | --- | --- |
| Python fundamentals and program structure | 35% | Readable variables, loops, collections and student-authored functions working together. |
| File handling and output | 15% | Multi-record FASTA and correct reproducible CSV in the documented place. |
| Algorithmic and biological correctness | 15% | Correct counts, lengths, GC, overlapping motif positions and stated assumptions. |
| Data visualization | 10% | At least two suitable readable charts with truthful labels/units. |
| Error handling and testing | 10% | Clear handling of bad inputs and independently checked examples. |
| Documentation and reproducibility | 10% | Setup, run and submission instructions another learner can follow. |
| Scientific interpretation and limitations | 5% | Descriptive conclusions limited to synthetic examples, without function or experimental claims. |

Total 100%. See the full project rubric for marking details. No GUI, database, remote service, machine learning or advanced packaging is required. Continue later with larger files only after you can explain this small workflow and its limits.

## Small output tools you may use

Read these during the project-brief block; practice them while completing homework. They extend the file/string ideas already taught.

- `f"{value:.2f}"` converts a number to text with exactly two digits after the decimal point. For value 50.0 it gives `50.00`. This is output formatting, not a change to the GC formula. `round(value, 2)` alone does not guarantee two printed digits.
- `";".join(parts)` joins a list of strings with semicolons. For parts `["0", "2"]` it gives `0;2`. Convert numeric positions with `str(position)` in a familiar for loop before joining. An empty list joins to empty text. This describes positions in the CSV, not a new indexing system.
- `csv.DictWriter(handle, fieldnames=["name", "value"])` creates a CSV writer whose rows are dictionaries; fieldnames fixes header order. `writer.writeheader()` writes the column names. `writer.writerow({"name": "Toy", "value": "50.00"})` writes one row. Use an open text handle with newline="", just as in our list-row example. Both writer styles use the standard csv module. The project brief defines exact required columns.
- `row.copy()` makes a new outer dictionary. Editing the copy's text/number values leaves the original dictionary's values unchanged. Avoid sharing nested mutable containers here; this is a shallow copy. Copying can help format report text without changing numeric values used for charts.
- `output_folder.mkdir(parents=True, exist_ok=True)` creates any missing parent folders and accepts a folder that already exists. It does not grant permission to a protected location. Keep outputs under the documented local folder.

These tools do not replace your own count, GC or motif algorithms.

The starter's `if __name__ == "__main__": main()` calls the main function when you run the file as a script. Importing the module for small checks does not automatically run the whole workflow. `__name__` is a value Python supplies; this familiar if statement compares it with the special script value.

Optional file-format detail: `handle.tell()` remembers a position in an open file, `handle.readline()` reads one line, and `handle.seek(position)` returns to the remembered position. The project brief explains these if you choose to handle leading blank lines before a FASTA header; they are file-reading tools, not DNA algorithms. The supplied classroom FASTA starts directly with a header.
