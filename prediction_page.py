import streamlit as st
import pickle
import numpy as np


def show_prediction_page():
    st.write("""## India Apartment & Home Rent Prediction""")

    st.write("""#### Calculate My Rent: """)

    def load_model():
        with open(r'OneDrive/Documents/Github/Rent_Prediction/model_labelencode.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    data = load_model()

    regressor = data['model']
    le_city = data['le_city']
    le_contact = data['le_contact']



    cities = (
        'Mumbai',
        'Chennai',
        'Bangalore',
        'Hyderabad',
        'Delhi',     
        'Kolkata',
        )


    contact = (
        'Contact Owner',
        'Contact Agent',
        'Contact Builder',
    )

    furnish = (
        'Semi-Furnished', 
        'Unfurnished', 
        'Furnished', 
    )
    with open('c:/Users/whitm/OneDrive/Documents/GitHub/Rent_Prediction\style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    city = st.selectbox('Select Your Preferred City', cities)
    contacts = st.selectbox('Select How to Contact Landlord', contact)

    size = st.slider('Select Preferred Size in Square Feet', min_value= 10, max_value = 10000)
    bhk = st.slider('Select Preferred Bedroom / Hall / Kitchen Amount')
    bathroom = st.slider('Select Preferred Bathroom Amount', min_value = 1, max_value = 10)
    floor = st.slider('Select Prefered Building Floor Total', min_value = -2, max_value = 150)
   

    ok = st.button('Calculate Rent')
    if ok:
        X = np.array([[size, city, bathroom, floor, contacts, bhk]])
        X[:, 1] = le_city.transform(X[:, 1])
        X[:, 4] = le_contact.transform(X[:, 4])
        X = X.astype(float)

        rent = regressor.predict(X)
        st.write(f"#### The estimated rent is ₹{rent[0]:.2f}")