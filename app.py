import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load('../model/salary_predictor.pkl')
encoders = joblib.load('../model/encoders.pkl')

st.title("💼 Employee Net Salary Predictor")

# Input fields
age = st.number_input("Age", 20, 65, 30)
experience = st.number_input("Experience (Years)", 0, 40, 5)
department = st.selectbox("Department", encoders['Department'].classes_)
role = st.selectbox("Role", encoders['Role'].classes_)
basic_salary = st.number_input("Basic Salary (₹)", 20000, 200000, 80000)
bonus = st.slider("Bonus %", 0, 50, 10)
tax = st.slider("Tax %", 0, 50, 15)
deductions = st.number_input("Deductions (₹)", 0, 20000, 2000)
ot_hours = st.slider("Overtime Hours", 0, 100, 5)
leaves = st.slider("Leaves Taken", 0, 30, 2)

# Predict
if st.button("Predict Net Salary"):
    input_data = pd.DataFrame([{
        'Age': age,
        'ExperienceYears': experience,
        'Department': encoders['Department'].transform([department])[0],
        'Role': encoders['Role'].transform([role])[0],
        'BasicSalary': basic_salary,
        'BonusPercent': bonus,
        'TaxPercent': tax,
        'Deductions': deductions,
        'OvertimeHours': ot_hours,
        'LeavesTaken': leaves
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Net Salary: ₹{prediction:,.2f}")
