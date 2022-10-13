from re import X
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def clean_flooron(x):
    if 'Gr' in str(x[:2]):
        return 0
    if 'Up' in str(x[:2]):
        return -1
    if 'Lo' in str(x[:2]):
        return -2
    else:
        return str(x[:2])

def clean_floortot(x):
    if 'nd' in str(x[-2:]):
        return 0
    else:
        return str(x[-2:])


@st.cache
def load_data():
    rent = pd.read_csv(r'C:\Users\whitm\OneDrive\Documents\GitHub\Rent_Prediction/House_Rent_Dataset.csv')

    rent['floor on'] = rent['Floor'].apply(clean_flooron)
    rent['floor total'] = rent['Floor'].apply(clean_floortot)

    rent['Posted On'] = pd.to_datetime(rent['Posted On'])
    rent['month'] = rent['Posted On'].dt.month
    rent['year'] = rent['Posted On'].dt.year
    rent['DOW'] = rent['Posted On'].dt.dayofweek

    rent[['floor on', 'floor total']] = rent[['floor on', 'floor total']].astype(int)

    rent = rent[['Bathroom','Size','City','Furnishing Status','Rent','Posted On','Point of Contact','BHK']]

    return rent

df = load_data()


def show_explore_page():
    st.write("## Explore Rent Prices in India")

    st.write(
        """
    #### MagicBricks India Household Rent Dataset (2022)
    """
    )
    data = df.groupby(['City'])['Rent'].mean().round(2).sort_values(ascending=True)
    data2 = df.groupby(['Point of Contact'])['Rent'].mean().round(2).sort_values(ascending=True)
    data3 = df.groupby(['Posted On'])['Rent'].mean().round(2).sort_values(ascending=True)
    data4 = df.groupby(['Bathroom'])['Rent'].mean().round(2).sort_values(ascending=True)
    data5 = df.groupby(['BHK'])['Rent'].mean().round(2).sort_values(ascending=True)

    st.write("""#### Average Cost of Rent by City""")
    st.bar_chart(data)

    st.write("""#### Average Cost of Rent by Point of Contact""")
    st.bar_chart(data2)

    st.write("""#### Average Cost of Rent by Bathroom Count""")
    st.bar_chart(data4)

    st.write("""#### Average Cost of Rent by Bedroom + Kitchen + Hall Count""")
    st.bar_chart(data5)

    st.write("""#### Listings By Date in 2022""")
    st.line_chart(data3)