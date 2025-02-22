import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
from fredapi import Fred

API_KEY = "92b9d033043b6c4d48afcb2115d97839"

# initialize FRED API client
fred = Fred(api_key=API_KEY)

# fetch economic data
gdp_growth = fred.get_series("A191RL1Q225SBEA")
# computes percent change and then multiplies by 100 to convert to a percentage
inflation = fred.get_series("CPIAUCSL").pct_change() * 100
unemployment = fred.get_series("UNRATE")

# 3 columns with gdp growth, inflation rate, and unemployment rate
df = pd.DataFrame({
    "GDP Growth (%)": gdp_growth,
    "Inflation Rate (%)": inflation,
    "Unemployment Rate (%)": unemployment
})

# convert to datetime format
# any rows with missing values are removed
df.index = pd.to_datetime(df.index)
df.dropna(inplace=True)

data_dir = "data"
# created the directory because it wasn't recognizing my folder
os.makedirs(data_dir, exist_ok=True)
data_path = os.path.join(data_dir, "economic_data.csv")

# writes teh df to a csv file
df.to_csv(data_path)
print(f"Data saved to {data_path}")

print(df.head())

# plots the data
df.plot(figsize=(10, 5), title="Economic Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend()
plt.grid()
plt.show()
