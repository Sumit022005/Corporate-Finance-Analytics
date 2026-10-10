import pandas as pd
import sqlite3

# 1. Load your CSV data into Python
df = pd.read_csv('corporate_financials.csv')

# 2. Create an in-memory SQL database connection
conn = sqlite3.connect(':memory:')

# 3. Dump the CSV data into an SQL table named 'corporate_financials'
df.to_sql('corporate_financials', conn, index=False, if_exists='replace')

# 4. Write and execute your SQL query here
query = """
SELECT 
    Department,
    SUM(Revenue) AS Total_Department_Revenue,
    SUM(Operating_Cost) AS Total_Department_Cost,
    ROUND((SUM(Revenue) - SUM(Operating_Cost)), 2) AS Absolute_Gross_Profit,
    ROUND(((SUM(Revenue) - SUM(Operating_Cost)) / SUM(Revenue)) * 100, 2) AS Profit_Margin_Pct
FROM corporate_financials
GROUP BY Department
ORDER BY Profit_Margin_Pct ASC;
"""

# 5. Run the query and view the database output table
output_df = pd.read_sql_query(query, conn)
print("\n--- 📊 SQL Query Output Result ---")
print(output_df.to_string(index=False))
