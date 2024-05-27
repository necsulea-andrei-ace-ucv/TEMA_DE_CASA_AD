import csv
import os
import glob
from tkinter import messagebox
import numpy as np

#read data from csv as a numpy array...making first_row list for the length data such no of tests, length of the fishing net etc.
#the data list is for sizes and values pairs....
def read_latest_csv_as_numpy_array():
    directory = os.getcwd()

    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    if csv_files:
        latest_file = max(csv_files, key=os.path.getctime)
        with open(latest_file, mode='r') as file:
            csv_reader = csv.reader(file, delimiter='\t')  # Specify tab as the delimiter
            rows = list(csv_reader)
        rows = [[item for item in row if item] for row in rows]
        first_row = np.array([int(item) for item in rows[0] if item])
        data = [[float(item) for item in row if item] for row in rows[1:]]
        return first_row, data
    else:
        messagebox.showerror("Error", "No CSV files found in the directory.")
        return None, None
    

#this function is described clearly into 'obtain_data_for_c_file.py'
#it detects the last created csv with the help of os module 
#after that returns the data through an already created and empty csv file different from the last created
def write_latest_csv_to_new_csv(filename):
    directory = os.getcwd()

    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    if csv_files:
        latest_file = max(csv_files, key=os.path.getctime)
        with open(latest_file, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
        with open(filename, 'w') as f:
            for row in rows:
                f.write(','.join(row) + '\n')

        #print(f"Data from {latest_file} written to {filename}")
        return True
    else:
        messagebox.showerror("Error", "No CSV files found in the directory.")
        return False