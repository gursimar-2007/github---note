#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i; j++)
        {
            printf("  ");
        }
        for (int k = 1; k <= 2*i-1; k++)
        {
            if(i==n ||k==1 || k==i*2-1)
                printf("* ");
            else
                printf("  ");
        }
        printf("\n");
    }

    // for(int i=n-1;i>=0;i--){
    //     for(int j=0;j<=n-i;j++){
    //         printf(" ");
    //     }
    // for(int k=0;k<=i;k++){
    //     printf("* ");
    // }
    // printf("\n");
    // }

    return 0;
}