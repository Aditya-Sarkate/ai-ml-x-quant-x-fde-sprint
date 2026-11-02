from pathlib import Path

import pytest

from src.expense_tracker.main import (
    add_expense,
    calculate_summary,
    delete_expense,
    filter_by_category,
)
from src.expense_tracker.models import Expense
from src.expense_tracker.storage import load_expenses, save_expenses


def test_add_expense():
    expenses = []
    expense = add_expense(expenses, 500, "Food", "Lunch")
    assert expense.id == 1
    assert expense.amount == 500
    assert len(expenses) == 1


def test_delete_expense():
    expenses = [Expense(1, 500, "Food", "Lunch"), Expense(2, 1000, "Travel", "Taxi")]
    assert delete_expense(expenses, 1) is True
    assert [expense.id for expense in expenses] == [2]


def test_delete_nonexistent_expense():
    expenses = [Expense(1, 500, "Food", "Lunch")]
    assert delete_expense(expenses, 99) is False
    assert len(expenses) == 1


def test_calculate_summary():
    expenses = [
        Expense(1, 500, "Food", "Lunch"),
        Expense(2, 1000, "Travel", "Taxi"),
        Expense(3, 1500, "Food", "Dinner"),
    ]
    summary = calculate_summary(expenses)
    assert summary == {"count": 3, "total": 3000, "average": 1000, "highest": 1500}


def test_filter_by_category_case_insensitive():
    expenses = [
        Expense(1, 500, "Food", "Lunch"),
        Expense(2, 1000, "Travel", "Taxi"),
        Expense(3, 1500, "Food", "Dinner"),
    ]
    assert len(filter_by_category(expenses, "food")) == 2


def test_invalid_amount():
    with pytest.raises(ValueError):
        add_expense([], -100, "Food", "Lunch")


def test_json_persistence(tmp_path: Path):
    file_path = tmp_path / "expenses.json"
    expenses = [Expense(1, 500, "Food", "Lunch")]
    save_expenses(file_path, expenses)
    assert load_expenses(file_path) == expenses
