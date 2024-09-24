
#include <stdio.h>

int main() {
    int test_cases;
    scanf("%d", &test_cases);  // Read number of test cases

    while (test_cases--) {
        int n;
        scanf("%d", &n);  // Read number of elements in the array

        int ar[n];

        // Input array elements
        for (int i = 0; i < n; i++) {
            scanf("%d", &ar[i]);
        }

        int current_length = 0;
        int max_length = 0;

        // Traverse the array to find maximum consecutive zeros
        for (int i = 0; i < n; i++) {
            if (ar[i] == 1) {
                current_length = 0;  // Reset the count if encounter 1
            } else if (ar[i] == 0) {
                current_length++;  // Increment count if encounter 0
            }

            // Update max_length if current length of consecutive zeros is greater
            if (max_length < current_length) {
                max_length = current_length;
            }
        }

        printf("%d\n", max_length);  // Print the maximum consecutive zeros length
    }

    return 0;
}
