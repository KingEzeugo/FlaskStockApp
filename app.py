from flask import Flask, render_template, request
import pandas as pd
import pygal
from pygal.style import DarkSolarizedStyle

app = Flask(__name__)

# Function to load stock symbols from CSV
def load_stock_symbols():
    df = pd.read_csv('Stocks.csv')
    return df['symbol'].unique()  # Unique stock symbols

# Function to generate a stock chart
def create_chart(data, chart_type):
    if chart_type == 'Line':
        chart = pygal.Line(style=DarkSolarizedStyle)
    elif chart_type == 'Bar':
        chart = pygal.Bar(style=DarkSolarizedStyle)
    else:
        return None

    chart.title = "Stock Data Chart"
    chart.x_labels = data['date']
    chart.add("Open", data['open'])
    chart.add("High", data['high'])
    chart.add("Low", data['low'])
    chart.add("Close", data['close'])
    
    return chart.render_data_uri()

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_uri = None
    symbols = load_stock_symbols()

    if request.method == 'POST':
        # Retrieve form data
        symbol = request.form.get('symbol')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        chart_type = request.form.get('chart_type')
        
        # Load CSV data and filter by symbol and date range
        df = pd.read_csv('Stocks.csv')
        df['date'] = pd.to_datetime(df['date'])
        data = df[(df['symbol'] == symbol) & 
                  (df['date'] >= pd.to_datetime(start_date)) &
                  (df['date'] <= pd.to_datetime(end_date))]

        # Generate chart if data is available
        if not data.empty:
            chart_uri = create_chart(data, chart_type)
        else:
            chart_uri = None  # Or set a message for "No data found"

    return render_template('index.html', symbols=symbols, chart_uri=chart_uri)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
