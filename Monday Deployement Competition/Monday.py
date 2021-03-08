import streamlit as st
import pickle
import numpy as np
import pandas as pd

classify=pickle.load(open('RBF.pkl','rb'))
st.markdown("<h1 style='text-align: center; color: red;'>Project deployement </h1>", unsafe_allow_html=True)
st.title("Competetion on Deployment on heroku server")

col1, col2 = st.beta_columns(2)


#'PetalLengthCm', 'PetalWidthCm',
#       'Species'
SepalLengthCm = col1.number_input("Please Enter col1 number ")

SepalWidthCm = col2.number_input("Please Enter col2 number ")


click = st.button('SUBMIT')
if click:
	df=pd.DataFrame([[SepalLengthCm, SepalWidthCm]])
	df=df.astype('float')
	c=classify.predict(df)
	if np.array(c)[0]==0:
		st.markdown("<h2 style='text-align: center; color: red;'>Your Predicted Value is</h2>", unsafe_allow_html=True)
		st.markdown("<h1 style='text-align: center; color: green;'>0</h1>", unsafe_allow_html=True)
	elif np.array(c)[0]==1:
		st.markdown("<h2 style='text-align: center; color: red;'>Your Predicted Value is</h2>", unsafe_allow_html=True)
		st.markdown("<h1 style='text-align: center; color: green;'>1</h1>", unsafe_allow_html=True)
	else:
		st.markdown("<h1 style='text-align: center; color: red;'>Error in Entering </h1>", unsafe_allow_html=True)
