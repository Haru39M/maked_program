#include <stdio.h>
void reverse(int *p, int n)
{
    int *px = p;
    int i;
    int j;
    int tmp;
    for (j=1;j<5;j++)
    {
        //最初から
        px = p;
        //一つの数字を右に持っていく
        for (i = n; i > j; i--)
        {
            //入れ替え
            tmp = *px;
            *px = *(px + 1);
            *(px + 1) = tmp;
            //ずらす
            px++;
        }
    }
}
int main(void)
{
    int num[5] = {1, 2, 3, 4, 5};
    int i;
    printf("before:");
    for (i = 0; i < 5; i++)
    {
        printf("%d ", num[i]);
    }
    printf("\n");
    reverse(num, 5);
    printf("after:");
    for (i = 0; i < 5; i++)
    {
        printf("%d ", num[i]);
    }
    printf("\n");
}