#include <stdio.h>
#define ADULTMONEY 700
#define CHILDMONEY 300
int rental(int adu,int chi){
    int money;
    money = ADULTMONEY*adu+CHILDMONEY*chi;
}
int main(void){
    int adult,child,allmoney;
    printf("Caluculate rental value.\n");
    printf("please input adult value[people]:\n");
    scanf("%d",&adult);
    printf("please input child value[people]:\n");
    scanf("%d",&child);
    printf("adult:%d,child:%d\n",adult,child);
    allmoney = rental(adult,child);
    printf("sum rental value is %d YEN.\n",allmoney);
}0
1
