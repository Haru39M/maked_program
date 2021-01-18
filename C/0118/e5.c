#include <stdio.h>
void delete (int *p, int n)
{
    while (*p != -1)
    {
        if (*p == n)
        {
            for (;*p!=-1;p++)
            {
                *p = *(p + 1);
            }
            break;
        }
        else
        {
            p++;
        }
    }
}
int main(void)
{
    int i;
    int n;
    int num[6] = {5, 2, 7, 9, 6, -1};
    printf("value to delete:\n");
    scanf("%d", &n);

    printf("before:");
    for (i = 0; num[i] != -1; i++)
    {
        printf("%d ", num[i]);
    }
    printf("\n");
    delete (num, n);
    printf("after:");
    for (i = 0; num[i] != -1; i++)
    {
        printf("%d ", num[i]);
    }
    printf("\n");

    return 0;
}