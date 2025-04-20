import streamlit as st

st.title("Unit Converter App")

st.markdown(" ### convert length, weight, time instantly")

st.write("Wellcome | Select, Catogery")

catogery = st.selectbox(" Choose Catogery", ["Length", "Weight", "Time"])

def unit_converter(catogery, value, unit):
    if catogery == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        
    
    elif catogery == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.04623
        elif unit == "pounds to kilograms":
            return value / 2.04623
        
    elif catogery == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == " minutes to seconds":
            return value * 60
        if unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        if unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
        
        return 0
    
if catogery == "Length":
    unit = st.selectbox("Select Unit ", ["kilometers to miles", "miles to kilometers"])
elif catogery == "Weight":
    unit = st.selectbox("Select Unit ", ["kilogram to pounds", "pounds to kilograms"])
elif catogery == "Time":
    unit = st.selectbox("Select Unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])
        
value = st.number_input("Enter Your Value to Convert")

if st.button("Convert"):
    result = unit_converter(catogery, value, unit)
    st.success(f" Your Final Result is {result} ")