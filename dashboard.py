import pandas as pd
import streamlit as st
from datetime import datetime 
from apscheduler.schedulers.background import BackgroundScheduler
from data_fetcher import init_fred, fetch_data, save_data

# Make sure fetch_data(init_fred())) works outside st
try:
    data = fetch_data(init_fred())
    save_data(data)
    print("Data fetched successfully!")
except Exception as e:
    print(f"Data fetching failed: {e}")

# Initialize scheduler
if "scheduler_started" not in st.session_state:
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: save_data(fetch_data(init_fred())), "interval", hours=1)
    scheduler.start()
    st.session_state.scheduler_started = True
    # Fetch data immediately at startup
    save_data(fetch_data(init_fred()))
    
st.title("Economic Indicators Dashboard")

# Try loading data
try:
    df = pd.read_csv("data/economic_data.csv", index_col=0, parse_dates=True)
except Exception as e:
    st.error(f"Data loading failed: {e}")
    df = pd.DataFrame()
    
if not df.empty:
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    st.sidebar.header("Dashboard Settings")
    available_indicators = df.columns.tolist()
    selected_indicators = st.sidebar.multiselect(
        "Select Economic Indicators", available_indicators, default=available_indicators
    )
    
    min_date, max_date = df.index.min(), df.index.max()
    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = df.loc[(df.index >= pd.to_datetime(start_date)) & (df.index <= pd.to_datetime(end_date))]
    else:
        filtered_df = df.copy()
        
    if st.sidebar.checkbox("Show Correlation Matrix"):
        st.write("### Correlation Matrix")
        st.write(filtered_df[selected_indicators].corr())
        
    st.write("### Economic Indicators Over Time")
    st.line_chart(filtered_df[selected_indicators])
else:
    st.warning("No data available to display at this moment")