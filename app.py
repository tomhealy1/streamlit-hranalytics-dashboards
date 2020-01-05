import streamlit as st
import pandas as pd 
import numpy as np 
import os

st.title('Aero-Tech Industries Analytics Dashboard')
st.write("This dashboard will serve as a proof of concept for a dashboard")


DATA_URL = ('https://raw.githubusercontent.com/tomhealy1/Prog_DA_2019_Assignment_2/master/newdataset.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(750)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.write(data)

option = st.selectbox(
    'Which Department do you like best',
     data['Department'].unique())
'You selected: ', option

deps = st.multiselect('Show employee for Department?', data['Department'].unique())
gender = st.multiselect('Show Gender from the selected Departments?', data['Gender'].unique())
# Filter dataframe
new_df = data[(data['Department'].isin(deps)) & (data['Gender'].isin(gender))]
# write dataframe to screen
st.write(new_df)