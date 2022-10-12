import streamlit as st
import pickle
import numpy as np


def show_prediction_page():
    st.write("""## India Apartment & Home Rent Prediction""")

    st.write("""#### Calculate My Rent: """)

    def load_model():
        with open(r'OneDrive/Desktop/ADS505/model_labelencode.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    data = load_model()

    regressor = data['model']
    le_areatype = data['le_areatype']
    le_arealocality = data['le_arealocality']
    le_city = data['le_city']
    le_contact = data['le_contact']
    le_furnish = data['le_furnish']


    cities = (
        'Mumbai',
        'Chennai',
        'Bangalore',
        'Hyderabad',
        'Delhi',     
        'Kolkata',
        )

    areas = (
        'Super Area',
        'Carpet Area',    
        'Built Area',        
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
    furnishs = st.selectbox('Select If You will Furnish Yourself', furnish)

    size = st.slider('Select Preferred Size in Square Feet', min_value= 10, max_value = 10000)
    #floor = st.slider('Floor On', min_value = -2, max_value = 150)
    bathroom = st.slider('Select Preferred Bathroom Amount', min_value = 1, max_value = 10)

    ok = st.button('Calculate Rent')
    if ok:
        X = np.array([[bathroom, size, city, furnishs]])
        X[:, 2] = le_city.transform(X[:,2])
        X[:, 3] = le_furnish.transform(X[:,3])
        X = X.astype(float)

        rent = regressor.predict(X)
        st.write(f"#### The estimated rent is ₹{rent[0]:.2f}")