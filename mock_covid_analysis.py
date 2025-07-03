import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clean dataset
df = pd.read_csv("mock_covid_data.csv")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by country and sum up totals
total_cases = df.groupby('Country')[['Confirmed', 'Recovered', 'Deaths']].sum()
print("Total cases by country:")
print(total_cases)

# Plot total confirmed cases by country
plt.figure(figsize=(8, 5))
sns.barplot(x=total_cases.index, y=total_cases['Confirmed'], palette="Oranges_r")
plt.title("Total Confirmed COVID-19 Cases by Country")
plt.ylabel("Confirmed Cases")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# Plot trend for India
india = df[df['Country'] == 'India']
plt.figure(figsize=(10, 5))
plt.plot(india['Date'], india['Confirmed'], label='Confirmed')
plt.plot(india['Date'], india['Recovered'], label='Recovered')
plt.plot(india['Date'], india['Deaths'], label='Deaths')
plt.title("COVID-19 Trend in India")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.tight_layout()
plt.show()
