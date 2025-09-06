import streamlit as st
import pandas as pd
import os

data_dir = "data"
image_dir = "images"
plot_dir = "plots"


# Dataset
st.title("Adobo Bank Dataset")

df = pd.read_csv('data/cc_clean.csv')
st.dataframe(df)

st.markdown('''
            ###### The model was driven by four main variables, i.e. ```dob```, ```acct_num```, ```amt``` and ```trans_datetime```.
''')


st.divider()

