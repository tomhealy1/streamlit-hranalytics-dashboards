#Import packages
import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
#import os
#Add titles etc
st.title('Aero-Tech Industries Analytics Dashboard')
st.header("This dashboard will use the contrived dataset from my college assignment, the file can be found here")
st.write('https://github.com/tomhealy1/Prog_DA_2019_Assignment_2/blob/master/newdataset.csv')
st.subheader("This is a small app deployed on heroku to see what streamlit can do, let's begin")



#Declare URL for app
DATA_URL = ('https://raw.githubusercontent.com/tomhealy1/Prog_DA_2019_Assignment_2/master/newdataset.csv')

#Define function for data
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

#This taken directly from the tutorial
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load rows of data into the dataframe.
data = load_data(750)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
st.subheader('View all data')
st.write(data)

#chart_data = pd.DataFrame(data, columns=['Gender', 'Department'])
#st._chart(chart_data)

st.subheader('Count plot for Gender')
sns.countplot(data['Gender'])
plt.title('Count plot of Gender')
st.pyplot()

st.subheader('Playing with selectbox')

option = st.selectbox(
    'Which Department do you like best(People Ops obvs :))',
     data['Department'].unique())
'You selected: ', option

st.subheader('Playing with multiselect')

deps = st.multiselect('Show employee for Department?', data['Department'].unique())
gender = st.multiselect('Show Gender from the selected Departments?', data['Gender'].unique())
# Filter dataframe
new_df = data[(data['Department'].isin(deps)) & (data['Gender'].isin(gender))]
# write dataframe to screen
st.write(new_df)

st.header('To be continued')

