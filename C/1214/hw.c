#include <stdio.h>
int main(void)
{
    int i = 0;
    int k = 0;
    int size = 0;
    int inum = 0;
    int syou = 0;
    int amari = 0;
    int end = 0;
    do
    {
        printf("単語帳の大きさ？");
        scanf("%d", &size);
    } while (!(size < 101));
    int num[size];
    do
    {
        printf("%d番目の数字？", i + 1);
        scanf("%d", &num[i]);
        i++;
    } while (i < size);

    for (i = 0; i < size; i++)
    {
        printf("%d番目の数字:%d\n", i + 1, num[i]);
    }

    //入力　しりとり開始
    do
    {
        printf("数値？");
        scanf("%d", &inum);

        //インプットされた数字の末尾のケタを取り出す
        amari = inum;
        do
        {
            amari %= 10;
        } while (amari > 9);
        //printf("%d\n", amari);

        //数字の先頭のケタを取り出し、判定
        for (k = 0; k < size; k++)
        {
            //取り出し
            syou = num[k];
            do
            {
                syou /= 10;
            } while (syou > 9);
            //printf("%d\n", syou);

            //判定
            if (amari == syou)
            {
                printf("%d -> %d", inum, num[k]);
                break;
            }
            else if (k == size - 1) //終端ならエンドをオンに
            {
                printf("You Win!");
                end = 1;
            }
        }

    } while (end == 0);

    return 0;
}