import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Salary Details", page_icon="💰", layout="centered")

# Load the CSV file
@st.cache  # Add caching to improve app performance
def load_data():
    return pd.read_csv("Employeedate.csv")

df = load_data()

# Calculate the number of unique employees
num_employees = df['EmpName'].nunique()

# Display title and metric
st.title("Streamlit Example")
st.metric(label="No. of Employees", value=num_employees)

# Display the bar chart
st.bar_chart(df['Salary'].groupby(df['EmpName']).sum())

# Display the table
st.table(df)
