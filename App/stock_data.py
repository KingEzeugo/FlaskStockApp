# app/stock_data.py
import pandas as pd

def get_stock_symbols():
    # Load the CSV file
    df = pd.read_csv('Stocks.csv')
    
    # Extract symbols and names as a list of dictionaries
    symbols = df[['symbol', 'name']].drop_duplicates()
    return symbols.to_dict(orient='records')  # Format for easy use in templates
