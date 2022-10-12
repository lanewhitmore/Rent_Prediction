import streamlit as st
from prediction_page import show_prediction_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Predict Rent or Explore Options", ("Predict", "Explore"))

if page == "Predict":
    show_prediction_page()
else:
    show_explore_page()
