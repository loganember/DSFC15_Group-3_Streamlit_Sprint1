import streamlit as st
import os

data_dir = "data"
image_dir = "images"
plot_dir = "plots"

# Home
st.title("From Clusters to Clarity: Predicting Churn with K-Means")
st.subheader("Uncovering hidden patterns in churn behavior")

st.write("Presented by Group 3: Data Miming")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("Why Does Churn Matter?")
    churn = os.path.join(image_dir, "customer-churn.jpg")
    st.image(churn)

with col2:
    with st.container(height=400, vertical_alignment="center"):
      st.markdown("##### *As of 2025, leading banks in the Philippines reported strong **double-digit growth in credit card receivables**, driven by rising consumer spending.")
      left, right = st.columns(2, vertical_alignment="center")
      left.button("+48% growth in 2024*", width="stretch")
      left.caption("RCBC")
      right.button("+18.2% growth in H1 2025**", width="stretch")
      right.caption("Metrobank")
      st.markdown("##### However, growth is only half the story. In this competitive market, **even small amounts of churn can quietly cut into profits.**")

st.divider()
