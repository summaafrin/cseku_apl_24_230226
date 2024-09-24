
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max = arr[0];
    for (int i = 0; i < n; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }

    int arr1[n];
    for (int i = 0; i < n; i++) {
        arr1[i] = max - arr[i];
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr1[i];
    }

    printf("%d\n", sum);

    return 0;
}
