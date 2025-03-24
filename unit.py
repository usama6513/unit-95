import streamlit as st
 
st.title("🚀 Universal Unit Convertor")
st.markdown("✨ Conversion of different Physical Quantities into thier Units ")
 
st.write("💫 Select a category, enter a value, and get the converted result.")
 
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])
 
def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
             return value * 0.621371
        elif unit == "Miles to Kilometers":
             return value / 0.621371
 
        elif category == "Weight":
         if unit == "Kilograms to Pounds":
             return value * 2.20462
         elif unit == "Pounds to Kilograms":
             return value / 2.20462
  
        elif category == "Time":
         if unit == "Seconds to Minutes":
             return value / 60
         elif unit == "Minutes to Seconds":
             return value * 60
         elif unit == "Hours to Minutes":
             return value * 60
         elif unit == "Minutes to Hours":
             return value / 60
         elif unit == "Hours to Days":
             return value / 24
         elif unit == "Days to Hours":
             return value * 24
if category == "Length":
     unit = st.selectbox("Select conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
     unit = st.selectbox("Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
     unit = st.selectbox("Select conversion", [
         "Seconds to Minutes", "Minutes to Seconds",
         "Minutes to Hours", "Hours to Minutes",
         "Hours to Days", "Days to Hours"
     ])
 
value = st.number_input("Enter the value to convert", min_value=0.0)
  
if st.button("🤖 Convert"):
     result = convert_unit(category, value, unit)
     if result is not None:
         st.success(f"The result is {result:.2f}")
     else:
         st.error("Invalid conversion. Please check your input.")
         st.markdown("<div class='footer'>Created with 💖 by Usama Sharif </div>",unsafe_allow_html=True)