import pandas as pd
import numpy as np

# Set random seed for consistent corporate financial data
np.random.seed(42)
num_records = 5000

# Generate synthetic fields
data = {
    'Transaction_ID': [f'TXN{1000 + i}' for i in range(num_records)],
    'Date': pd.date_range(start='2025-01-01', periods=num_records, freq='h')[:num_records],
    'Department': np.random.choice(['IT Operations', 'Marketing', 'Sales Infrastructure', 'Human Resources', 'R&D'], num_records),
    'Region': np.random.choice(['North India', 'South India', 'West India', 'East India'], num_records),
    'Revenue': np.random.uniform(5000, 75000, num_records).round(2),
    'Operating_Cost': np.random.uniform(3000, 50000, num_records).round(2)
}

# Create Dataframe and save it
df = pd.DataFrame(data)
df.to_csv('corporate_financials.csv', index=False)
print("[SUCCESS]: 'corporate_financials.csv' generated with 5,000 corporate records!")
