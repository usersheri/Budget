import streamlit as st
from database import DatabaseManager
from expense import Expense
import pandas as pd

db = DatabaseManager()

st.set_page_config(page_title="Expense & Budget Manager", page_icon="💰")

st.title(" Expense & Budget Manager")

menu = ["Add Expense", "View Expenses", "Category Summary"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Expense":
    st.subheader(" Add New Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Bills", "Entertainment", "Others"])
    description = st.text_input("Description")
    amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)

    if st.button("Save Expense"):
        exp = Expense(date, category, description, amount)
        db.insert_expense(exp.date, exp.category, exp.description, exp.amount)
        st.success(f" Expense added for {category} - ₹{amount}")

elif choice == "View Expenses":
    st.subheader(" All Expenses")
    data = db.fetch_all_expenses()
    df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Description", "Amount"])
    st.dataframe(df)

    if not df.empty:
        id_to_delete = st.number_input("Enter Expense ID to Delete", min_value=1, step=1)
        if st.button("Delete Expense"):
            db.delete_expense(id_to_delete)
            st.success(" Expense deleted successfully")

elif choice == "Category Summary":
    st.subheader(" Expense Summary by Category")
    summary = db.total_by_category()
    if summary:
        sum_df = pd.DataFrame(summary, columns=["Category", "Total (₹)"])
        st.bar_chart(sum_df.set_index("Category"))
        st.table(sum_df)
    else:
        st.info("No expenses added yet!")
