import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import random
import time

# Set up the Streamlit page configuration
st.set_page_config(page_title="VSOC & IDPS Demo Dashboard", layout="wide")
st.title("🚗 Vehicle Security Operations Center (VSOC) & Intrusion Detection and Prevention System (IDPS) Demo Dashboard")
st.markdown("**Simulated real-time vehicle monitoring, cyberattack detection, IDPS activation, VSOC alerts, and OTA updates**")

# Initialize session state for vehicle data and alerts
if 'vehicle_data' not in st.session_state:
    st.session_state.vehicle_data = pd.DataFrame()
if 'vsoc_alerts' not in st.session_state:
    st.session_state.vsoc_alerts = pd.DataFrame()

# Sidebar: User Inputs
st.sidebar.header("User Inputs")
num_vehicles = st.sidebar.slider("Number of Vehicles", min_value=10, max_value=500, value=100, step=10)

# Function to generate random vehicle data
def generate_vehicle_data(num):
    data = pd.DataFrame({
        'latitude': np.random.uniform(-90, 90, num),
        'longitude': np.random.uniform(-180, 180, num),
        'Vehicle ID': [f"V-{i}" for i in range(1, num + 1)],
        'Status': ['Normal'] * num
    })
    return data

# Function to simulate cyberattacks
def simulate_cyber_attack():
    data = st.session_state.vehicle_data.copy()
    attack_types = ["SQL Injection", "Spoofing Attack", "DoS Attack", "Malware Injection"]
    num_attacks = random.randint(1, len(data) // 10)
    attack_indices = random.sample(range(len(data)), num_attacks)
    for idx in attack_indices:
        data.at[idx, 'Status'] = random.choice(attack_types)
    st.session_state.vehicle_data = data
    st.warning("Cyberattack simulated!")

# Function to activate IDPS
def activate_idps_system():
    data = st.session_state.vehicle_data
    detected_attacks = data[data['Status'] != 'Normal']
    if not detected_attacks.empty:
        st.session_state.vsoc_alerts = detected_attacks[['Vehicle ID', 'Status']]
        st.error(f"{len(detected_attacks)} attacks detected!")
    else:
        st.success("No attacks detected.")

# Function to initiate OTA update
def initiate_ota_update():
    with st.spinner('Deploying OTA Update...'):
        time.sleep(2)
        st.success("OTA Update Deployed Successfully!")

# Generate initial vehicle data if not already generated
if st.session_state.vehicle_data.empty:
    st.session_state.vehicle_data = generate_vehicle_data(num_vehicles)

# Display the map with vehicle locations as red dots
st.header("🌍 Vehicle Locations")
vehicle_layer = pdk.Layer(
    'ScatterplotLayer',
    data=st.session_state.vehicle_data,
    get_position='[longitude, latitude]',
    get_fill_color='[255, 0, 0, 160]',
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
    tooltip={"text": "{Vehicle ID}"}
)
st.pydeck_chart(r)

# Buttons for actions
st.sidebar.button("Simulate Cyberattack", on_click=simulate_cyber_attack)
st.sidebar.button("Activate IDPS", on_click=activate_idps_system)
st.sidebar.button("Initiate OTA Update", on_click=initiate_ota_update)

# Display VSOC Alerts if they exist
if not st.session_state.vsoc_alerts.empty:
    st.subheader("📡 VSOC Alerts")
    st.dataframe(st.session_state.vsoc_alerts)

# Footer
st.markdown("---")
st.markdown("**Developed to demonstrate an advanced VSOC and IDPS with real-time monitoring and response capabilities.**")
