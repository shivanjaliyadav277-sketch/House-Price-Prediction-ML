import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠House Price prediction using ML')
st.image('https://cdn.dribbble.com/userupload/42021677/file/original-454f1d86c864ae65b5ab6e292a3e5a11.gif')

df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('Select House feature')
st.image('https://cdn.dribbble.com/userupload/42021677/file/original-454f1d86c864ae65b5ab6e292a3e5a11.gif')
all_value = []
for i in y:
  ans = st.sidebar.slider(f'Select {i} value')
  all_value.append(ans)

st.write(all_value)








