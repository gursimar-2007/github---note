// #include<stdio.h>
// void main(){
//     int a;
//     printf("enter no");
//     scanf("%d",&a);
//     if(a%3==0){
    //         printf("this number is divisible");
    //     }else{
        //         printf("the number is not divisible");
        //     }
        
        // }
#include <stdio.h>

int main()
{
    int a[10],sz,key,i;

    printf("Entr size of array: ");
    scanf("%d", &sz);

    printf("Entr arr element : ");
    for(i = 0;i<sz;i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Enter key: ");
    scanf("%d", &key);

    for(i = 0; i < sz; i++)
    {
        if(a[i] == key)
        {
            printf("indices are %d ", i);
        }
    }

    return 0;
}