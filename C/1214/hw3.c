#include <stdio.h>
#include <math.h>
int main(void)
{
    int num[100] = {0};
    int *p = num;//配列の最初のアドレスをポインタ変数pに渡す
    int i;
    int size = 0;//単語帳の大きさ
    int inum = 0;//インプットナンバー
    int saizyoui = 0;//最上位ケタ
    int matsubi = 0;//最下位ケタ
    do
    {
        printf("単語帳の大きさ？ \n");
        scanf("%d", &size);
    } while (!(size < 101));
    num[size] = -1;

    i = 1;
    do
    {
        printf("%d番目の数字？ \n", i);
        scanf("%d", p);
        i++;
        p++;
    } while (*p != -1);

    i = 1;
    for (p = num; *p != -1; p++)
    {
        printf("%d番目の数字:%d\n", i, *p);
        i++;
    }

    //入力　しりとり開始
    do
    {
        printf("数値？ \n");
        scanf("%d", &inum);

        //インプットされた数字の末尾のケタを取り出す
        matsubi = inum%10;

        //数字の先頭のケタを取り出し、判定
        for (p = num; *p != -1; p++)
        {
            //取り出し
            i = 0;
            do
            {
                saizyoui = *p/pow(10,i);
                i++;
            } while (saizyoui > 9);

            //判定
            if (matsubi == saizyoui)
            {
                printf("%d -> %d \n", inum, *p);
                break;
            }
        }
    } while (*p != -1);
    printf("%d -> なし\n",inum);
    printf("You Win! \n");

    return 0;
}