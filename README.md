# Grade Classifier

A command-line Python program that accepts a mark out of 100 and reports the corresponding letter grade. It validates user input and provides clear messages for empty, non-numeric, non-finite, and out-of-range values.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the project requirements:

```bash
pip install -r requirements.txt
```

## Run

```bash
python grade_classifier.py
```

## Example

```text
Enter your mark out of 100: 84
Result: 84.0% is classified as grade A.
```

The program uses the following grading scale:

- A: 80–100
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: Below 50

## Known limitations

- The program classifies only one mark each time it runs.
- The grading scale is simplified and may not match every institution.
- Results are displayed in the terminal and are not saved.