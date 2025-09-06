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
