import streamlit as st
from datetime import datetime
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

API_Key = '5e8ed80210b838d7123b16e9e8faf111'

# Create the FRED Object
fred = Fred(api_key=API_Key)

# Get the Rates from FRED
series_ids = {
    'Fed Funds Rate': 'FEDFUNDS',
    'Prime Rate': 'PRIME',
    '30 Year Mortgage Rate': 'MORTGAGE30US',
    '15 Year Mortgage Rate': 'MORTGAGE15US',
    '10 Year vs. 2 Year Treasury': 'T10Y2Y',
    '10 Year Treasury Rate': 'DGS10',
    '2 Year Treasury Rate': 'DGS2'
}

data = {}
current_rates = {}

for key, series_id in series_ids.items():
    data[key] = fred.get_series(series_id=series_id)
    current_rates[key] = data[key].iloc[-1]

# Convert series to DataFrame
data_frames = {key: pd.DataFrame(value, columns=[key]) for key, value in data.items()}

# Streamlit app
st.title('Mortgage Rates Dashboard')

for key, df in data_frames.items():
    st.header(key)
    st.write(f"Current {key}: {current_rates[key]:.2f}")
    st.line_chart(df)
