#include <stdio.h>
void nullify(char *p)
{
    *p = '\0';
}
int main(void)
{
    char str[] = "test";
    char *p;

    printf("before:\n");
    printf("str = ");
    p = str;
    while (*p != '\0')
    {
        printf("%c", *p);
        p++;
    }
    printf("\n");
    nullify(str);

    printf("after:\n");
    printf("str = ");
    p = str;
    while (*p != '\0')
    {
        printf("%c", *p);
        p++;
    }
    printf("\n");
    return 0;
}