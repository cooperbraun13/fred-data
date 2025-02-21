import pandas as pd
import requests
import matplotlib.pyplot as plt
from fredapi import Fred

API_KEY = "92b9d033043b6c4d48afcb2115d97839"

fred = Fred(api_key=API_KEY)

from fredapi import Fred

# Use your actual API key here
API_KEY = "92b9d033043b6c4d48afcb2115d97839"

# Initialize FRED API
fred = Fred(api_key=API_KEY)

# Try fetching GDP Growth Rate data
try:
    gdp_growth = fred.get_series('A191RL1Q225SBEA')  # GDP Growth Rate
    print("✅ API Key is working! Sample Data:")
    print(gdp_growth.head())  # Print first few rows

except Exception as e:
    print("❌ API Key is NOT working. Error:", e)
