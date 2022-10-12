import streamlit as st
from prediction_page import show_prediction_page
from explore_page import show_explore_page

with open('c:/Users/whitm/OneDrive/Documents/GitHub/Rent_Prediction\style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    page = st.sidebar.selectbox("Predict Rent or Explore Options", ("Predict", "Explore"))

    if page == "Predict":
        show_prediction_page()
    else:
        show_explore_page()