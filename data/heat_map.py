# line chart 
ecg_data_path = 'filtered_results/WFDBRecords/01/010/JS00001_filtered.csv' # Adjust the path as needed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.fft import fft

# Assuming ecg_data is already loaded as follows:
ecg_data = pd.read_csv(ecg_data_path)

# Setting up the figure layout
fig, axs = plt.subplots(2, 1, figsize=(20, 20), constrained_layout=True)

# Heatmap of the first 1000 data points
subset = ecg_data.iloc[:1000, 1:13] # Adjust the range as needed
sns.heatmap(subset.transpose(), cmap="YlGnBu", cbar_kws={'label': 'Signal Amplitude'}, ax=axs[0])
axs[0].set_title('ECG Signal Heatmap')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Lead')

# Subplots for each lead
leads = ecg_data.columns[1:]
for i, lead in enumerate(leads):
    axs[1].plot(ecg_data['time'], ecg_data[lead], label=lead)
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
axs[1].legend(ncol=3)
axs[1].set_title('ECG Signals for All Leads')

plt.show()
