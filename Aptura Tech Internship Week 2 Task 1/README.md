**Aptura Tech Solutions — Python Internship**

**Week 2 — Task 1:**

# 💰 CLI Expense Tracker

A simple and user-friendly **Expense Tracker** developed in Python. The application allows users to record, view, search, filter, calculate monthly totals, and delete their expenses.

The project includes both a **Command-Line Interface (CLI)** as required by the task and an additional **Streamlit web interface** for a more interactive user experience.

---

## 🎯 Objective

The objective of this project is to build a practical expense management system using Python that demonstrates:

- File handling and data persistence
- JSON data storage
- Input validation
- Searching and filtering
- Monthly expense calculations
- Error handling
- Command-line interaction
- Streamlit-based frontend development

---

## ✨ Features

### CLI Features

- ➕ Add a new expense
- 📋 View all expenses
- 🔎 Search expenses by category or description
- 🏷️ Filter expenses by category
- 📅 Calculate total expenses for a specific month
- 🗑️ Delete an expense
- 💾 Store data persistently in a JSON file
- ⚠️ Handle invalid user input
- 🛡️ Handle missing or corrupted JSON files

### Streamlit Features

- 📊 Interactive expense dashboard
- 💰 Display total expenses
- 📝 Display total number of records
- 🏷️ Display number of categories
- 📈 Expense breakdown chart
- ➕ Add expenses through a form
- 📋 View expenses in a structured table
- 🔎 Search expenses
- 🏷️ Filter expenses by category
- 📅 Calculate monthly totals
- 🗑️ Delete expenses

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **JSON**
- **Object-Oriented Programming**
- **File Handling**
- **DateTime**

---

## 📁 Project Structure

```text
Task 1 - Aptura Tech Internship Week 2 Task 1/
│
├── app.py
├── cli.py
├── expense_manager.py
├── expenses.json
├── README.md
└── screenshots/
    ├── 01_dashboard.png
    ├── 02_add_expense.png
    ├── 03_view_expenses.png
    ├── 04_search_expense.png
    ├── 05_filter_category.png
    ├── 06_monthly_total.png
    └── 07_delete_expense.png
````

---

## ▶️ How to Run

### Run the CLI Version

```bash
python cli.py
```

---

### Run the Streamlit Version


```bash
streamlit run app.py
```


---

## 💾 Data Storage

All expense records are stored in:

```text
expenses.json
```

Each expense contains information such as:

* Expense ID
* Amount
* Category
* Description
* Date

Example:

```json
{
    "id": 1,
    "amount": 500.0,
    "category": "Food",
    "description": "Burger",
    "date": "2026-09-02"
}
```


---

## 🧪 Testing

The application was tested for the following operations:

| Test                    | Status   |
| ----------------------- | -------- |
| Add Expense             | ✅ Passed |
| View Expenses           | ✅ Passed |
| Search Expense          | ✅ Passed |
| Filter by Category      | ✅ Passed |
| Monthly Total           | ✅ Passed |
| Delete Expense          | ✅ Passed |
| Invalid Amount Handling | ✅ Passed |
| Invalid Date Handling   | ✅ Passed |
| JSON Data Persistence   | ✅ Passed |
| Streamlit Dashboard     | ✅ Passed |

---


## 📚 What I Learned

Through this project, I practiced:

* Python Object-Oriented Programming
* Working with JSON files
* Data persistence
* Exception handling
* Input validation
* Searching and filtering data
* Date-based calculations
* Building CLI applications
* Creating interactive interfaces using Streamlit
* Connecting a frontend with a Python backend

---



````