# Federal Reverse Economic Data (FRED)
Streamlit-powered web dashboard that fetches and visualizes economic indicators from the Federal Reserve Economic Data (FRED) API. 

The key functionalities include:
Fetching Economic Data
* GDP Growth
* Inflation Rate
* Unemployment Rate

Data Storage & Updates
* Saves data to local directory
* Uses APScheduler to update data every hour

Interactive Data Visualization in Streamlit
* View a data preview
* Select specific economic indicators
* Adjust the date range for filtering
* Display a correlation matrix to compare relationships between indicators
* Generate time-series plots

Data Visualization in Matplotlib
* Allows users to generate static graphs for reports/analysis

# How It Works
Fetch Data:
* fetch_data(init_fred()) pulls GDP, Inflation, and Unemployment data from FRED
* Data is saved in data/economic_data.csv

Run Streamlit Dashboard:
* streamlit run dashboard.py launches an interactive UI

Schedule Auto-Updates
* APScheduler updates the dataset every hour
* Ensures real-time economic tracking