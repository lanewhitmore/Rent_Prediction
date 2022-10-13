import streamlit as st
from explore_page import show_explore_page
from prediction_page import show_prediction_page

## Open both pages with css style
#with open('style.css') as f:
    #st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

page = st.sidebar.selectbox("Predict Rent or Explore Options", ("Predict", "Explore"))

if page == "Predict":
    show_prediction_page()
else:
    show_explore_page()
