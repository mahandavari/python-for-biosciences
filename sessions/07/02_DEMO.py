# Synthetic educational data; no external service. Outputs go under the working folder.
from pathlib import Path
import file_tools

# __file__ is the saved script path, independent of the terminal's current folder.
course_root = Path(__file__).resolve().parents[2]
input_path = course_root / "datasets" / "session-07" / "sequences.fasta"
output_folder = Path.cwd() / "outputs"
output_folder.mkdir(exist_ok=True)
output_path = output_folder / "demo_report.csv"
try:
    records = file_tools.read_fasta(input_path)
    file_tools.save_report(records, output_path)
    print("Saved records:", len(records))
    print("Report:", output_path.name)
except FileNotFoundError:
    print("Missing input. Check that the whole course folder was extracted.")
except ValueError as error:
    print("Invalid input:", error)
