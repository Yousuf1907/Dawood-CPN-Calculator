import streamlit as st
import pandas as pd

st.title("CPN Calculator")
# st.navigation([st.Page("2_📖_Instructions.py"), st.Page("3_About Me.py")])

Matric_marks = st.number_input("Please enter your Matric(X) Percentage: ")
Inter_Marks = st.number_input("Please enter your Intermediate (XII) Percentage: ")
Field = st.selectbox("In which field you want to take admission?", ["BS CS", "BS AI", "BS Cyber", "BE Architecture", "BE CSE", "BE Electronics", "BE Energy & Environment", "BE Industrial", "BE Metallurgy Material", "BE Petroleum", "BE Telecom", "BE Chemical"])

required_cpn = {
    'BS CS': 64,
    'BS AI': 60,
    'BS Cyber': 57,
    'BE Architecture': 54,
    'BE CSE': 63,
    'BE Electronics': 55,
    'BE Energy & Environment': 51,
    'BE Industrial': 53,
    'BE Metallurgy Material': 50.32,
    'BE Petroleum': 50.41,
    'BE Telecom': 51,
    'BE Chemical': 52
}

if Field:
    cpn_required = required_cpn[Field]
    bla = (Matric_marks * 0.1) + (Inter_Marks * 0.3)
    needed_marks = round((cpn_required - bla) * (5 / 3), 2)
    if Field == "BS CS" or Field == "BE CSE": 
        st.write(f"For Minimum chance at seat: {needed_marks}")
    
    if Field == "BS CS" or Field == "BE CSE":
        st.write(f"Best Chance to secure the Seat: {needed_marks + 15} + ")
    elif Field == "BS AI" or Field == "BS Cyber":
        st.write(f"Best Chance to secure the Seat: {needed_marks + 20} +")
    elif Field != "BS CS" and Field != "BS Cyber" and Field != "BS AI":
        st.write(f"Best Chance to secure the Seat: {needed_marks + 25} +")
    
    
    # st.write(f"Minimum required Test Score: {needed_marks}")
        