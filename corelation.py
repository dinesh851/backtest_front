import pandas as pd
from sklearn.covariance import empirical_covariance
import numpy as np

# Step 1: Load the CSV data
# Replace 'stock_data.csv' with the actual path to your CSV file
df = pd.read_csv('test_sort/market_data_2021/2021-01-01/BANKNIFTY_2021-01-01.csv')

# Step 2: Compute correlation using scikit-learn
# Select columns for which you want to calculate the correlation
selected_columns = ['close', 'high', 'low', 'open', 'VWAP']
selected_data = df[selected_columns].to_numpy()

# Calculate the covariance matrix
cov_matrix = empirical_covariance(selected_data, assume_centered=True)

# Calculate the correlation matrix from the covariance matrix
correlation_matrix = np.corrcoef(selected_data, rowvar=False)

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
