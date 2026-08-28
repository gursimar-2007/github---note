#include<stdio.h>
// int main(){
//     int a;
//     int b;
//     printf("enter first side");
//     scanf("%d",&a);
//     printf("enter second side");
//     scanf("%d",&b);
//     int per;
//     per=a*b;
//     printf("the permeter of rectangle is :%d",per);
int main(){
    int n1;
    int n2;
    int n3;
    int cube;
    printf("enter the side 1:");
    scanf("%d",&n1);
    printf("enter the side 2:");
    scanf("%d",&n2);
    printf("enter the side 3:");
    scanf("%d",&n3);
    cube=n1*n2*n3;
    printf("the cube of sides is %d and the adress of the following variables are %d %d %d",cube,&n1,&n2,&n3);
    
    
    return 0;

}