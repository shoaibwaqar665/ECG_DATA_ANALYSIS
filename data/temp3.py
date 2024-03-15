import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load ECG data from the CSV file
data = pd.read_csv('filtered_results/WFDBRecords/01/010/JS00001_filtered.csv')

# Extract ECG signal data (excluding the 'time' column)
X = data.iloc[:, 1:].values

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
X_pca = pca.fit_transform(X)

# Create a new DataFrame with the principal components and time
df_pca = pd.DataFrame({'time': data['time'], 'PC1': X_pca[:, 0], 'PC2': X_pca[:, 1]})

# Plot the principal components against time
plt.figure(figsize=(12, 6))
plt.plot(df_pca['time'], df_pca['PC1'], label='Principal Component 1')
plt.plot(df_pca['time'], df_pca['PC2'], label='Principal Component 2')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ECG Signals Projected onto the First Two Principal Components')
plt.legend()
plt.show()