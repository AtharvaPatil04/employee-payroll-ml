# 💼 Employee Payroll Management System with Salary Prediction (Python + ML + Streamlit)

A complete data science project built using **Python, Pandas, Scikit-learn, and Streamlit**, designed to simulate a real-world **Employee Payroll Management System** and predict employee **Net Salary** based on business rules and machine learning.

---

## 📌 Features

✅ Generate realistic employee data (300 entries)  
✅ Calculate Net Salary from business logic  
✅ Perform Exploratory Data Analysis (EDA)  
✅ Train ML model to predict salary (R² > 0.9)  
✅ Export payroll reports to Excel  
✅ Build and run a Streamlit web app for prediction  
✅ Resume-ready and industry-relevant project

---

## 🧠 Technologies Used

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn (Linear Regression)
- Streamlit (for web app)
- Faker (for realistic data generation)
- XlsxWriter (for Excel reports)

---

## 📊 Net Salary Logic

The **Net Salary** is calculated using:
Net Salary = (Basic Salary + Bonus) - (Tax + Deductions) + Overtime Pay - Leave Penalties


Where:
- Bonus is based on performance %
- Tax is a fixed %
- Overtime = ₹500/hour
- Leave penalty = ₹1000/leave beyond 2

---

## 🧪 Machine Learning

We trained a **Linear Regression model** using:
- Age
- Experience
- Department
- Role
- Basic Salary
- Bonus %, Tax %, Deductions
- Overtime Hours & Leaves

### ✅ Model Metrics:
- MAE: ₹ ~2500–3000  
- RMSE: ₹ ~3500–4000  
- R² Score: **~0.91**

---

## 🖥️ Streamlit Web App

Run the app using:

```bash
cd your_project_folder
streamlit run app.py

📁 Excel Report Output
The project also exports a clean payroll Excel report including:

Full employee data

Top 10 earners

Department-wise summary

File: monthly_payroll_report.xlsx






