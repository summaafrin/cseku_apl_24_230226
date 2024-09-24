
#include <stdio.h>

int main() {
    int numbers[4];  // Array to hold four integers
    int test_cases;  // Variable to store the number of test cases
    scanf("%d", &test_cases);  // Read the number of test cases

    while (test_cases--) {
        // Read four integers into the numbers array
        for (int i = 0; i < 4; i++) {
            scanf("%d", &numbers[i]);
        }

        int max_value = numbers[0];  // Initialize max_value with the first element
        int count_greater = 0;        // Counter for numbers greater than max_value

        // Traverse the array to count how many numbers are greater than max_value
        for (int i = 0; i < 4; i++) {
            if (max_value < numbers[i]) {
                count_greater++;  // Increment counter if the current number is greater
            }
        }

        printf("%d\n", count_greater);  // Print the count of numbers greater than max_value
    }

    return 0;
}
