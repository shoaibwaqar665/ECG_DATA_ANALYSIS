# line chart 
ecg_data_path = 'filtered_results/WFDBRecords/01/010/JS00001_filtered.csv' # Adjust the path as needed

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.fft import fft

# # Load the ECG data
# ecg_data = pd.read_csv(ecg_data_path)
# plt.figure(figsize=(10, 6))
# plt.plot(ecg_data['time'], ecg_data['I'], label='Lead I')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('ECG Signal for Lead I')
# plt.legend()
# plt.show()


# # Using a subset for the heatmap
# subset = ecg_data.iloc[:1000, 1:13] # Adjust the range as needed
# plt.figure(figsize=(10, 8))
# sns.heatmap(subset.transpose(), cmap="YlGnBu", cbar_kws={'label': 'Signal Amplitude'})
# plt.title('ECG Signal Heatmap')
# plt.xlabel('Time')
# plt.ylabel('Lead')
# plt.show()


# fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 10), sharex=True)
# leads = ecg_data.columns[1:]

# for i, ax in enumerate(axes.flatten()):
#     ax.plot(ecg_data['time'], ecg_data[leads[i]])
#     ax.set_title(leads[i])

# plt.tight_layout()
# plt.show()


# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'r-', animated=True)

# def init():
#     ax.set_xlim(0, 5)  # Adjust based on your data's time range
#     ax.set_ylim(-1, 1)  # Adjust according to the amplitude of your ECG signals
#     return ln,

# def update(frame):
#     xdata.append(frame)
#     ydata.append(ecg_data['I'].iloc[frame])
#     ln.set_data(xdata, ydata)
#     return ln,

# ani = FuncAnimation(fig, update, frames=range(len(ecg_data)), init_func=init, blit=True)
# plt.show()


# plt.figure(figsize=(10, 6))
# plt.plot(ecg_data['time'], ecg_data['I'], label='Lead I')
# plt.plot(ecg_data['time'], ecg_data['II'], label='Lead II', alpha=0.7)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('Comparative Plot of Lead I and II')
# plt.legend()
# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.fft import fft

# # Load the ECG data

# ecg_data = pd.read_csv(ecg_data_path)

# # Setting up the figure layout
# fig = plt.figure(constrained_layout=True, figsize=(20, 20))
# gs = fig.add_gridspec(3, 2)


# # Heatmap of the first 1000 data points
# subset = ecg_data.iloc[:1000, 1:13] # Adjust the range as needed
# ax2 = fig.add_subplot(gs[0, 1])
# sns.heatmap(subset.transpose(), cmap="YlGnBu", cbar_kws={'label': 'Signal Amplitude'}, ax=ax2)
# ax2.set_title('ECG Signal Heatmap')
# ax2.set_xlabel('Time')
# ax2.set_ylabel('Lead')

# # Subplots for each lead
# ax3 = fig.add_subplot(gs[1, :])
# leads = ecg_data.columns[1:]
# for i, lead in enumerate(leads):
#     ax3.plot(ecg_data['time'], ecg_data[lead], label=lead)
# ax3.set_xlabel('Time (s)')
# ax3.set_ylabel('Amplitude')
# ax3.legend(ncol=3)
# ax3.set_title('ECG Signals for All Leads')

# plt.show()


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
