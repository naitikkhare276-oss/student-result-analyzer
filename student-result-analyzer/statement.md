# Problem Statement

## Problem Statement
In most classrooms and small institutions, calculating student totals,
percentages, grades, and identifying toppers is still done manually using
spreadsheets or by hand. This is time-consuming and prone to calculation
errors, especially as the number of students and subjects grows.

## Scope of the Project
This project provides a lightweight, console-based Student Result & Grade
Analyzer that:
- Stores student records in memory during a session (no external database)
- Automatically calculates totals, percentages, and letter grades
- Validates all user input (roll number format, name format, mark range)
- Generates class-level analytics (topper, average, pass/fail counts)
- Produces individual formatted report cards

The scope is intentionally limited to in-memory processing using core
Python data structures and functions — it does not include persistent file
storage, a graphical interface, or a database, as these are outside the
current syllabus scope.

## Target Users
- College/school faculty who need a quick way to process a small class's
  results without spreadsheet software
- Students learning Python fundamentals who want a practical reference
  project combining data structures, functions, modules, and regex

## High-Level Features
1. Add a new student record with validated input
2. View all student records in a summary table
3. Search for a specific student by roll number and view their report card
4. View class-level analytics: average percentage, pass/fail count, topper
5. View all students ranked by percentage (highest to lowest)
