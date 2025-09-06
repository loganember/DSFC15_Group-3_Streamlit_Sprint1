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

st.subheader("2. High, moderate and low engagements groups were identified based on spend and activity")
g2 = os.path.join(plot_dir, "2.png")
st.image(g2)
with st.expander("See analysis"):
  st.write('''
        The Adobo Bank RFM analysis was split into **80% training data and 20% test data** before applying **KMeans clustering** to help avoid data leakage. 

        This approach allowed us to group customers into the following segments:
        * **VIPs are highly active customers.** They transact frequently, in high amounts and have engaged recently.
        * **Regular** customers transact moderately and in fair amounts.
        * The **Occasional** segment engage less frequently, and haven’t transacted recently, but at least spend a moderate amount when they do.
  ''')

st.subheader("3. Flagged Accounts Show Month-on-Month and Average Declines in Transaction Category Breadth")
g3 = os.path.join(plot_dir, "3.png")
st.image(g3)
st.caption("X-axis = average velocity or mean month-to-month change in no. of active categories over the last n months")
st.caption("Y-axis = cumulative velocity (total growth/decline in categories over all months).")
with st.expander("See analysis"):
  st.write('''
        Quadrants:
        * **Top-right (positive avg, positive cum)**  Accounts steadily expanding into more categories.
        * **Top-left (negative avg, positive cum)**   Historically expanded, but recently slowing down.
        * **Bottom-right (positive avg, negative cum)** Historically contracted, but recently recovering.
        * :red[**Bottom-left (negative avg, negative cum)** Long-term and recent contraction 
          * Flagged Accounts]
        **Regression line** → Shows the average relationship: if slope is positive, accounts with negative averages tend also to have negative cumulative growth.

  ''')
