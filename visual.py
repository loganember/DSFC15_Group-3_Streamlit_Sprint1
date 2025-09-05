import os
import streamlit as st
# Visualizations
st.title("Behind The Numbers")
st.divider()

# Display an image from images folder
overall_img_path = os.path.join(image_dir, "data_miming.png")
if os.path.exists(overall_img_path):
    st.image(overall_img_path, caption="test", use_column_width=True)
else:
    st.warning("No overview image found. Please add an image to `images/` directory.")
