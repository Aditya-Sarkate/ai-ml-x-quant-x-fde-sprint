import json
from pathlib import Path

from .models import Expense


def load_expenses(file_path: Path) -> list[Expense]:
    """Load expenses from JSON, returning an empty list if absent."""
    if not file_path.exists():
        return []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Expense data must be a JSON list.")
        return [Expense.from_dict(item) for item in data]
    except json.JSONDecodeError as exc:
        raise ValueError("Expense file contains invalid JSON.") from exc


def save_expenses(file_path: Path, expenses: list[Expense]) -> None:
    """Save expenses to JSON."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data = [expense.to_dict() for expense in expenses]
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
