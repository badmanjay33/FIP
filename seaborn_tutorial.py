import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'])


plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['passengers'], color='blue', marker='.', linestyle='-')
plt.title('Line Plot: Airline Passengers Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(df['year'], df['passengers'], color='darkorange', alpha=0.7, edgecolors='k')
plt.title('Scatter Plot: Passengers by Year')
plt.xlabel('Year')
plt.ylabel('Number of Passengers')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='passengers', bins=15, kde=True, color='purple')
plt.title('Histogram: Distribution of Passenger Counts')
plt.xlabel('Number of Passengers')
plt.ylabel('Frequency (Months)')
plt.show()


plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x='month', y='passengers', hue='month', palette='Set3', legend=False)
plt.title('Box Plot: Passenger Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.show()