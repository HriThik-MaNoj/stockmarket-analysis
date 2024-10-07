# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
file_path = 'symbols_valid_meta.csv'  # Update with your CSV file path
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Head:")
print(data.head())  # Displays the first 5 rows of the dataset
print("\nDataset Info:")
print(data.info())  # Gives information about data types, missing values, etc.
print("\nStatistical Summary:")
print(data.describe())  # Summary statistics for numerical columns

# Visualizing Closing Price Trends
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Price Trend Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Visualizing Stock Volume
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Volume'], color='orange')
plt.xlabel('Date')
plt.ylabel('Stock Volume')
plt.title('Stock Volume Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Stock Market Data')
plt.show()

# Moving Averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Plotting Moving Averages
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.plot(data['Date'], data['MA50'], label='50-Day MA', linestyle='--')
plt.plot(data['Date'], data['MA200'], label='200-Day MA', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Moving Averages (50-Day & 200-Day)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

