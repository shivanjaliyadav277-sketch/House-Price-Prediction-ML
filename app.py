import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠House Price prediction using ML')

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq-35QBawdcQKkchXYV-qPFZ3ei7y6TOoYTJk-H_06hf9MUyRkQOHBz4lbuQ&s')
df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]
st.sidebar.title('Select House feature')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq-35QBawdcQKkchXYV-qPFZ3ei7y6TOoYTJk-H_06hf9MUyRkQOHBz4lbuQ&s')
all_value = []
for i in X:
  min_value = int(X[i].min())
  max_value = int(X[i].max())
  ans = st.sidebar.slider(f'Select {i} value',min_value,max_value)
  all_value.append(ans)
st.write(all_value)









