FlaskStockApp
FlaskStockApp is a web-based application for visualizing historical stock data. Built with Flask and Docker, this app allows users to select stock symbols, date ranges, and chart types to view stock trends.

Overview
This project was developed as an extension of a command-line tool, making it accessible via the web using Flask. The application pulls stock symbols and data from a provided CSV file (Stocks.csv), eliminating the need for an API key. Users can select a stock, set date ranges, and view the data in line or bar chart format.

Features
Dynamic Stock Selection: Choose from symbols loaded directly from a CSV file.
Chart Visualization: View stock data as line or bar charts.
Dockerized Setup: Easily set up and deploy using Docker.
Installation
Prerequisites
Docker and Docker Compose
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/KingEzeugo/FlaskStockApp.git
cd FlaskStockApp
Build and Run with Docker

bash
Copy code
docker-compose up --build
Access the App Visit http://localhost:5000 in your browser.

Usage
Select a Stock Symbol from the dropdown.
Set Date Range and Chart Type (Line or Bar).
Click Generate Chart to display the data.
Note
All stock data is loaded from the included Stocks.csv file, with error handling for invalid entries and date ranges.

