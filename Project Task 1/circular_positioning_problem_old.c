#include <stdio.h>

int main() {
    int a;
    scanf("%d",&a);
    while(a--){
        int n;
        scanf("%d",&n);
        int ar[n];
        for(int i=0;i<n;i++){
            scanf("%d",&ar[i]);
        }
        int count=0,max=0;
        for(int i=0;i<n;i++){
            if(ar[i]==1){
                count=0;
            }
            else if(ar[i]==0){
                count++;
            }
            if(max<count){
                max=count;
            }
        }
        printf("%d\n",max);
    }

    return 0;
}
