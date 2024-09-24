
#include <stdio.h>

int main() {
    int test_cases;  // Variable to store the number of test cases
    scanf("%d", &test_cases);  // Read the number of test cases

    // Loop through each test case
    for (int t = 0; t < test_cases; t++) {
        int input_number;  // Variable to store the current number
        scanf("%d", &input_number);  // Read the input number

        // Check if the number is divisible by 7
        if (input_number % 7 == 0) {
            printf("%d\n", input_number);  // Print the number if divisible by 7
        }
        // Special case for numbers greater than or equal to 990 and not divisible by 7
        else if (input_number >= 990 && input_number % 7 != 0) {
            printf("%d\n", 994);  // Print 994 as the closest number divisible by 7
        }
        else {
            // Round the number down to the nearest multiple of 10
            input_number = (input_number / 10) * 10;

            // Find the nearest number divisible by 7
            for (int candidate = input_number; candidate <= input_number + 7; candidate++) {
                if (candidate % 7 == 0) {
                    printf("%d\n", candidate);  // Print the nearest number divisible by 7
                    break;
                }
            }
        }
    }

    return 0;  // Return success
}
