import streamlit as st

# Set page title
st.set_page_config(page_title="DSFC15 Group 3 - Sprint1 Streamlit", layout="wide")

# Sidebar Navigation
pages = {
    "Navigation": [
      st.Page("home.py", title="Home"),
      st.Page("game_plan.py", title="Our Game Plan"),
      st.Page("dataset.py", title="Introduction to The Dataset"),
      st.Page("visual.py", title="Behind The Numbers"),
      st.Page("reco.py", title="What Now?"),
      st.Page("appen.py", title="Appendices"),
    ]
}

pg = st.navigation(pages)
pg.run()

# menu = st.selectbox(
#     "Navigate Here",
#     ("Home", "Our Game Plan", "Introduction to The Dataset", "Behind The Numbers", "What Now?", "Appendices"),
# )

# Data miming Logo in the sidebar 
big_logo = "images/data_miming.png"
small_logo = "images/data_miming_s.png"

st.logo(big_logo, icon_image=small_logo)
st.sidebar.markdown("Group :3")

# Home
st.title("From Clusters to Clarity: Predicting Churn with K-Means")
st.subheader("Uncovering hidden patterns in churn behavior")

# Ensure directories exist
data_dir = "data"
image_dir = "images"
plot_dir = "plots"

os.makedirs(data_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(plot_dir, exist_ok=True)
