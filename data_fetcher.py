import os
import pandas as pd
import logging
from fredapi import Fred

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# FRED API key
API_KEY = "92b9d033043b6c4d48afcb2115d97839"

def init_fred():
    """
    Initialize and return a FRED API client 
    """
    return Fred(api_key=API_KEY)

def fetch_data(fred):
    """
    Fetch economic data from FRED and return a DataFrame
    """
    try:
        gdp_growth = fred.get_series("A191RL1Q225SBEA")
        # Convert to percentage
        inflation = fred.get_series("CPIAUCSL").pct_change() * 100
        unemployment = fred.get_series("UNRATE")
        
        df = pd.DataFrame({
            "GDP Growth (%)": gdp_growth,
            "Inflation Rate (%)": inflation,
            "Unemployment Rate (%)": unemployment
        })
        
        df.index = pd.to_datetime(df.index)
        df.dropna(inplace=True)
        
        logging.info("Data fetched successfully")
        return df
    except Exception as e:
        logging.error("Error fetching data: %s", e)
        raise
    
def save_data(df, data_dir="data", filename="economic_data.csv"):
    """
    Save DataFrame to CSV file 
    """
    os.makedirs(data_dir, exist_ok=True)
    data_path = os.path.join(data_dir, filename)
    df.to_csv(data_path)
    logging.info("Data saved to %s", data_path)
    return data_path