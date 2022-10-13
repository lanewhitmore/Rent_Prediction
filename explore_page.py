import streamlit as st
import pandas as pd
import altair as alt

## formulas from nb
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

### caching preprocessing 
@st.cache
def load_data():
    rent = pd.read_csv(r'House_Rent_Dataset.csv')

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

### Showing consumers valuable charts
def show_explore_page():
    st.write("## Explore Rent Prices in India")

    st.write(
        """
    #### MagicBricks India Household Rent Dataset (2022)
    """
    )
    data = df.groupby(['City'])['City','Rent'].mean().round(2)
    data2 = df.groupby(['Point of Contact'])['Point of Contact','Rent'].mean().round(2)
    data3 = df.groupby(['Posted On'])['Rent'].mean().round(2).sort_value(ascending = True)
    data4 = df.groupby(['Bathroom'])['Bathroom','Rent'].mean().round(2)
    data5 = df.groupby(['BHK'])['BHK','Rent'].mean().round(2)

    st.write("""#### Average Cost of Rent by City""")
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            alt.X('City'),
            alt.Y("Rent"),
            alt.Color('City', scale=alt.Scale(scheme='dark2')),
            alt.Tooltip(["City", "Rent"]),
        )
        .interactive()
    )

    st.write("""#### Average Cost of Rent by Point of Contact""")
    chart = (
        alt.Chart(data2)
        .mark_bar()
        .encode(
            alt.X('Point of Contact'),
            alt.Y("Rent"),
            alt.Color('Point of Contact', scale=alt.Scale(scheme='dark2')),
            alt.Tooltip(["Point of Contact", "Rent"]),
        )
        .interactive()
    )

    st.write("""#### Average Cost of Rent by Bathroom Count""")
    chart = (
        alt.Chart(data4)
        .mark_bar()
        .encode(
            alt.X('Bathroom'),
            alt.Y("Rent"),
            alt.Color('Bathroom', scale=alt.Scale(scheme='dark2')),
            alt.Tooltip(["Bathroom", "Rent"]),
        )
        .interactive()
    )

    st.write("""#### Average Cost of Rent by Bedroom + Kitchen + Hall Count""")
    chart = (
        alt.Chart(data5)
        .mark_bar()
        .encode(
            alt.X("BHK"),
            alt.Y("Rent"),
            alt.Color("BHK", scale=alt.Scale(scheme='dark2')),
            alt.Tooltip(["BHK", "Rent"]),
        )
        .interactive()
    )
    st.altair_chart(chart)

    st.write("""#### Listings By Date in 2022""")
    st.line_chart(data3)