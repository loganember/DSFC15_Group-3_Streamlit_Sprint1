import streamlit as st
# Reco
st.title("What Should We Do Next?")

st.divider()

st.subheader("The Low-Spend Night transactions presents a potential untapped market")

with st.container(height="content", vertical_alignment="center"):
    st.write('''
          Upon initial analysis, the majority of transactions across Adobo Bank’s customer base was in the **low-spend category**. 

          However, Low-spend Night transactions represent only a small portion of that segment, **roughly 14% of all low-spend transactions**.
    ''')
    st.write('''
          **Recommendations**:
            1. Push limited-time evening offers
            2. Offer exclusive perks for night-time transactions
            3. Further segment and analyze the categories of transactions happening at night.
    ''')

st.subheader("Tailor strategies to retain VIPs, grow Regulars and Occasionals")

with st.container(height="content", vertical_alignment="center"):
    st.markdown('''
      | Transaction Time    | Category | Frequency | Total Amount |
      | -------- | ------- | -------- | ------- |
      | VIP    | LOW | HIGH | HIGH |
      | Regular    | LOW | MEDIUM | MEDIUM |
      | Occasional    | HIGH | LOW | MEDIUM |
      ''')
    st.markdown('''
          **Key Strategies**:
                1. VIPs: Focus on maintain engagement and retention
                        * Offer loyalty rewards like higher cashback or exclusive discounts
                        * Further analyze spending categories to personalize rewards

                2. Regulars: Encourage higher spend and/or transaction frequency
                        * Promote tools for payment convenience like tap-to-pay to encourage frequent card usage
                      
                3. Occasionals: Re-engage them and encourage more regular transactions
                        * Send personalized “We Miss You” offers or limited-time perks
                        * Personalized marketing: Use behavior and transaction category to suggest relevant products.
                        * Proactive outreach: Send helpful financial tips, alerts, or reminders before issues arise.
                        * Loyalty programs: Offer perks for long-term customers (e.g., reduced fees, special rates).
    ''')
