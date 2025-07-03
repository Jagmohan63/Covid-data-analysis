
# covid_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("covid_data.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Data cleaning
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])

# Total confirmed cases by country
top_countries = df.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 countries with highest confirmed cases:")
print(top_countries)

# Plot top 10 countries by confirmed cases
plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='orange')
plt.title('Top 10 Countries by Confirmed Cases')
plt.ylabel('Confirmed Cases')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trend over time for a specific country (India)
india_data = df[df['Country'] == 'India']

plt.figure(figsize=(10,5))
plt.plot(india_data['Date'], india_data['Confirmed'], label='Confirmed')
plt.plot(india_data['Date'], india_data['Recovered'], label='Recovered')
plt.plot(india_data['Date'], india_data['Deaths'], label='Deaths')
plt.title('COVID-19 Trend in India')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()
plt.tight_layout()
plt.show()
