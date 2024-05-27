import numpy as np
import csv
import time
import matplotlib.pyplot as plt

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

def main():
    all_lobsters = []
    all_net_capacities = []
    results = []

    # Read data from csv files
    for i in range(1 , 9):
        with open(f'{i}.csv', 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            rows = list(reader)
            num_tests = int(rows[0][0])
            num_lobsters = int(rows[0][1])
            max_value_range = int(rows[0][2])
            net_capacity = int(rows[0][3])

            all_net_capacities.append(net_capacity)
            # Parsing the lobsters size and value
            lobsters = np.array([[int(rows[1][j]), int(rows[1][j + 1])] for j in range(0, len(rows[1]), 2)])
            all_lobsters.append(lobsters)

    # Process each test case
    for i, (lobsters, net_capacity) in enumerate(zip(all_lobsters, all_net_capacities)):
        start_time = time.process_time()
        max_value, selected_sizes, selected_values = valori_maxime_homari(lobsters, net_capacity, len(lobsters))
        end_time = time.process_time()
        time_elapsed = end_time - start_time

        results.append((i+1, max_value, selected_sizes, selected_values, time_elapsed))

        with open("results_py.txt", "a") as result_file:
            result_file.write(f"Test {i+1}:\n")
            result_file.write(f"Max Value: {max_value}\n")
            result_file.write(f"Selected Sizes: {selected_sizes}\n")
            result_file.write(f"Selected Values: {selected_values}\n")
            result_file.write(f"Time Elapsed: {time_elapsed} seconds\n\n")

    # Plot the time complexities
    test_ids = [result[0] for result in results]
    times = [result[4] for result in results]

    plt.plot(test_ids, times, marker='o')
    plt.xlabel('Test Case')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of LOBSTERS Problem')
    plt.grid(True)

    # Add value labels
    for i, time_value in enumerate(times):
        plt.annotate(f'{time_value:.2f}', xy=(test_ids[i], time_value), xytext=(5,5), textcoords='offset points')

    plt.savefig('time_complexity.png')
    plt.show()

if __name__ == "__main__":
    main()
