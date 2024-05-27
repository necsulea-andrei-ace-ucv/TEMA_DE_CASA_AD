#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <time.h>

// Define maximum number of elements and maximum line length
#define MAX_NUMBERS 1000
#define MAX_LINE_LENGTH 10000

// Macro to get the maximum of two numbers
#define max(a, b) ((a) > (b) ? (a) : (b))

// Global variables to store data
long long first_row[MAX_NUMBERS]; // Stores the first row of input data
long long lobsters_data[MAX_NUMBERS][MAX_NUMBERS][2]; // Stores the main data matrix
int first_row_length = 0; // Length of the first row
int num_rows = 0; // Number of rows in the main data matrix
int num_cols = 0; // Number of columns in the main data matrix
clock_t start, end;
double cpu_time_used;

/*
 * Reads data from a CSV file and populates the first_row and lobsters_data arrays.
 * The first_row array contains metadata, and the lobsters_data array contains size-value pairs.
 */
void read_data(const char *filename) 
{
    // Open the file in read mode
    FILE *file = fopen(filename, "r");
    if (file == NULL) 
    {
        perror("Error opening file"); // Print error message if file cannot be opened
        exit(EXIT_FAILURE);
    }

    // Buffer to read each line
    char line[MAX_LINE_LENGTH];
    int row_index = 0; // Index of the current row being read

    // Read each line of the file
    while (fgets(line, sizeof(line), file) != NULL) 
    {
        // Tokenize the line by tabs, spaces, and newline characters
        char *token = strtok(line, "\t \n");
        int col_index = 0; // Index of the current column being read

        // Process each token in the line
        while (token != NULL) 
        {
            char *endptr;
            errno = 0;
            // Convert the token to a long long integer
            long long num = strtoll(token, &endptr, 10);

            // Check for conversion errors
            if (errno != 0 || endptr == token) 
            {
                perror("strtoll"); // Print error message if conversion fails
                fclose(file);
                exit(EXIT_FAILURE);
            }

            // Store the data in the appropriate location
            if (row_index == 0) 
            {
                first_row[first_row_length++] = num; // Store in the first row
            } 
            else 
            {
                int element_index = col_index / 2;
                int sub_index = col_index % 2;
                lobsters_data[row_index - 1][element_index][sub_index] = num; // Store in the main data matrix
            }

            col_index++;
            token = strtok(NULL, "\t \n");
        }

        // Update the number of columns if it's the second row
        if (row_index == 1) 
        {
            num_cols = col_index / 2;
        }

        row_index++;
    }

    // Update the number of rows
    num_rows = row_index - 1;
    fclose(file); // Close the file
}

// Function to send data pointers to caller
void send_data(long long **first_row_ptr, long long ***lobsters_data_ptr, int *first_row_length_ptr, int *num_rows_ptr, int *num_cols_ptr) 
{
    *first_row_ptr = first_row;
    *lobsters_data_ptr = (long long **)lobsters_data;
    *first_row_length_ptr = first_row_length;
    *num_rows_ptr = num_rows;
    *num_cols_ptr = num_cols;
}

// Function to sort an array in descending order
void sort_desc(long long arr[], int n) 
{
    for (int i = 0; i < n - 1; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            if (arr[i] < arr[j]) 
            {
                long long temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

/*
 * Implements the 0/1 Knapsack algorithm to find the maximum value of lobsters that can be captured
 * within the given net capacity. It also tracks the sizes and values of the selected lobsters.
 */
long long valori_maxime_homari(long long homari_valoare[][2], long capacitate_plasa, long n, long long *selected_sizes, long long *selected_values) 
{
    // Allocate memory for dynamic programming matrices
    long long **matrice_valori_maxime = malloc((n + 1) * sizeof(long long *));
    int **keep = malloc((n + 1) * sizeof(int *));
    for (long i = 0; i <= n; i++) 
    {
        matrice_valori_maxime[i] = malloc((capacitate_plasa + 1) * sizeof(long long));
        keep[i] = malloc((capacitate_plasa + 1) * sizeof(int));
    }

    // Initialize matrices with zeros
    for (long i = 0; i <= n; i++)
        for (long j = 0; j <= capacitate_plasa; j++) 
        {
            matrice_valori_maxime[i][j] = 0;
            keep[i][j] = 0;
        }

    // Dynamic programming to find maximum value
    for (long i = 1; i <= n; i++) 
    {
        long size = homari_valoare[i - 1][0];
        long value = homari_valoare[i - 1][1];
        for (long j = 0; j <= capacitate_plasa; j++) 
        {
            if (j >= size && matrice_valori_maxime[i - 1][j - size] + value > matrice_valori_maxime[i - 1][j]) 
            {
                matrice_valori_maxime[i][j] = matrice_valori_maxime[i - 1][j - size] + value;
                keep[i][j] = 1;
            } 
            else 
            {
                matrice_valori_maxime[i][j] = matrice_valori_maxime[i - 1][j];
            }
        }
    }

    long long result_matrix = matrice_valori_maxime[n][capacitate_plasa];

    // Track the items to be included in the solution
    long k = capacitate_plasa;
    long long sum_sizes = 0, sum_values = 0;
    int index = 0;
    for (long i = n; i > 0; i--) 
    {
        if (keep[i][k]) 
        {
            selected_sizes[index] = homari_valoare[i - 1][0];
            selected_values[index] = homari_valoare[i - 1][1];
            sum_sizes += homari_valoare[i - 1][0];
            sum_values += homari_valoare[i - 1][1];
            k -= homari_valoare[i - 1][0];
            index++;
        }
    }

    // Sort the selected sizes and values in descending order
    sort_desc(selected_sizes, index);
    sort_desc(selected_values, index);

    // Clean up memory
    for (long i = 0; i <= n; i++) 
    {
        free(matrice_valori_maxime[i]);
        free(keep[i]);
    }
    free(matrice_valori_maxime);
    free(keep);

    return result_matrix;
}

int main() 
{
    long long *first_row_ptr;
    long long (*lobsters_data_ptr)[MAX_NUMBERS][2];
    int first_row_length, num_rows, num_cols;

    // Read the data from the file
    read_data("data_for_c.csv");
    send_data(&first_row_ptr, (long long ***)&lobsters_data_ptr, &first_row_length, &num_rows, &num_cols);

    long capacitate_plasa = first_row_ptr[3];

    FILE *file = fopen("output_c.txt", "w");

    if (file == NULL) 
    {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    fprintf(file, "\nNo. of tests: %lld\n", first_row_ptr[0]);
    fprintf(file, "No. of lobsters: %lld\n", first_row_ptr[1]);
    fprintf(file, "Maximum value for random data: %lld\n", first_row_ptr[2]);
    fprintf(file, "Net capacity: %lld\n", first_row_ptr[3]);

    fprintf(file, "\n\nLobsters data:\n\n");
    for (int i = 0; i < num_rows; i++) 
    {
        fprintf(file, "Test no. %d: ", i + 1);
        for (int j = 0; j < num_cols; j++) 
        {
            fprintf(file, "[%lld, %lld] ", lobsters_data_ptr[i][j][0], lobsters_data_ptr[i][j][1]);
        }
        fprintf(file, "\n");
    }

    fprintf(file, "\n\nSizes:\n");
    for (int i = 0; i < num_rows; i++) 
    {
        fprintf(file, "Test no. %d: ", i + 1);
        for (int j = 0; j < num_cols; j++) 
        {
            fprintf(file, "%lld ", lobsters_data_ptr[i][j][0]);
        }
        fprintf(file, "\n");
    }

    fprintf(file, "\nValues:\n");
    for (int i = 0; i < num_rows; i++) 
    {
        fprintf(file, "Test no. %d: ", i + 1);
        for (int j = 0; j < num_cols; j++) 
        {
            fprintf(file, "%lld ", lobsters_data_ptr[i][j][1]);
        }
        fprintf(file, "\n");
    }

    fprintf(file, "\n\nMaximum value of capture per test:\n\n");
    for (int i = 0; i < num_rows; i++) 
    {
        long long selected_sizes[MAX_NUMBERS] = {0};
        long long selected_values[MAX_NUMBERS] = {0};

        start = clock();
        long long max_value = valori_maxime_homari((long long (*)[2])lobsters_data_ptr[i], capacitate_plasa, num_cols, selected_sizes, selected_values);
        end = clock();

        fprintf(file, "Test no. %d:\n", i + 1);
        fprintf(file, "Maximum value: %lld\n", max_value);

        fprintf(file, "Sizes: ");
        long long sum_sizes = 0;
        for (int j = 0; selected_sizes[j] != 0; j++) 
        {
            if (j > 0) fprintf(file, " + ");
            fprintf(file, "%lld", selected_sizes[j]);
            sum_sizes += selected_sizes[j];
        }
        fprintf(file, " = %lld\n", sum_sizes);

        fprintf(file, "Values: ");
        long long sum_values = 0;
        for (int j = 0; selected_values[j] != 0; j++) 
        {
            if (j > 0) fprintf(file, " + ");
            fprintf(file, "%lld", selected_values[j]);
            sum_values += selected_values[j];
        }
        fprintf(file, " = %lld\n", sum_values);

        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        fprintf(file, "CPU time: %f seconds\n", cpu_time_used);

        fprintf(file, "\n");
    }

    fclose(file);

    return 0;
}
