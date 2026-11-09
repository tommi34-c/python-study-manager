# Python Study Manager

[Suomi](README.md) | [English](README_EN.md)

**Version: v1.2 – In development**

## Project purpose

Python Study Manager is a Python learning project that I am developing into a study management application.

The goal is to track programming languages being studied, daily study hours, weekly progress, and, in future versions, learning goals.

The application is developed step by step while I learn Python fundamentals and software development workflows.

## Current features

| No. | Feature | Implementation | Status |
|---|---|---|---|
| 1 | Start the program from the terminal | `python study_manager.py` | Implemented |
| 2 | Ask for the student's name | `input()` | Implemented |
| 3 | Ask which programming language is being studied | `input()` | Implemented |
| 4 | Ask for today's study hours | `int(input())` | Implemented |
| 5 | Estimate weekly hours from one day's hours | `study_hours * 7` | Implemented |
| 6 | Display study information | `print()` and f-strings | Implemented |
| 7 | Evaluate the study day | `if`, `elif`, `else` | Implemented |
| 8 | Process seven study days | `for`, `range()` | Implemented |
| 9 | Ask for each day's study hours | `daily_hours` | Implemented |
| 10 | Add up the hours for the week | `total_hours += daily_hours` | Implemented |
| 11 | Display total weekly study hours | `print()` | Implemented |
| 12 | Calculate average daily study hours | `average_hours` | Implemented |

**Current state:** All 12 documented features have been implemented. The average daily study hours calculation has been successfully tested with seven days of study data.

The application is still under development. Planned improvements include functions, input validation, error handling, and persistent data storage.

Currently, study data is stored in memory and is lost when the program exits.

### Study-day feedback

| Daily study hours | Feedback |
|---|---|
| 0–1 | Keep practicing! |
| 2–3 | Good progress! |
| 4 or more | Excellent study day! |

### Technologies used

- **Programming language:** Python 3
- **Interface:** Command-line interface (CLI)
- **Development environment:** Fedora Linux KDE
- **Main source file:** `study_manager.py`
- **Data handling:** Variables and calculations in memory
- **Control structures:** Conditional statements and a `for` loop

## Development roadmap

1. **v1.0 – Collecting study information (implemented)**
   - Student name
   - Programming language
   - Daily study hours
   - Weekly hours estimate
2. **v1.1 – Conditional statements (implemented)**
   - `if`, `elif`, and `else`
   - Feedback based on daily study hours
3. **v1.2.1 – Repetition with `for` (implemented)**
   - `for` loop and `range()`
   - Tracking seven study days
   - Average daily study hours calculation implemented and tested
4. **v1.2.2 – `while` loop practice (planned)**
   - How a `while` loop works
   - Loop termination conditions
   - Processing user input in a loop
5. **v1.3 – Functions (planned)**
   - Organizing reusable logic with `def`
6. **v1.4 – Input validation (planned)**
   - Handling invalid input with `try` and `except`
7. **v2.0 – Saving data (planned)**
   - Study history in JSON and CSV files
8. **v2.1 – Study goals (planned)**
   - Setting and monitoring learning goals
9. **v3.0 – Database and reporting (planned)**
   - SQLite database
   - Study history
   - Progress charts

## Running the application

From the project directory, run:

```bash
python study_manager.py
```

The program asks for a name, a programming language, today's study hours, and the study hours for seven days. The program calculates the total study hours for seven days and displays the average daily study hours.

## Language

This document is in English. The Finnish project documentation is available in [`README.md`](README.md).

Note: The application currently displays feedback in Finnish.
The English messages above are translations for documentation.
