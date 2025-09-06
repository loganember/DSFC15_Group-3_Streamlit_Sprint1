import os
import streamlit as st

data_dir = "data"
image_dir = "images"
plot_dir = "plots"

# Visualizations
st.title("Behind The Numbers")
st.divider()
st.subheader("1. Majority of transactions are small and happen during regular working hours")
g1 = os.path.join(plot_dir, "1.png")
st.image(g1)
with st.expander("See analysis"):
    st.write('''
        The largest segment (**47,524**) of transactions consists of **Low-Spend Regular Weekday**, followed by those that are **Low-Spend Regular Weekend** (**31,086**).

        High spend transactions make up a smaller portion of the data with only **1,133 High-Spend Regular Weekday** transactions and just **8 High-Spend Regular Weekend** transactions.
    ''')

