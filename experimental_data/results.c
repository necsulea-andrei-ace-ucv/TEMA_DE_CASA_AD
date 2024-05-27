#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct {
    int size;
    int value;
} Lobster;

void valori_maxime_homari(Lobster *lobsters, int n, int capacitate_plasa, int *max_value, int *selected_sizes, int *selected_values, int *selected_count) {
    int **matrice_valori_maxime = malloc((n + 1) * sizeof(int *));
    int **keep = malloc((n + 1) * sizeof(int *));
    for (int i = 0; i <= n; i++) {
        matrice_valori_maxime[i] = malloc((capacitate_plasa + 1) * sizeof(int));
        keep[i] = malloc((capacitate_plasa + 1) * sizeof(int));
    }

    for (int i = 0; i <= n; i++) {
        for (int c = 0; c <= capacitate_plasa; c++) {
            matrice_valori_maxime[i][c] = 0;
            keep[i][c] = 0;
        }
    }

    for (int i = 1; i <= n; i++) {
        int size = lobsters[i - 1].size;
        int value = lobsters[i - 1].value;
        for (int c = 0; c <= capacitate_plasa; c++) {
            if (c >= size && matrice_valori_maxime[i - 1][c - size] + value > matrice_valori_maxime[i - 1][c]) {
                matrice_valori_maxime[i][c] = matrice_valori_maxime[i - 1][c - size] + value;
                keep[i][c] = 1;
            } else {
                matrice_valori_maxime[i][c] = matrice_valori_maxime[i - 1][c];
            }
        }
    }

    *max_value = matrice_valori_maxime[n][capacitate_plasa];

    int c = capacitate_plasa;
    int idx = 0;
    for (int i = n; i > 0; i--) {
        if (keep[i][c]) {
            selected_sizes[idx] = lobsters[i - 1].size;
            selected_values[idx] = lobsters[i - 1].value;
            c -= lobsters[i - 1].size;
            idx++;
        }
    }

    *selected_count = idx;

    for (int i = 0; i <= n; i++) {
        free(matrice_valori_maxime[i]);
        free(keep[i]);
    }
    free(matrice_valori_maxime);
    free(keep);
}

void sort_desc(int *array, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (array[i] < array[j]) {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

int main() {
    FILE *file;
    char filename[20];
    int num_tests, num_lobsters, max_value_range, net_capacity;
    Lobster lobsters[10000];
    int all_net_capacities[8];
    Lobster all_lobsters[8][10000];
    int results[8][3];
    double times[8];

    // Read data from csv files
    for (int i = 1; i <= 8; i++) {
        sprintf(filename, "%d.csv", i);
        file = fopen(filename, "r");
        if (!file) {
            perror("Error opening file");
            return 1;
        }

        fscanf(file, "%d %d %d %d", &num_tests, &num_lobsters, &max_value_range, &net_capacity);
        all_net_capacities[i - 1] = net_capacity;

        for (int j = 0; j < num_lobsters; j++) {
            fscanf(file, "%d %d", &lobsters[j].size, &lobsters[j].value);
            all_lobsters[i - 1][j] = lobsters[j];
        }

        fclose(file);
    }

    // Process each test case
    for (int i = 0; i < 9; i++) {
        clock_t start_time = clock();
        int max_value;
        int selected_sizes[10000];
        int selected_values[10000];
        int selected_count;

        valori_maxime_homari(all_lobsters[i], num_lobsters, all_net_capacities[i], &max_value, selected_sizes, selected_values, &selected_count);
        clock_t end_time = clock();
        double time_elapsed = (double)(end_time - start_time) / CLOCKS_PER_SEC;
        times[i] = time_elapsed;

        results[i][0] = i + 1;
        results[i][1] = max_value;
        results[i][2] = selected_count;

        FILE *result_file = fopen("results_c.txt", "a");
        if (result_file) {
            fprintf(result_file, "Test %d:\n", i + 1);
            fprintf(result_file, "Max Value: %d\n", max_value);
            fprintf(result_file, "Selected Sizes: ");
            for (int j = 0; j < selected_count; j++) {
                fprintf(result_file, "%d ", selected_sizes[j]);
            }
            fprintf(result_file, "\nSelected Values: ");
            for (int j = 0; j < selected_count; j++) {
                fprintf(result_file, "%d ", selected_values[j]);
            }
            fprintf(result_file, "\nTime Elapsed: %f seconds\n\n", time_elapsed);
            fclose(result_file);
        }
    }

    return 0;
}
