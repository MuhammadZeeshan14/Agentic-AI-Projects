import streamlit as st
import pandas as pd

st.title('BMI Calculator')

height = st.slider('Enter your height (in cm)', 100, 250, 175)
weight = st.slider('Enter your weight (in kg)', 40, 200, 70)

bmi=weight/((height/100)**2)

st.write('Your BMI is:', round(bmi, 2))
