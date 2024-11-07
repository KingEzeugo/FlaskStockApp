# app/routes.py
from flask import render_template, request
from .stock_data import get_stock_symbols
from . import create_app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    symbols = get_stock_symbols()  # Load symbols from CSV
    
    if request.method == 'POST':
        # Handle the form submission and render chart here, if needed
        selected_symbol = request.form.get('symbol')
        return f"Selected stock symbol: {selected_symbol}"
    
    return render_template('index.html', symbols=symbols)

