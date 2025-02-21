import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
from fredapi import Fred

API_KEY = "92b9d033043b6c4d48afcb2115d97839"
fred = Fred(api_key=API_KEY)

# fetch economic data
gdp_growth = fred.get_series("A191RL1Q225SBEA")
inflation = fred.get_series("CPIAUCSL").pct_change() * 100
unemployment = fred.get_series("UNRATE")

df = pd.DataFrame({
    "GDP Growth (%)": gdp_growth,
    "Inflation Rate (%)": inflation,
    "Unemployment Rate (%)": unemployment
})

df.index = pd.to_datetime(df.index)
df.dropna(inplace=True)

# Define your directory and file path
data_dir = "data"  # adjust if needed
os.makedirs(data_dir, exist_ok=True)  # Create the directory if it doesn't exist
data_path = os.path.join(data_dir, "economic_data.csv")

df.to_csv(data_path)
print(f"Data saved to {data_path}")

print(df.head())

df.plot(figsize=(10, 5), title="Economic Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend()
plt.grid()
plt.show()
