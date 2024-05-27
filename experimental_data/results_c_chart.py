import matplotlib.pyplot as plt

def read_results(filename):
    test_cases = []
    times = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            test_case = int(lines[i].split()[1].strip(':'))
            time_elapsed = float(lines[i + 4].split()[2])
            test_cases.append(test_case)
            times.append(time_elapsed)
    
    return test_cases, times

def plot_time_complexity(test_cases, times):
    plt.figure(figsize=(10, 5))
    plt.plot(test_cases, times, marker='o', linestyle='-', color='b')
    for i, txt in enumerate(times):
        plt.annotate(f'{txt:.4f}', (test_cases[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.xlabel('Test Case')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of LOBSTERS Problem in C')
    plt.grid(True)
    plt.savefig('time_complexity_c.png')
    plt.show()

if __name__ == "__main__":
    test_cases, times = read_results('experimental_data/results_c.txt')
    plot_time_complexity(test_cases, times)
