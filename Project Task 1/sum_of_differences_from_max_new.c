
#include <stdio.h>

int main() {
    int num_elements;  // Variable to store the number of elements in the array
    scanf("%d", &num_elements);  // Read the number of elements

    int arr[num_elements];  // Array to hold the input elements
    // Input array elements
    for (int i = 0; i < num_elements; i++) {
        scanf("%d", &arr[i]);  // Read each element into the array
    }

    int max_value = arr[0];  // Initialize max_value with the first element
    // Find the maximum value in the array
    for (int i = 0; i < num_elements; i++) {
        if (max_value < arr[i]) {
            max_value = arr[i];  // Update max_value if a larger element is found
        }
    }

    int difference_array[num_elements];  // Array to store the differences
    // Calculate the differences between max_value and each element
    for (int i = 0; i < num_elements; i++) {
        difference_array[i] = max_value - arr[i];  // Compute the difference
    }

    int total_difference = 0;  // Variable to store the sum of differences
    // Calculate the sum of the differences
    for (int i = 0; i < num_elements; i++) {
        total_difference += difference_array[i];  // Accumulate the total difference
    }

    printf("%d\n", total_difference);  // Print the total difference

    return 0;  // Return success
}
