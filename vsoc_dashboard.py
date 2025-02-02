import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import random

# Set up the Streamlit page configuration
st.set_page_config(page_title="VSOC Dashboard", layout="wide")
st.title("🚗 Vehicle Security Operations Center (VSOC) Dashboard")
st.markdown("**Real-time vehicle monitoring and cyberattack detection**")

# Generate sample vehicle data
def generate_vehicle_data(num_vehicles):
    data = pd.DataFrame({
        'Vehicle ID': [f'V-{i}' for i in range(1, num_vehicles + 1)],
        'Latitude': np.random.uniform(-90, 90, num_vehicles),
        'Longitude': np.random.uniform(-180, 180, num_vehicles),
        'Status': np.random.choice(['No threats detected', 'Potential threat detected', 'Confirmed cyberattack'], num_vehicles)
    })
    return data

# Number of vehicles to simulate
num_vehicles = 100
vehicle_data = generate_vehicle_data(num_vehicles)

# Display vehicle data on a map
st.header("🌍 Vehicle Locations")
vehicle_layer = pdk.Layer(
    'ScatterplotLayer',
    data=vehicle_data,
    get_position='[Longitude, Latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=200000,
    pickable=True
)
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=1
)
r = pdk.Deck(
    layers=[vehicle_layer],
    initial_view_state=view_state,
    tooltip={"text": "{Vehicle ID}\nStatus: {Status}"}
)
st.pydeck_chart(r)

# Display vehicle data in a table
st.header("📋 Vehicle Data")
st.dataframe(vehicle_data)
