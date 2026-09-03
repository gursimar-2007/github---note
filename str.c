#include<stdio.h>
#include<string.h>
int main(){
    char str1[]="fateh";
    char str2[]=" sir";
    printf("the length of the characters is %d\n",strlen(str));
    printf("the REVERSE of the characters is %s\n",strrev(str));
    printf("THE LOWERCASE FORMAT OF THIS STRING IS=%s\n",strlwr(str));
    printf("THE UPPERCASE FORMAT OF THIS STRING IS=%s\n",strupr(str));
    strcpy(str2,str1);
    printf("copied string is %s",str2);
    strcat(str1,str2);
    printf("concated string =%s",str1);
    return 0;
}
