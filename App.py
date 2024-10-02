import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIPML.pkl', 'rb'))

st.header('HEALTH INSURANCE PRICE  CHANGES PREDICTOR MODEL')

gender = st.selectbox('Choose Gender',['Female','Male'])
smoker = st.selectbox('Are you a smoker ?',['Yes','No'])
region =  st.selectbox('Choose Region', ['SouthEast', 'SouthWest','NorthEast','NorthWest'])

age = st.slider('Enter Age', 5 , 100)
bmi = st.slider('Enter BMI', 5 , 100)
children = st.slider('Choose Number of Children',0, 10 )

if gender == 'Female':
    gender = 0
else:
    gender = 1

if smoker == 'No':
    smoker = 0
else:
    smoker = 1

if region == 'SouthEast':
    region = 0
if region == 'SouthWest':
    region = 1
if region == 'NorthEast':
    region = 2
else:
    region = 3

input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
if st.button('predict'):
    predicted_prem = model.predict(input_data)
    display_string ='Insurance Price:' +' '+ str(round(predicted_prem[0], 2)) +' '+ 'Rwf'
    st.markdown(display_string)