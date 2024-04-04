import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(page_title="Employee Salary Details",page_icon="💰",layout="centered")

# Load the CSV file
df = pd.read_csv("C:\\Users\\ZuraAdmn\\Downloads\\Employeedate.csv")
num_employees = df['EmpName'].nunique()

st.title("Streamlit Example")

# Add metric
st.metric(label="No. of Employees", value=num_employees)


# df_selection = df.query("Employee == @Empname")
# st.dataframe(df_selection)

#Dynamic filters
dynamic_filters = DynamicFilters(df, filters=['EmpName'])
dynamic_filters.display_filters()
dynamic_filters.display_df()
dynamic_filters.display_df

# Display the bar chart
st.bar_chart(data=df, x='EmpName', y='Salary')
st.table(data=df)





