# Python Study Manager

[Suomi](README.md) | [English](README_EN.md)

**Development version:** v1.2 – Fixed seven-day and flexible study tracking implemented and tested (10 November 2026).

**Status:** Active learning project. Input validation is the next development milestone.

## Project Overview

Python Study Manager is a command-line application (CLI) developed as a Python programming and software engineering learning project.

The application tracks programming study hours and provides feedback on daily progress.

Development follows an incremental workflow: learn the concepts, write code independently, review errors, test functionality, and commit verified changes using Git.

## Current Features

| No. | Feature | Implementation | Status |
|---|---|---|---|
| 1 | Start the application | `python study_manager.py` | Tested |
| 2 | Ask for the student's name | `input()` | Tested |
| 3 | Ask for the programming language | `input()` | Tested |
| 4 | Ask for daily study hours | `int(input())` | Tested with valid input |
| 5 | Estimate weekly study hours | `study_hours * 7` | Tested |
| 6 | Display student information | `print()`, f-strings | Tested |
| 7 | Evaluate daily progress | `if`, `elif`, `else` | Tested |
| 8 | Select a tracking mode | `choice`, `if`, `elif` | Tested |
| 9 | Fixed seven-day tracking | `for`, `range()` | Tested |
| 10 | Flexible study-day tracking | `while` | Tested |
| 11 | Calculate total study hours | `total_hours += daily_hours` | Tested |
| 12 | Count recorded study days | `day_count += 1` | Tested |
| 13 | Calculate average daily hours | Division | Tested |
| 14 | Generate study summaries | `print()` | Tested |
| 15 | Format averages to two decimals | `:.2f` | Tested |
| 16 | Version control | Git | In use |

## Daily Study Feedback

| Daily hours | Feedback |
|---|---|
| 0–1 | Keep practicing! |
| 2–3 | Good progress! |
| 4 or more | Excellent study day! |

The application currently displays its interface and feedback in Finnish.

The initial weekly estimate (`study_hours * 7`) is a projection based on a single day, not the total recorded in the tracking modes.

## Running the Application

Run the following command from the project directory:

```bash
python study_manager.py
```

The application first asks for the student's name, programming language, and today's study hours.

Two tracking modes are available:

**Option 1 – Fixed Seven-Day Tracking**

The application requests study hours for seven days and calculates total hours and the daily average.

**Option 2 – Flexible Tracking**

The application allows the user to record any number of study days.

Enter `k` to continue or `e` to finish.

The program calculates the total study hours, number of recorded days, and average daily hours.

Study data is currently held in memory and is not saved permanently.

## Functional Testing

### PY-SM-19.5 – Fixed Seven-Day Tracking

Test values: `3, 4, 2, 5, 3, 4, 2`

Expected and observed results:

```text
Viikon opiskelutunnit yhteensä: 23 tuntia
Päivittäinen keskiarvo: 3.29 tuntia
```

**Result: PASSED**

### PY-SM-19.6 – Flexible Tracking

Test values: `2, 4, 6`

Continuation responses: `k, k, e`

Expected and observed results:

```text
Viikon opiskelutunnit yhteensä: 12 tuntia
Opiskelupäiviä: 3
Päivittäinen keskiarvo: 4.00 tuntia
```

**Result: PASSED**

These tests verify normal application usage. Invalid inputs and additional edge cases have not yet been fully tested.

## Learning Progress

Detailed learning milestones and completed exercises are documented in [OPPIMISLISTA.md](OPPIMISLISTA.md).

## Development Roadmap

| Phase | Description | Status |
|---|---|---|
| v1.0 | Collect student information | Completed |
| v1.1 | Conditional statements and feedback | Completed |
| v1.2.1 | `for` loop and seven-day tracking | Tested |
| v1.2.2 | `while` loop exercises | Completed |
| v1.2.3 | Menu and flexible tracking | Tested |
| Next | Input validation with `try` and `except` | Planned |
| Planned | Invalid menu selection handling | Planned |
| Planned | Functions and modular structure | Planned |
| Planned | JSON and CSV data storage | Planned |
| Planned | Study goals and progress tracking | Planned |
| Future | SQLite database and graphical reporting | Proposed |

## Technologies

- **Programming language:** Python 3
- **Operating system:** Fedora Linux KDE
- **Interface:** Command-line interface (CLI)
- **Version control:** Git and GitHub
- **Main program:** `study_manager.py`
- **Data storage:** Runtime memory

## Version Control

Verified development commits:

```text
cdd8c4d feat: add fixed and flexible study hours tracking
87a7338 docs: update README and Python learning progress
```

## Documentation

- [Finnish README](README.md)
- [English README](README_EN.md)
- [Learning Progress](OPPIMISLISTA.md)

This project is developed for educational purposes and is under active development.
