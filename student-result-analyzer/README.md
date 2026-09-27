# Student Result & Grade Analyzer

A console-based, menu-driven Python application that manages student records,
calculates grades, and generates class analytics and report cards — built
entirely using core Python fundamentals (no external database or file storage).

## Overview

Teachers/admins often calculate percentages, grades, and class toppers
manually, which is slow and error-prone. This project automates that
process: an admin adds student records (roll number, name, marks in 5
subjects) during a session, and the system instantly computes grades,
searches records, ranks students, and prints a formatted report card.

## Features

- **Add Student** — validated roll number (regex), name, and 5 subject marks
- **View All Students** — tabular summary of every record
- **Search Student** — linear search by roll number, prints a full report card
- **Class Analytics** — class average, pass/fail count, class topper
- **Ranked List** — all students sorted by percentage (highest first)
- Input validation at every step (roll number format, name format, mark range)

## Technologies / Concepts Used

- Python 3 (standard library only — `re` module for regex)
- Core data structures: lists, dictionaries, tuples
- Custom modules: `student_utils.py`, `validators.py`, `report.py`
- Functions: required, default, variable-length (`*args`), and `lambda`
- Control flow: `while`/`for` loops, `if-elif-else`, `break`/`continue`

## Project Structure

```
student-result-analyzer/
├── main.py                # menu loop / program entry point
├── student_utils.py        # student record & grade calculation logic
├── validators.py            # regex-based input validation
├── report.py                 # formatted console output / report cards
├── test_calculations.py       # basic tests for core logic
├── README.md
└── statement.md
```

## How to Install & Run

1. Ensure Python 3.8+ is installed:
   ```bash
   python3 --version
   ```
2. Clone or download this repository.
3. Navigate into the project folder:
   ```bash
   cd student-result-analyzer
   ```
4. Run the program:
   ```bash
   python3 main.py
   ```
5. Follow the on-screen menu (options 1–6).

## Instructions for Testing

Run the included test file to validate grade calculation, input
validators, and record management logic:
```bash
python3 test_calculations.py
```
Expected output: `All tests passed successfully.`

## Sample Menu

```
========================================
   STUDENT RESULT & GRADE ANALYZER
========================================
1. Add Student
2. View All Students
3. Search Student by Roll Number
4. View Class Analytics
5. View Ranked List (Toppers first)
6. Exit
```

## Future Enhancements

- Persist records to a CSV/JSON file so data survives across sessions
- Add exception handling (`try/except`) for more robust input parsing
- Convert to an object-oriented design once classes are covered in the syllabus
- Add a GUI (Tkinter) or web front-end
