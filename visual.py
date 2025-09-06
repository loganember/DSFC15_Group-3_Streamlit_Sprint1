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
        * **Bottom-left (negative avg, negative cum)** Long-term and recent contraction 
          * Flagged Accounts
        
        **Regression line** → Shows the average relationship: if slope is positive, accounts with negative averages tend also to have negative cumulative growth.

  ''')

st.subheader("4. Visualizing streaks of months with decline in category breadth ")
g4 = os.path.join(plot_dir, "4.png")
st.image(g4)

st.subheader("5. Historical Benchmarking: Flagged Accounts show consistent 3-Month and 6-Month Accelerated Decline in Spending Volume")
g5 = os.path.join(plot_dir, "5.png")
st.image(g5)
with st.expander("See analysis"):
  st.write('''
        **Blue Line – Monthly Spend**: Customer’s actual spending each month.
        **Orange Line – 3-Month Avg**: Smooths short-term changes to show recent spending trends.
        **Red Line – 6-Month Avg**: Longer-term baseline to separate temporary dips from true declines.
        **Red Dots – Churn Risk Flags**:
            Triggered when:
              1. 3-Month Avg is falling
              2. 6-Month Avg is falling
              3. Monthly spend keeps dropping (negative velocity)

        → **Indicates churn risk, noting consistent, accelerating decline in spending**

  ''')

st.subheader("6. Peer benchmarking: Creating a category churn threshold by geographic cohort")

col6, col7 = st.columns(2)

with col6:
    g6 = os.path.join(plot_dir, "6.png")
    st.image(g6)

with col7:
    g7 = os.path.join(plot_dir, "7.png")
    st.image(g7)

with st.container(height="content", vertical_alignment="center"):
  with st.expander("See analysis"):
    st.write('''
          **Urban Customers are Big-Basket Shoppers.** Their average transaction size is high, but their overall monthly total is lower.
          **Rural Customers are Small-Basket, Frequent Shoppers.** Their average transaction size is very low, but because they make so many purchases, their overall monthly total is much, much higher.

    ''')

st.subheader("7. Peer benchmarking: Creating a category churn threshold by geographic cohort ")

col8, col9 = st.columns(2)

with col8:
    g8 = os.path.join(plot_dir, "8.png")
    st.image(g8)

with col9:
    g9 = os.path.join(plot_dir, "9.png")
    st.image(g9)


st.subheader("8. Flagged Accounts show under transaction vs. segment-specific category norms, adjusted for region")
g10 = os.path.join(plot_dir, "10.png")
st.image(g10)
with st.expander("See analysis"):
  st.write('''
        * **Flagged accounts below average median of bottom 25% for risk of churn**
        * **Risk**: We've identified Rural accounts at high risk of churn  
        * **Opportunity**: Conversely, our Urban customer base shows strong resilience and consistent engagement in key lifestyle categories like fitness, travel, and shopping. 

        
        Recommendation: Two-pronged strategy: targeted re-engagement campaigns for the at-risk Rural segment and up-sell/loyalty initiatives for the stable Urban core.
  ''')

st.subheader("9. Silent Generation is infrequent but high-spend, Baby Boomers are frequent by low-spend and Gen X is balanced ")

col11, col12, col13 = st.columns(3)

with col11:
    g11 = os.path.join(plot_dir, "11.png")
    st.image(g11)

with col12:
    g12 = os.path.join(plot_dir, "12.png")
    st.image(g12)

with col13:
    g13 = os.path.join(plot_dir, "13.png")
    st.image(g13)

with st.container(height="content", vertical_alignment="center"):
  with st.expander("See analysis"):
    st.write('''
          * **Baby Boomers** transact the most often (1,073) but in small amounts ($162).
          * **Generation X** hasn’t transacted recently (102 days) but exhibit balanced spending behavior, i.e. they transact fairly frequently (924) and in fair amounts ($219).
          * **Silent Generation** engage the most recently (58 days), don’t transact often (766) but when they do, they spend big ($263).
    ''')
