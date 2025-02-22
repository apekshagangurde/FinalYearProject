import pandas as pd
import pydeck as pdk
import streamlit as st

def load_places_data():
    # Define the data with accurate names and coordinates
    places = {
        'Place': [
            'Sadhana Restaurant', 
            'Panchavati Gaurav Thali', 
            'Barbeque Nation', 
            'The Gateway Hotel Ambad',
            'IBIS Nashik Hotel',
            'Express Inn Nashik',
            'Hotel Yahoo Restaurant',
            'Ginger Hotel Nashik',
            'Hotel Rama Heritage',
            'Kokni Darbar'
        ],
        'Latitude': [
            19.9564,  # Replace with accurate latitude
            19.9975,  # Replace with accurate latitude
            19.9735,  # Replace with accurate latitude
            19.9355,  # Replace with accurate latitude
            19.9754,  # Replace with accurate latitude
            19.9423,  # Replace with accurate latitude
            19.9946,  # Replace with accurate latitude
            19.9753,  # Replace with accurate latitude
            19.9892,  # Replace with accurate latitude
            19.9855   # Replace with accurate latitude
        ],
        'Longitude': [
            73.7862,  # Replace with accurate longitude
            73.7877,  # Replace with accurate longitude
            73.7906,  # Replace with accurate longitude
            73.7759,  # Replace with accurate longitude
            73.7539,  # Replace with accurate longitude
            73.7744,  # Replace with accurate longitude
            73.7912,  # Replace with accurate longitude
            73.7641,  # Replace with accurate longitude
            73.7781,  # Replace with accurate longitude
            73.7843   # Replace with accurate longitude
        ]
    }

    # Create a DataFrame from the dictionary
    return pd.DataFrame(places)

def display_map(df):
    # Rename the columns to lowercase as required by Streamlit
    df = df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

    # Display the map centered on Nashik
    st.map(df)

    # Optionally, add an interactive pydeck chart for more customization
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=19.9975,  # Replace with accurate central latitude
            longitude=73.7877,  # Replace with accurate central longitude
            zoom=12,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

def display_places_table(df):
    st.subheader('Details of Restaurants and Hotels:')
    st.write(df)
