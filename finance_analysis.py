import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ingest Corporate Dataset
df = pd.read_csv('corporate_financials.csv')

# 2. Financial Metrics Engineering (No Machine Learning)
# Gross Profit = Revenue - Operating Cost
df['Gross_Profit'] = (df['Revenue'] - df['Operating_Cost']).round(2)
# Net Margin % = (Gross Profit / Revenue) * 100
df['Net_Margin_Percentage'] = ((df['Gross_Profit'] / df['Revenue']) * 100).round(2)

# 3. Aggregate Performance Across Departments (Group By Analysis)
print("\n--- Corporate Performance Summary by Department ---")
dept_summary = df.groupby('Department')[['Revenue', 'Operating_Cost', 'Gross_Profit']].sum().reset_index()
print(dept_summary)

# 4. Generate Regional Margin Leakage Chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Region', y='Net_Margin_Percentage', hue='Department', errorbar=None, palette='viridis')
plt.title('Regional Net Profit Margin Breakdown across Departments')
plt.xlabel('Corporate Region Office')
plt.ylabel('Net Profit Margin (%)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the visualization output
plt.tight_layout()
plt.savefig('regional_margin_leakage.png')
print("\n[SUCCESS]: Financial visualization saved as 'regional_margin_leakage.png'!")
