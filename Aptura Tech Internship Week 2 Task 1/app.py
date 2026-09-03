import streamlit as st
from expense_manager import ExpenseManager
from datetime import date


# PAGE CONFIG

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# BACKEND

manager = ExpenseManager()


# CUSTOM CSS

st.markdown("""
<style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: #fafafa;
        text-align: center;
    }

    .metric-title {
        font-size: 16px;
        color: #666;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 700;
    }

    div[data-testid="stMetric"] {
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 12px;
    }

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# SIDEBAR 

st.sidebar.title("💰 Expense Tracker")

option = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Expense",
        "View Expenses",
        "Search Expense",
        "Filter by Category",
        "Monthly Total",
        "Delete Expense"
    ]
)


# DASHBOARD 

if option == "Dashboard":

    st.markdown(
        '<div class="main-title">💰 Expense Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Track and manage your expenses easily.</div>',
        unsafe_allow_html=True
    )

    expenses = manager.get_expenses()

    total_expenses = sum(
        expense["amount"] for expense in expenses
    )

    total_records = len(expenses)

    categories = len(
        set(expense["category"] for expense in expenses)
    )

# SUMMARY CARDS 

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💵 Total Expenses",
            f"Rs. {total_expenses:,.2f}"
        )

    with col2:
        st.metric(
            "🧾 Total Records",
            total_records
        )

    with col3:
        st.metric(
            "🏷️ Categories",
            categories
        )

    st.divider()

# EXPENSE BREAKDOWN 

    if expenses:

        st.subheader("📊 Expense Breakdown")

        category_totals = {}

        for expense in expenses:
            category = expense["category"]

            category_totals[category] = (
                category_totals.get(category, 0)
                + expense["amount"]
            )

        st.bar_chart(category_totals)

        st.divider()

# RECENT EXPENSES 

        st.subheader("📋 Recent Expenses")

        recent_expenses = expenses[-5:]

        for expense in reversed(recent_expenses):

            st.write(
                f"**{expense['category']}** — "
                f"{expense['description']} — "
                f"Rs. {expense['amount']:,.2f}"
            )

    else:

        st.info(
            "No expenses added yet. Add your first expense!"
        )


# ADD EXPENSE

elif option == "Add Expense":

    st.title("➕ Add Expense")

    st.write(
        "Enter the details of your expense below."
    )

    with st.form("expense_form"):

        amount = st.number_input(
            "Amount (Rs.)",
            min_value=0.01,
            step=100.0
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Education",
                "Health",
                "Entertainment",
                "Other"
            ]
        )

        description = st.text_input(
            "Description"
        )

        expense_date = st.date_input(
            "Date",
            value=date.today()
        )

        submitted = st.form_submit_button(
            "➕ Add Expense"
        )

        if submitted:

            if not description.strip():

                st.error(
                    "Please enter a description."
                )

            else:

                success, message = manager.add_expense(
                    amount,
                    category,
                    description,
                    expense_date.strftime("%Y-%m-%d")
                )

                if success:

                    st.success(message)

                   

                else:

                    st.error(message)


# VIEW EXPENSES 

elif option == "View Expenses":

    st.title("📋 All Expenses")

    expenses = manager.get_expenses()

    if expenses:

        table_data = [
            {
                "ID": expense["id"],
                "Date": expense["date"],
                "Category": expense["category"],
                "Description": expense["description"],
                "Amount (Rs.)": expense["amount"]
            }
            for expense in expenses
        ]

        st.dataframe(
            table_data,
            use_container_width=True,
            hide_index=True
        )

        total = sum(
            expense["amount"]
            for expense in expenses
        )

        st.success(
            f"Total Expenses: Rs. {total:,.2f}"
        )

    else:

        st.info(
            "No expenses found."
        )


# SEARCH EXPENSE

elif option == "Search Expense":

    st.title("🔍 Search Expenses")

    keyword = st.text_input(
        "Search by category or description",
        placeholder="e.g. Food, Lunch, Transport..."
    )

    if keyword.strip():

        results = manager.search_expenses(
            keyword
        )

        if results:

            table_data = [
                {
                    "ID": expense["id"],
                    "Date": expense["date"],
                    "Category": expense["category"],
                    "Description": expense["description"],
                    "Amount (Rs.)": expense["amount"]
                }
                for expense in results
            ]

            st.dataframe(
                table_data,
                use_container_width=True,
                hide_index=True
            )

            st.write(
                f"**{len(results)} expense(s) found.**"
            )

        else:

            st.warning(
                "No matching expenses found."
            )


#FILTER BY CATEGORY

elif option == "Filter by Category":

    st.title("🏷️ Filter by Category")

    expenses = manager.get_expenses()

    if expenses:

        categories = sorted(
            set(
                expense["category"]
                for expense in expenses
            )
        )

        selected_category = st.selectbox(
            "Select Category",
            categories
        )

        results = manager.filter_by_category(
            selected_category
        )

        if results:

            table_data = [
                {
                    "ID": expense["id"],
                    "Date": expense["date"],
                    "Category": expense["category"],
                    "Description": expense["description"],
                    "Amount (Rs.)": expense["amount"]
                }
                for expense in results
            ]

            st.dataframe(
                table_data,
                use_container_width=True,
                hide_index=True
            )

            category_total = sum(
                expense["amount"]
                for expense in results
            )

            st.success(
                f"Total {selected_category} Expenses: "
                f"Rs. {category_total:,.2f}"
            )

    else:

        st.info(
            "No expenses available for filtering."
        )


# MONTHLY TOTAL

elif option == "Monthly Total":

    st.title("📅 Monthly Expense Total")

    month = st.date_input(
        "Select any date from the month",
        value=date.today()
    )

    selected_month = month.strftime("%Y-%m")

    total = manager.monthly_total(
        selected_month
    )

    st.metric(
        "Monthly Total",
        f"Rs. {total:,.2f}"
    )

    expenses = [
        expense
        for expense in manager.get_expenses()
        if expense["date"].startswith(selected_month)
    ]

    if expenses:

        st.subheader(
            f"Expenses for {month.strftime('%B %Y')}"
        )

        table_data = [
            {
                "ID": expense["id"],
                "Date": expense["date"],
                "Category": expense["category"],
                "Description": expense["description"],
                "Amount (Rs.)": expense["amount"]
            }
            for expense in expenses
        ]

        st.dataframe(
            table_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            f"No expenses found for "
            f"{month.strftime('%B %Y')}."
        )


# DELETE EXPENSE

elif option == "Delete Expense":

    st.title("🗑️ Delete Expense")

    expenses = manager.get_expenses()

    if expenses:

        expense_options = {
            f"ID {expense['id']} — "
            f"{expense['category']} — "
            f"{expense['description']} — "
            f"Rs. {expense['amount']:,.2f}":
            expense["id"]
            for expense in expenses
        }

        selected_expense = st.selectbox(
            "Select expense to delete",
            list(expense_options.keys())
        )

        expense_id = expense_options[
            selected_expense
        ]

        if st.button("🗑️ Delete Expense"):

            success, message = manager.delete_expense(
                expense_id
            )

            if success:

                st.success(message)

                
            else:

                st.error(message)

    else:

        st.info(
            "No expenses available to delete."
        )