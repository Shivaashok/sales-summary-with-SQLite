# sales-summary-with-SQLite

Objective:
Use Python and SQL to pull simple sales information (like total quantity sold and total revenue) from a tiny SQLite database, display the results, and visualize them with a basic bar chart.

Tools Required:

Python (with sqlite3, pandas, matplotlib)

SQLite (built into Python, no extra setup)

Jupyter Notebook or a .py file

Database:

sales_data.db

One table called "sales" with the following columns:

id (INTEGER PRIMARY KEY)

product (TEXT)

quantity (INTEGER)

price (REAL)

Steps to Run the Script:

Ensure Python is installed with pandas and matplotlib.

Run the script to create and populate the SQLite database with sample sales data.

The script will connect to the database using sqlite3.

It will execute a SQL query to calculate total quantity sold and total revenue per product.

The results will be loaded into a pandas DataFrame.

The DataFrame will be printed in the console.

A simple bar chart will be generated showing total revenue per product.

The chart can be saved as "sales_chart.png".

Expected Output:

Console output showing total quantity and revenue for each product.

A bar chart displaying total revenue by product.

Learning Outcomes:

Writing basic SQL queries.

Importing SQL data into Python using pandas.

Performing simple data summaries.

Creating a simple sales visualization with matplotlib.

Instructions for Customization:

Add more rows to the sales table by modifying the sample_data list.

Adjust the SQL query if additional summary metrics are needed (e.g., average price).

Change the chart style or colors using matplotlib parameters.
