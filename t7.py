import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("sales_data.db")

# SQL query: total quantity and total revenue per product
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# Load SQL query into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the summary
print("Sales Summary:")
print(df)

# Bar chart: products vs total revenue
plt.figure(figsize=(6,4))
plt.bar(df['product'], df['total_revenue'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Revenue ($)')
plt.title('Total Revenue by Product')
plt.tight_layout()

# Show the plot
plt.show()

# Optionally save the chart
plt.savefig("sales_chart.png")
