import streamlit as st
import pandas as pd
import numpy as np
import random

# Set up the Streamlit page configuration
st.set_page_config(page_title="IDPS Demo", layout="wide")
st.title("🛡️ Intrusion Detection and Prevention System (IDPS) Demo")
st.markdown("**Simulating cyberattacks and IDPS responses**")

# Generate sample cyberattack data
def generate_attack_data(num_attacks):
    data = pd.DataFrame({
        'Attack ID': [f'A-{i}' for i in range(1, num_attacks + 1)],
        'Attack Type': np.random.choice(['Malware', 'DoS', 'Spoofing', 'Man-in-the-Middle'], num_attacks),
        'Severity': np.random.choice(['Low', 'Medium', 'High'], num_attacks),
        'Status': np.random.choice(['Detected', 'Prevented', 'Failed'], num_attacks)
    })
    return data

# Number of attacks to simulate
num_attacks = 50
attack_data = generate_attack_data(num_attacks)

# Display attack data in a table
st.header("⚠️ Cyberattack Data")
st.dataframe(attack_data)

# Display attack statistics
st.header("📊 Attack Statistics")
attack_counts = attack_data['Attack Type'].value_counts()
st.bar_chart(attack_counts)
