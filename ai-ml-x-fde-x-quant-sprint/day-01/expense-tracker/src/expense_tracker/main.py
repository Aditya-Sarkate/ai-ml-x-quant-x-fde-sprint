from pathlib import Path

from .models import Expense
from .storage import load_expenses, save_expenses

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "expenses.json"


def generate_id(expenses: list[Expense]) -> int:
    return max((expense.id for expense in expenses), default=0) + 1


def add_expense(
    expenses: list[Expense], amount: float, category: str, description: str
) -> Expense:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if not category.strip():
        raise ValueError("Category cannot be empty.")
    if not description.strip():
        raise ValueError("Description cannot be empty.")

    expense = Expense(
        id=generate_id(expenses),
        amount=amount,
        category=category.strip(),
        description=description.strip(),
    )
    expenses.append(expense)
    return expense


def delete_expense(expenses: list[Expense], expense_id: int) -> bool:
    for index, expense in enumerate(expenses):
        if expense.id == expense_id:
            del expenses[index]
            return True
    return False


def filter_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    return [
        expense for expense in expenses
        if expense.category.casefold() == category.strip().casefold()
    ]


def calculate_summary(expenses: list[Expense]) -> dict[str, float | int]:
    if not expenses:
        return {"total": 0.0, "average": 0.0, "highest": 0.0, "count": 0}
    amounts = [expense.amount for expense in expenses]
    return {
        "total": sum(amounts),
        "average": sum(amounts) / len(amounts),
        "highest": max(amounts),
        "count": len(expenses),
    }


def display_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("\nNo expenses found.")
        return
    print("\nExpenses")
    print("-" * 60)
    for expense in expenses:
        print(
            f"ID: {expense.id} | ₹{expense.amount:.2f} | "
            f"{expense.category} | {expense.description}"
        )


def get_positive_amount() -> float:
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    expenses = load_expenses(DATA_FILE)
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. Delete expense")
        print("3. View expenses")
        print("4. Search by category")
        print("5. Show summary")
        print("6. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            amount = get_positive_amount()
            category = input("Category: ")
            description = input("Description: ")
            try:
                expense = add_expense(expenses, amount, category, description)
                save_expenses(DATA_FILE, expenses)
                print(f"Expense added with ID {expense.id}.")
            except ValueError as exc:
                print(f"Error: {exc}")
        elif choice == "2":
            expense_id = get_integer("Expense ID: ")
            if delete_expense(expenses, expense_id):
                save_expenses(DATA_FILE, expenses)
                print("Expense deleted.")
            else:
                print("Expense ID not found.")
        elif choice == "3":
            display_expenses(expenses)
        elif choice == "4":
            category = input("Category: ")
            display_expenses(filter_by_category(expenses, category))
        elif choice == "5":
            summary = calculate_summary(expenses)
            print("\nSummary")
            print("-" * 30)
            print(f"Number of expenses: {summary['count']}")
            print(f"Total: ₹{summary['total']:.2f}")
            print(f"Average: ₹{summary['average']:.2f}")
            print(f"Highest: ₹{summary['highest']:.2f}")
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
