import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Salary Details", page_icon="💰", layout="wide")

# Load the CSV file
@st.cache  # Add caching to improve app performance
def load_data():
    return pd.read_csv("Employeedate.csv")

df = load_data()

num_employees = df['EmpName'].nunique()
num_citys=df['City'].nunique()

# Count employees by city
city_employee_counts = df.groupby('City').size()

st.title("Streamlit Example:")
st.divider()

left_column, middle_column =st.columns(2)
# Add metric
with left_column:
    st.metric(label="No. of Employees", value=num_employees)
with middle_column:   
    st.metric(label="No. of Cities",value=num_citys)
st.divider()

# Display charts and toggle switches side by side
col1, col2 = st.columns(2)

left_, Right_ =st.columns(2)

#Selection of Employee
st.sidebar.header("Filter Here:")
EmpName = st.sidebar.multiselect(
     "Select Employee:",
     options=df["EmpName"].unique(),
     default=df["EmpName"].unique()
)
df_selection= df.query("EmpName==@EmpName")

# Display charts and toggle switches
with left_:
    st.subheader("Employee Salary")
    chart_type_salary = st.radio("Select Chart Type", ["Bar Chart", "Line Chart"], key='chart_type_salary')
    if chart_type_salary == "Bar Chart":
        st.bar_chart(data=df_selection, x='EmpName', y='Salary')
    elif chart_type_salary == "Line Chart":
        st.line_chart(data=df_selection, x='EmpName', y='Salary')
with Right_:
    st.subheader("City Wise Employee Count")
    chart_type_employee_count = st.radio("Select Chart Type", ["Line Chart", "Bar Chart"], key='chart_type_employee_count')
    if chart_type_employee_count == "Line Chart":
        st.line_chart(city_employee_counts)
    elif chart_type_employee_count == "Bar Chart":
        st.bar_chart(city_employee_counts)
    

# Display the entire DataFrame
st.subheader("Employee Data")
st.table(df_selection)