import streamlit as st
import os

data_dir = "data"
image_dir = "images"
plot_dir = "plots"



# Game Plan
st.title("The Game Plan")
col1, col2 = st.columns(2)
with col1:
  with st.container(height=300, vertical_alignment="center"):
    st.markdown('''
      The analysis focused on the following key factors:
        * How often Adobo Bank use their credit card/s
        * How recently they used it
        * How much they spend on it
      The following methods (on the right) were used to determine which customers are at a higher risk of churn.

      ''')

with col2:
    with st.container(height=110, vertical_alignment="center"):
      st.markdown('''
      ##### Customer Churn Prediction
      This method is best for binary classification, i.e. churn or not churn. It is also able to output probabilities, for eg. Customer A has a 85% chance of churn.
      ''')
    with st.container(height=170, vertical_alignment="center"):
      st.markdown('''
      ##### K-Means Clustering (Machine Learning)
      After we have determined the similar usage pattern of each customer in terms of recency and frequency, they can be clustered into whether or not they will stop using their credit card. This solution can also help distinguish the temporal and behavioral patterns for the customers.
      ''')

# put divider
st.divider()

col3, col4 = st.columns(2)
with col3:
  with st.container(height=300, vertical_alignment="center"):
    st.markdown('''
      ### The following behavioral patterns (temporal behavior) were also taken into account during analysis.
      ''')

with col3:
    with st.container(height="content", vertical_alignment="center"):
      st.markdown('''
      | Transaction Time    | Category |
      | -------- | ------- |
      | Early Birds  | 6 AM to 9 AM    |
      | Night Owls | 10 PM to 2 AM     |
      | Regular    | Rest of the day    |
      ''')

with col4:
    with st.container(height="content", vertical_alignment="center"):
      st.markdown('''
      | Transaction Day    | Category |
      | -------- | ------- |
      | Weekday Spender  | Monday to Friday    |
      | Weekend Spender | Saturday to Sunday     |
      ''')
