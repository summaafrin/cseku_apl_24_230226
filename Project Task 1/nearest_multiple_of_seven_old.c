
#include<stdio.h>
int main()
{

    int n,t;
    scanf("%d",&n);
    for(t=0; t<n; t++)
    {
        int x,n;
        scanf("%d",&x);
        if(x%7==0)
        {
            printf("%d\n",x);
        }
        else if(x>=990 && x%7!=0)
        {
            printf("%d\n",994);
        }
        else
        {
            x=x/10;
            x=x*10;
            for(n=x; n<=x+7; n++)
            {
                if(n%7==0)
                {
                    printf("%d\n",n);
                    break;
                }
            }
        }


    }
    return 0;




}
