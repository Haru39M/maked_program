/*12071149 Haruto Wakayama*/
#include <stdio.h>
int main(void){
    int Nmax = 0;//上限の項数
    int N = 2;//項数
    
    int num0 = 0;
    int num1 = 1;
    int num2 = 0;
    
    do{
        printf("Input num(2<=num<=20)?: \n");
        scanf("%d",&Nmax);
        printf("Your input number --> %d \n",Nmax);
    }while(!((Nmax >= 2)&&(Nmax <= 20)));
    
    printf("F(0) = 0 \n");
    printf("F(1) = 1 \n");
    
    do{
    
        num2 = num0 + num1;
    
        num0 = num1;
        num1 = num2;
    
        printf("F(%d):F(%d) + F(%d) --> %d + %d = %d\n",N,N-1,N-2,num0,num1,num2);
    
        N += 1;
    }while(N <= Nmax);
    
    return 0;
}
