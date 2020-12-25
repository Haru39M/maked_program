#include <stdio.h>
int main(void){
    double timeA;
    double timeB;
    double timeAB;
    printf("Aさんが１人で仕事をした場合、かかる時間:");
    scanf("%lf",&timeA);
    
    printf("Aさんが１人で仕事をした場合、かかる時間:");
    scanf("%lf",&timeB);
    
    timeAB = timeA*timeB/(timeA+timeB);
    
    printf("２人で手分けした場合：%f時間で終わります \n",timeAB);
    
    return 0;
}
