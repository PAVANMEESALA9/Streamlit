import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Salary Details", page_icon="💰", layout="centered")

# Load the CSV file
@st.cache  # Add caching to improve app performance
def load_data():
    return pd.read_csv("Employeedate.csv")

df = load_data()

# Filter employees by name
employee_name = st.selectbox('Select Employee Name', ['All'] + sorted(df['EmpName'].unique()))

# Filter DataFrame based on selected employee name
filtered_df = df if employee_name == 'All' else df[df['EmpName'] == employee_name]

# Calculate the number of unique employees
num_employees = filtered_df['EmpName'].nunique()

# Display title and metric
st.title("Streamlit Example")
st.metric(label="No. of Employees", value=num_employees)

# Display the bar chart
st.bar_chart(filtered_df['Salary'].groupby(filtered_df['EmpName']).sum())

# Display the table
st.table(filtered_df)
