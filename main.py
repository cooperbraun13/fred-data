from data_fetcher import init_fred, fetch_data, save_data
import matplotlib.pyplot as plt

# Initialize FRED API
fred = init_fred()

# Fetch data and save to CSV
df = fetch_data(fred)
data_path = save_data(df)

print(f"Data saved to {data_path}")
print(df.head())

# Plot data
df.plot(figsize=(10, 5), title="Economic Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend()
plt.grid()
plt.show()