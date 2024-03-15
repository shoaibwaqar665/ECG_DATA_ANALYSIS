
import pandas as pd
import matplotlib.pyplot as plt

# Ensure you have the 'filtered_results/WFDBRecords/010/JS00001_filtered.csv' file in the correct location
df = pd.read_csv('filtered_results/WFDBRecords/01/010/JS00001_filtered.csv')

# Extract the necessary columns for visualization
time = df['time']
lead_I = df['I']
lead_II = df['II']
lead_III = df['III']
lead_AVF = df['aVF']
lead_AVL = df['aVL']
lead_AVR = df['aVR']
lead_V1 = df['V1']
lead_V2 = df['V2']
lead_V3 = df['V3']
lead_V4 = df['V4']
lead_V5 = df['V5']
lead_V6 = df['V6']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, lead_I, label='Lead I')
plt.plot(time, lead_II, label='Lead II')
plt.plot(time, lead_III, label='Lead III')
plt.plot(time, lead_AVF, label='Lead AVF')
plt.plot(time, lead_AVL, label='Lead AVL')
plt.plot(time, lead_AVR, label='Lead AVR')
plt.plot(time, lead_V1, label='Lead V1')
plt.plot(time, lead_V2, label='Lead V2')
plt.plot(time, lead_V3, label='Lead V3')
plt.plot(time, lead_V4, label='Lead V4')
plt.plot(time, lead_V5, label='Lead V5')
plt.plot(time, lead_V6, label='Lead V6')

# Customize the plot
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('ECG Measurements')
plt.legend()
plt.grid(True)  # Adding grid for better readability

# Display the plot
plt.show()