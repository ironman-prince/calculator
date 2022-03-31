import streamlit as st
st.set_page_config(layout="wide")

st.title('EMI Calculator')

# Styling
st.markdown(""" <style> .big-font { font-size:25px !important; } </style> """, unsafe_allow_html=True)

def calculate_emi(p , n , r):

    cal1 = ( 1 + (r/100) ) ** n
    cal2 = cal1 - 1

    cal = cal1 / cal2

    emi = p * ( r / 100 ) * cal
    return  round( emi , 3 )

principal = st.slider('Select Principal Amount?', 1000, 1000000,1)

tenure = st.slider('Select Tenure?', 1, 30)

roi = st.slider('Select Rate of Interest?', 0.01, 15.00)

tenure_in_months = tenure * 12
monthly_roi = roi / 12

if st.button('CALCULATE EMI'):
    result = calculate_emi(principal , tenure_in_months , monthly_roi)
    st.write(f'<p class = "big-font"> Monthly Payment would be : {result} </p>' , unsafe_allow_html=True)
