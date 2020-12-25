#include <stdio.h>
void calc(int *p);
int main(void){
    int day = 0;
    int kabu[100] = {0};
    do
    {
        printf("%d日目の株価？\n",day+1);
        scanf("%d",&kabu[day]);
        day++;
    } while (kabu[day-1] > -1);
    printf("Stock Price:\n");
    day = 0;
    do
    {
        printf("Day %d: %d\n",day+1,kabu[day]);
        day++;
    } while (kabu[day] > -1);

    calc(kabu);
}
void calc(int *p){
    int day = 0;
    int *q = p;
    int bought = -1;
    int earn = 0;
    int cost = 0;
    while (*q > -1)
    {
        if ((bought < 0)&&(*q < *(q+1)))//もし明日のほうが高ければ
        {
            printf("buy: day %d at %d\n",day+1,*q);
            bought *= -1;
            cost = *q;
        }
        else if ((bought > 0)&&(*q > *(q+1))){
            printf("sell: day %d at %d\n",day+1,*q);
            bought *= -1;
            earn += *q-cost;
        }
        q++;
        day++;
    }
    
    printf("Total Earning = %d",earn);
}