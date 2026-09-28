#include<stdio.h>


int i=1;
int *p=&i;
int *q;
q=p;
*q=5;
printf("the answer is %d",*p);