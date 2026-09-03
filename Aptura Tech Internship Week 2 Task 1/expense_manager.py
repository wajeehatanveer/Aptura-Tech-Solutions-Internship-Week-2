import json
import os
from datetime import datetime


class ExpenseManager:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from the JSON file."""
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                print("Warning: Invalid data format. Starting with empty records.")
                return []

        except json.JSONDecodeError:
            print("Warning: JSON file is corrupted. Starting with empty records.")
            return []

        except OSError:
            print("Error: Unable to read expense file.")
            return []

    def save_expenses(self):
        """Save expenses to the JSON file."""
        try:
            with open(self.file_name, "w") as file:
                json.dump(self.expenses, file, indent=4)

            return True

        except OSError:
            print("Error: Unable to save expenses.")
            return False

    def add_expense(self, amount, category, description, date=None):
        """Add a new expense."""

        if amount <= 0:
            return False, "Amount must be greater than zero."

        if not category.strip():
            return False, "Category cannot be empty."

        if not description.strip():
            return False, "Description cannot be empty."

        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "id": len(self.expenses) + 1,
            "amount": round(float(amount), 2),
            "category": category.strip().title(),
            "description": description.strip(),
            "date": date
        }

        self.expenses.append(expense)

        if self.save_expenses():
            return True, f"Expense added successfully! ID: {expense['id']}"

        return False, "Expense could not be saved."

    def get_expenses(self):
        """Return all expenses."""
        return self.expenses

    def search_expenses(self, keyword):
        """Search expenses by category or description."""

        keyword = keyword.lower().strip()

        return [
            expense
            for expense in self.expenses
            if keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
        ]

    def filter_by_category(self, category):
        """Return expenses belonging to a specific category."""

        category = category.lower().strip()

        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category
        ]

    def monthly_total(self, month):
        """
        Calculate total expenses for a specific month.

        Month format: YYYY-MM
        """

        total = 0

        for expense in self.expenses:
            if expense["date"].startswith(month):
                total += expense["amount"]

        return round(total, 2)

    def delete_expense(self, expense_id):
        """Delete an expense by ID."""

        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()

                return True, "Expense deleted successfully."

        return False, "Expense ID not found."
    
    
if __name__ == "__main__":
    manager = ExpenseManager()

    success, message = manager.add_expense(
        1000,
        "clothes",
        "New shirt"
    )

    print(message)

    print("\nAll Expenses:")

    for expense in manager.get_expenses():
        print(expense)