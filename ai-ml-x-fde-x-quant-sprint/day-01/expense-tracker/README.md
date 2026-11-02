# Expense Tracker

A beginner-friendly CLI expense tracker built for Day 1.

## Features
- Add and delete expenses
- View expenses
- Search by category
- Show total, average, and highest expense
- Persist records as JSON
- Validate input
- Automated tests with pytest

## Setup

From the repository root:

```bash
python -m venv .venv
```

Activate the environment, then:

```bash
python -m pip install -r day-01/expense-tracker/requirements.txt
```

## Run

```bash
cd day-01/expense-tracker
python -m src.expense_tracker.main
```

## Test

From the repository root:

```bash
python -m pytest day-01/expense-tracker/tests
```

## Future improvements
- Currency configuration
- Date field and monthly reports
- CSV export
- SQLite or PostgreSQL storage
- REST API
- Authentication
- Docker
