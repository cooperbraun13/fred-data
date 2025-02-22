import pandas as pd
import streamlit as st
from datetime import datetime 
from apscheduler.schedulers.background import BackgroundScheduler
from data_fetcher import init_fred, fetch_data, save_data

# Initialize scheduler