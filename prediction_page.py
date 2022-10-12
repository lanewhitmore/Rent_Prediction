import streamlit as st
import pickle
import numpy as np


def show_prediction_page():
    st.title('India Apartment & Home Rent Prediction')

    st.write("""### Plug in information to predict Rent""")

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

    city = st.selectbox('City', cities)
    furnishs = st.selectbox('Furnishings', furnish)

    size = st.slider('Square Feet', min_value= 10, max_value = 10000)
    #floor = st.slider('Floor On', min_value = -2, max_value = 150)
    bathroom = st.slider('Bathrooms', min_value = 1, max_value = 10)

    ok = st.button('Calculate Rent')
    if ok:
        X = np.array([[bathroom, size, city, furnishs]])
        X[:, 2] = le_city.transform(X[:,2])
        X[:, 3] = le_furnish.transform(X[:,3])
        X = X.astype(float)

        rent = regressor.predict(X)
        st.subheader(f"The estimated rent is ₹{rent[0]:.2f}")