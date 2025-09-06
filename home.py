import streamlit as st
# Home
st.title("From Clusters to Clarity: Predicting Churn with K-Means")
st.subheader("Uncovering hidden patterns in churn behavior")

st.write("Presented by Group 3: Data Miming")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("Why Does Churn Matter?")

with col2:
    st.markdown("*As of 2025, leading banks in the Philippines reported strong **double-digit growth in credit card receivables**, driven by rising consumer spending.")
    left, right = st.columns(2)
    left.button("+48% growth in 2024*", width="stretch")
    right.button("+18.2% growth in H1 2025**", width="stretch")
