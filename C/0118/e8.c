#include <stdio.h>
int are_identical(char *pa, char *pb)
{
    int result = 0;
    while (1)
    {
        if ((*pa == '\0') && (*pb == '\0'))
        {
            result = 1;
            break;
        }
        if (*pa != *pb)
        {
            break;
        }
        
        pa++;
        pb++;
    }

    return result;
}
int main(void)
{
    char wa[100];
    char wb[100];
    int result;
    printf("input a word:\n");
    scanf("%s", wa);
    printf("input another word:\n");
    scanf("%s", wb);
    result = are_identical(wa, wb);
    if (result == 1)
    {
        printf("identical\n");
    }
    else
    {
        printf("different\n");
    }
    return 0;
}