#include <stdio.h>
#include <math.h>
int main(void){
    int num[100] = {0};
    int *p = num; //リストのアドレス変数
    int i;
    int k = 0;
    int size = 0;
    int inum = 0;
    int saizyoui = 0;
    int amari = 0;
    int end = 0;

    printf("単語帳の大きさ？");
    scanf("%d", size);
    num[size] = -1;
    printf("%d",size);
    
    i=0;
    do{
        printf("%d番目の数字？", i + 1);
        scanf("%d", &k);
        i++;
    } while (i < size);

    //     for (i = 0; i < size; i++)
    //     {
    //         printf("%d番目の数字:%d\n", i + 1, num[i]);
    //     }

    //     //入力　しりとり開始
    //     do
    //     {
    //         printf("数値？");
    //         scanf("%d", &inum);

    //         //インプットされた数字の末尾のケタを取り出す
    //         amari = inum;
    //         i = 0;
    //         do
    //         {
    //             amari %= 10;
    //         } while (amari > 9);
    //         //printf("%d\n", amari);

    //         //数字の先頭のケタを取り出し、判定
    //         for (k = 0; k < size; k++)
    //         {
    //             //取り出し
    //             saizyoui = num[k];
    //             do
    //             {
    //                 saizyoui /= 10;
    //             } while (saizyoui > 9);
    //             //printf("%d\n", saizyoui);

    //             //判定
    //             if (amari == saizyoui)
    //             {
    //                 printf("%d -> %d\n", inum, num[k]);
    //                 break;
    //             }
    //             else if (k == size - 1) //終端ならエンドをオンに
    //             {
    //                 printf("You Win!\n");
    //                 end = 1;
    //             }
    //         }

    //     } while (end == 0);
    return 0;
}