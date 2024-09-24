
#include <stdio.h>

int main() {
    int arr[4];
    int t;
    scanf("%d", &t);

    while (t--) {
        for (int i = 0; i < 4; i++) {
            scanf("%d", &arr[i]);
        }

        int max = arr[0];
        int cnt = 0;

        for (int i = 0; i < 4; i++) {
            if (max < arr[i]) {
                cnt++;
            }
        }

        printf("%d\n", cnt);
    }

    return 0;
}
