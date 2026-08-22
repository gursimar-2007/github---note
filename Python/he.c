#include <stdio.h>
int main()
{
    int number;
    int n;
    int key;
    int is_found = 0;
    printf("your number:");
    scanf("%d", &number);
    printf("your number you wanna find:");
    scanf("%d", &key);
    n = number;
    while (n > 0)
    {
        int remainder = n % 10;
        if (key == remainder)
        {
            is_found = 1;
            break;
        }
        n = n / 10;
    }
    if (is_found)
    {
        printf("found");
    }
    else
    {
        printf("not found");
    }
    return 0;
}
