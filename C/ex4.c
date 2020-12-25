#include <stdio.h>
int count_baisu(int a1,int b1,int k1){
    int kosuu1 = 0;
    for(int num = a1;num <= b1;num++){
        if(num % k1 ==0){
            kosuu1 += 1;
        }
    }
    return kosuu1;
}
int main(){
    int a,b,k,kosuu = 0;
    printf("いくつから？:");
    scanf("%d",&a);
    printf("いくつまで？:");
    scanf("%d",&b);
    printf("何の倍数？:");
    scanf("%d",&k);
    kosuu = count_baisu(a,b,k);
    printf("%dから%dまでに%dの倍数は%d個ある",a,b,k,kosuu);
    return 0;
}
