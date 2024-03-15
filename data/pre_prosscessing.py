import os
import csv
import wfdb
import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
# Butterworth Low-Pass Filter functions
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs  # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Function to process each file and apply noise removal
def process_file(hea_file_path, result_folder, filtered_folder, file_name):
    print("Processing", file_name)
    # Read the WFDB file using rdsamp function
    signals, metadata = wfdb.rdsamp(hea_file_path)

    # Access metadata information
    fs = metadata['fs']
    sig_len = metadata['sig_len']
    n_sig = metadata['n_sig']
    sig_names = metadata['sig_name']

    # Set cutoff frequency for low-pass filter
    cutoff = 100  # Example cutoff frequency of 100Hz

    # Apply filter to each signal
    filtered_signals = np.array([butter_lowpass_filter(signals[:, i], cutoff, fs) for i in range(n_sig)])

    # Write the original data to CSV file
    csv_file_name = os.path.join(result_folder, f"{file_name}.csv")
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['time'] + sig_names
        writer.writerow(header)
        for i in range(sig_len):
            time_stamp = i / fs  # Calculate the time stamp
            row = [time_stamp] + signals[i].tolist()
            writer.writerow(row)

    # Write the filtered data to a new CSV file in the filtered_folder directory
    filtered_csv_file_name = os.path.join(filtered_folder, f"{file_name}_filtered.csv")
    with open(filtered_csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Writing the same header
        for i in range(sig_len):
            time_stamp = i / fs  # Calculate the time stamp
            row = [time_stamp] + filtered_signals[:, i].tolist()
            writer.writerow(row)

    print(f"File {file_name} processed and filtered data saved successfully.")

# Function to process a directory of files
def process_directory(directory, base_dir, result_base_dir, filtered_base_dir):
    result_dir = os.path.join(result_base_dir, directory)
    filtered_dir = os.path.join(filtered_base_dir, directory)
    os.makedirs(result_dir, exist_ok=True)
    os.makedirs(filtered_dir, exist_ok=True)

    records_path = os.path.join(base_dir, directory, 'RECORDS')  # Path to the RECORDS file
    if os.path.exists(records_path):
        with open(records_path, 'r') as records_file:
            for line in records_file:
                file_name = line.strip()
                hea_file_path = os.path.join(base_dir, directory, file_name)

                # Check if .hea file exists
                if os.path.exists(f"{hea_file_path}.hea"):
                    # Process the file
                    process_file(hea_file_path, result_dir, filtered_dir, file_name)
                else:
                    print(f"Missing .hea file for {file_name}")

    else:
        print('Could not find RECORDS file:', records_path)

    # Recursively process subdirectories
    current_dir_path = os.path.join(base_dir, directory)  # Path to the current directory
    for subdir in os.listdir(current_dir_path):
        subdir_path = os.path.join(current_dir_path, subdir)
        if os.path.isdir(subdir_path):
            process_directory(subdir, base_dir, result_base_dir, filtered_base_dir)

# Main execution
if __name__ == "__main__":
    records_directory = 'data'
    result_directory = 'results'
    filtered_result_directory = 'filtered_results'
    first_records_filename = 'RECORDS.txt'

    # Read the list of subfolder paths from the first RECORDS file
    with open(os.path.join(records_directory, first_records_filename), 'r') as first_records_file:
        subfolder_paths = first_records_file.read().splitlines()

    # Process each subfolder path
    for subfolder_path in subfolder_paths:
        process_directory(subfolder_path, records_directory, result_directory, filtered_result_directory)

