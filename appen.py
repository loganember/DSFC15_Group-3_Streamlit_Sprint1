import streamlit as st
import os

data_dir = "data"
image_dir = "images"
plot_dir = "plots"

# Appendix
st.title("Appendices")
st.divider()
st.subheader("Classification of Customers Based on Their Transactions")
g14 = os.path.join(plot_dir, "14.png")
st.image(g14)
st.caption("Entertainment Enthusiast = ['shopping_net', 'entertainment', 'travel', 'shopping_pos']")
st.caption("Essential Spenders = ['home', 'gas_transport', 'personal_care', 'grocery_pos', 'health_fitness', 'grocery_net', 'kids_pets']")
st.caption("Food Lovers = ['food_dining']")
st.caption("Others = ['misc_net', 'misc_pos', 'others']")
with st.expander("See analysis"):
  st.markdown('''
        **Insights by Category:**

            1. **Essential Spenders**:
              - The largest group as 84% of customers classify under this segment which indicates that most customers are spending primarily on necessities like groceries, health, and personal care.
            
            2. **Entertainment Enthusiasts**:
              - These customers focus more on entertainment-related spending. The transactions made may be infrequent, potentially driven by seasonal trends or occasional spending behavior.
            
            3. **Others**:
              - Represents uncategorized or miscellaneous spending, not fitting in any specific group.
            
            4. **Food Lovers**:
              - Zero transactions, which may simply indicate that customers tend to use their credit cards more for other categories rather than food and dining.

  ''')

g15 = os.path.join(plot_dir, "15.png")
st.image(g15)
with st.expander("See analysis"):
  st.markdown('''
        - The distribution is slightly **right-skewed**, as the upper whisker is longer.
        - The majority of customers who spend on food and dining made **between 40 and 145 transactions**, indicating that a typical customer made about an average of **95 transactions**.
        - Compared to the other dominant classifications for each customer, transactions related to food and dining can be considered **moderate** in volume.
  ''')

g16 = os.path.join(plot_dir, "16.png")
st.image(g16)
with st.expander("See analysis"):
  st.markdown('''
        Entertainment Enthusiasts as a group show:
          - **Low transaction frequency**
          - **High recency**, meaning most haven’t interacted in a while
        This could suggest:
          - They are **seasonal users**
          - Their spending patterns are **occasional** or **event-driven**
          - A need for **engagement strategies** to bring them back (e.g., personalized offers, entertainment deals, reactivation campaigns)
  ''')
