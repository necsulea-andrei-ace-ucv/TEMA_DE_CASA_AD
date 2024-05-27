import numpy as np
from read_data_from_csv_py import read_latest_csv_as_numpy_array
import matplotlib.pyplot as plt
import time

def valori_maxime_homari(homari_valoare, capacitate_plasa, n):

    """
    This function implements the 0/1 Knapsack algorithm to find the maximum value
    of lobsters that can be captured within the given net capacity.
    
    Parameters:
    - homari_valoare: List of pairs representing the size and value of each lobster.
    - capacitate_plasa: The maximum capacity of the net.
    - n: The number of lobsters.
    
    Returns:
    - max_value: The maximum value that can be captured.
    - selected_sizes: List of sizes of the lobsters included in the optimal solution.
    - selected_values: List of values of the lobsters included in the optimal solution.
    
    The algorithm uses dynamic programming to build a matrix where the entry at [i][c]
    represents the maximum value that can be achieved with the first i lobsters and 
    capacity c. It also tracks which items are included in the optimal solution.
    """

    # Initialize the DP matrix and the keep matrix
    matrice_valori_maxime = np.zeros((n + 1, capacitate_plasa + 1), dtype=np.int64)
    keep = np.zeros((n + 1, capacitate_plasa + 1), dtype=np.int64)
    
    # Fill the DP matrix
    for i in range(1, n + 1):
        size = homari_valoare[i - 1][0]
        value = homari_valoare[i - 1][1]
        for c in range(capacitate_plasa + 1):
            if c >= size and matrice_valori_maxime[i - 1][c - size] + value > matrice_valori_maxime[i - 1][c]:
                matrice_valori_maxime[i][c] = matrice_valori_maxime[i - 1][c - size] + value
                keep[i][c] = 1
            else:
                matrice_valori_maxime[i][c] = matrice_valori_maxime[i - 1][c]
    
    # Maximum value achieved
    max_value = matrice_valori_maxime[n][capacitate_plasa]
    
    # Determine which items to keep
    selected_sizes = []
    selected_values = []
    c = capacitate_plasa
    for i in range(n, 0, -1):
        if keep[i][c]:
            selected_sizes.append(homari_valoare[i - 1][0])
            selected_values.append(homari_valoare[i - 1][1])
            c -= homari_valoare[i - 1][0]

    selected_sizes.sort(reverse=True)
    selected_values.sort(reverse=True)

    return max_value, selected_sizes, selected_values


def algorithm_py():

    """
    Main function to read the input data, process each test case using the
    valori_maxime_homari function, and write the results to the output file.
    
    The input data is read from the latest CSV file and consists of the first row
    with meta-information and subsequent rows with lobster size-value pairs.
    
    The results include the maximum value of capture for each test, as well as the
    sizes and values of the lobsters selected in the optimal solution.
    """


    first_row, homari = read_latest_csv_as_numpy_array()
    if first_row is not None and homari is not None:
        capacitate_plasa = int(first_row[3])
        n = int(first_row[1])

        results = []
        all_selected_sizes = []
        all_selected_values = []
        times = []

        for test_number, test_data in enumerate(homari):
            lobsters_data = np.array([(int(test_data[i]), int(test_data[i + 1])) for i in range(0, len(test_data), 2)], dtype=np.int64)
            
            # Measure the time for each test case
            start_time = time.time()
            max_value, selected_sizes, selected_values = valori_maxime_homari(lobsters_data, capacitate_plasa, n)
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            times.append(elapsed_time)
            
            results.append(max_value)
            all_selected_sizes.append(selected_sizes)
            all_selected_values.append(selected_values)

        # Write results to output_py.txt file
        with open("output_py.txt", "w") as file:
            file.write(f"No. of tests: {first_row[0]}\n")
            file.write(f"No. of lobsters: {first_row[1]}\n")
            file.write(f"Maximum value for random data: {first_row[2]}\n")
            file.write(f"Net capacity: {first_row[3]}\n\n")

            file.write(f"\nLobsters data:\n\n")
            for test_number, test_data in enumerate(homari):
                file.write(f"Test no. {test_number + 1}: ")
                for i in range(0, len(test_data), 2):
                    file.write(f"[{test_data[i]}, {test_data[i + 1]}] ")
                file.write("\n")
            
            file.write(f"\nSizes:\n")
            for test_number, test_data in enumerate(homari):
                file.write(f"Test no. {test_number + 1} : ")
                for i in range(0, len(test_data), 2):
                    file.write(f"{test_data[i]} ")
                file.write("\n")

            file.write(f"\nValues:\n")
            for test_number, test_data in enumerate(homari):
                file.write(f"Test no. {test_number + 1} : ")
                for i in range(1, len(test_data), 2):
                    file.write(f"{test_data[i]} ")
                file.write("\n")

            file.write(f"\n\nMaximum value of capture per test:\n\n")
            for test_number, max_value in enumerate(results):
                file.write(f"Test no. {test_number + 1}:\n")
                file.write(f"Maximum value: {max_value}\n")
                
                file.write("Sizes: ")
                sizes_sum = 0
                for size in all_selected_sizes[test_number]:
                    if sizes_sum > 0:
                        file.write(" + ")
                    file.write(f"{size}")
                    sizes_sum += size
                file.write(f" = {sizes_sum}\n")

                file.write("Values: ")
                values_sum = 0
                for value in all_selected_values[test_number]:
                    if values_sum > 0:
                        file.write(" + ")
                    file.write(f"{value}")
                    values_sum += value
                file.write(f" = {values_sum}\n")
                file.write(f"CPU Time: {times[test_number]:.4f} seconds\n")
                file.write("\n")

        # Plot the time complexity chart
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(times) + 1), times, marker='o', linestyle='-', color='b')
        plt.xlabel('Test Case Number')
        plt.ylabel('Time (seconds)')
        plt.title('Time Complexity (Python version)')
        plt.grid(True)
        
        # Annotate the times on the chart
        for i, time_value in enumerate(times):
            plt.text(i + 1, time_value, f'{time_value:.4f}', fontsize=9, ha='right')

        plt.show()