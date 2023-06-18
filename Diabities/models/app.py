# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:42:44 2023

@author: Akshay Kumar Hiran
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/harshit computer/Desktop/Diabities/models/Trained_Diabities_model.pkl', 'rb'))

# Create a sidebar with a title and some text
with st.sidebar:
    st.title("Hello Patients!")
    st.write("Introducing Diabities Web Application")


option = st.sidebar.selectbox(
    'Select Your Language?',
    ( 'English','Hindi')
)
# creating a function for Prediction
def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if option=='English':
      if (prediction[0] == 0):
        st.success('The Person is not diabetic')
      else:
        st.warning('The Person is diabetic')
    if option =='Hindi':
      if (prediction[0] == 0):
        st.success('व्यक्ति मधुमेह ग्रस्त नहीं है')
      else:
        st.warning('व्यक्ति मधुमेह ग्रस्त है')
      

if option=='English':
  # giving a title
  st.title('Diabetes Prediction Web App')


  col1, col2 = st.columns(2)   
  # getting the input data from the user    
  Pregnancies = col1.text_input('Number of Pregnancies(0-18)')
  Glucose = col2.text_input('Glucose Level(0-200)')
  col3,col4 = st.columns(2)  
  BloodPressure = col3.text_input('Blood Pressure value(0-130)')
  SkinThickness = col4.text_input('Skin Thickness value(0-99)')
  col5,col6 = st.columns(2) 
  Insulin = col5.text_input('Insulin Level(0-846)')
  BMI = col6.text_input('BMI value(0-67)')
  col7,col8 = st.columns(2)
  DiabetesPedigreeFunction = col7.text_input('Diabetes Pedigree Function value(0.070-2.50)')
  Age = col8.text_input('Age of the Person(20-82)')


if option=='Hindi':
  # giving a title
  st.title('मधुमेह जाँच वेब ऐप')
  
  col1, col2 = st.columns(2)   
  # getting the input data from the user    
  Pregnancies = col1.text_input('गर्भधारण की संख्या (0-18)')
  Glucose = col2.text_input('ग्लूकोज स्तर (0-200)')
  col3,col4 = st.columns(2)  
  BloodPressure = col3.text_input('रक्तचाप मान (0-130)')
  SkinThickness = col4.text_input('त्वचा मोटाई मूल्य(0-99)')
  col5,col6 = st.columns(2) 
  Insulin = col5.text_input('इंसुलिन स्तर (0-846)')
  BMI = col6.text_input('बीएमआई मान (0-67)')
  col7,col8 = st.columns(2)
  DiabetesPedigreeFunction = col7.text_input('मधुमेह वंशावली मान (0.070-2.50)')
  Age = col8.text_input('व्यक्ति की आयु (1-100)')
     
# code for Prediction
diagnosis = ''

if st.button("Check Result"):
    diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

  
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  