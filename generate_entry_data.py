import numpy as np
import pandas as pd

def generate_data(no_of_tests, len_of_homari_array, maximum_value_of_range):
    """
     Generate random data for the given parameters.
    
    Parameters:
        no_of_tests (int): Number of test cases.
        len_of_homari_array (int): Length of each homari array.
        maximum_value_of_range (int): Maximum value for random data.
        
      Returns:
        np_data_array (list): List of NumPy arrays containing random data.
    """
    np_data_array = [np.random.randint(maximum_value_of_range, size=(len_of_homari_array, 2), dtype=np.int64) for _ in range(no_of_tests)]
    return np_data_array

def create_csv_file(filename, data, no_of_tests, len_of_homari_array, maximum_value_of_range, capacitate_plasa):
    """
    Create a CSV file with the provided data and metadata(nontrivial data).
    
      Parameters:
        filename (str): Name of the CSV file to create.
        data (list): List of NumPy arrays containing data for each test case.
        no_of_tests (int): Number of test cases.
        len_of_homari_array (int): Length of each homari array.
        maximum_value_of_range (int): Maximum value for random data.
        capacitate_plasa (int): Fishing net capacity.
    """
    flattened_data = [arr.ravel() for arr in data]
    df_csv = pd.DataFrame(flattened_data)
    metadata_row = [no_of_tests, len_of_homari_array, maximum_value_of_range, capacitate_plasa]
    metadata_df = pd.DataFrame([metadata_row])
    df_csv = pd.concat([metadata_df, df_csv], ignore_index=True)
    df_csv.to_csv(filename, index=False, header=False, sep='\t')

def load_to_csv(filename, no_of_tests, len_of_homari_array, maximum_value_of_range, capacitate_plasa):
    """
    Generate random data and create a CSV file with the provided metadata(non-trivial big data).
    
      Parameters:
        filename (str): Name of the CSV file to create.
        no_of_tests (int): Number of test cases.
        len_of_homari_array (int): Length of each homari array.
        maximum_value_of_range (int): Maximum value for random data.
        capacitate_plasa (int): Fishing net capacity.
    """
    data = generate_data(no_of_tests, len_of_homari_array, maximum_value_of_range) 
    create_csv_file(filename, data, no_of_tests, len_of_homari_array, maximum_value_of_range, capacitate_plasa)
