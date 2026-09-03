from expense_manager import ExpenseManager


def display_expenses(expenses):
    """Display expenses in a readable format."""

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("=" * 75)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"Rs. {expense['amount']:>6.2f}"
        )

    print("=" * 75)


def add_expense(manager):
    """Take input and add a new expense."""

    print("\n--- Add Expense ---")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if not date:
        date = None
    else:
        try:
            from datetime import datetime
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    success, message = manager.add_expense(
        amount,
        category,
        description,
        date
    )

    print(message)


def search_expense(manager):
    """Search expenses by keyword."""

    keyword = input("\nEnter search keyword: ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = manager.search_expenses(keyword)
    display_expenses(results)


def filter_category(manager):
    """Filter expenses by category."""

    category = input("\nEnter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    results = manager.filter_by_category(category)
    display_expenses(results)


def monthly_total(manager):
    """Calculate monthly expense total."""

    month = input("\nEnter month (YYYY-MM): ").strip()

    try:
        from datetime import datetime
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format. Use YYYY-MM.")
        return

    total = manager.monthly_total(month)

    print(f"\nTotal expenses for {month}: Rs. {total:.2f}")


def delete_expense(manager):
    """Delete an expense by ID."""

    try:
        expense_id = int(input("\nEnter Expense ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    success, message = manager.delete_expense(expense_id)
    print(message)


def main():
    manager = ExpenseManager()

    while True:
        print("\n" + "=" * 40)
        print("        EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Filter by Category")
        print("5. Monthly Total")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_expense(manager)

        elif choice == "2":
            display_expenses(manager.get_expenses())

        elif choice == "3":
            search_expense(manager)

        elif choice == "4":
            filter_category(manager)

        elif choice == "5":
            monthly_total(manager)

        elif choice == "6":
            delete_expense(manager)

        elif choice == "7":
            print("\nThank you for using Expense Tracker! 👋")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()