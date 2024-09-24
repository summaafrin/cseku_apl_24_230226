#include <stdio.h>

int main() {
    int test_cases;  // Variable to store the number of test cases
    scanf("%d", &test_cases);  // Read the number of test cases

    while (test_cases--) {  // Loop for each test case
        int n;  // Variable to store the number of elements in the array
        scanf("%d", &n);  // Read the number of elements

        int arr[n];  // Declare an array to hold the elements
        // Input array elements
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);  // Read each element into the array
        }

        int current_count = 0;  // Counter for consecutive zeros
        int max_consecutive_zeros = 0;  // Variable to track the maximum consecutive zeros

        // Traverse the array to find maximum consecutive zeros
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                current_count = 0;  // Reset the counter if a 1 is encountered
            } else if (arr[i] == 0) {
                current_count++;  // Increment the counter for each consecutive 0
            }

            // Update max_consecutive_zeros if current_count exceeds it
            if (max_consecutive_zeros < current_count) {
                max_consecutive_zeros = current_count;
            }
        }

        printf("%d\n", max_consecutive_zeros);  // Print the maximum number of consecutive zeros
    }

    return 0;  // Return success
}
