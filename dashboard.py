import pandas as pd
import streamlit as st
from datetime import datetime 
from apscheduler.schedulers.background import BackgroundScheduler
from data_fetcher import init_fred, fetch_data, save_data

# Initialize scheduler
if "schedular_started" not in st.session_state:
    schedular = BackgroundScheduler()
    schedular.add_job(lambda: save_data(fetch_data(init_fred())), "interval", hours=1)
    schedular.start()
    st.session_state.schedular_started = True
    # Fetch data immediately at startup
    save_data(fetch_data(init_fred()))
    
st.title("Economic Indicators Dashboard")

# Try loading data
try:
    df = pd.read_csv("data/economic_data.csv", index_col=0, parse_dates=True)
except Exception as e:
    st.error("Data not available, please wait for the data fetching job to complete")
    df = pd.DataFrame()