#include <stdio.h>
int main(void){
    int x=0;
    int y=0;
    int result=0;
    
    printf("input:x>>");
    scanf("%d",&x);
    printf("input:y>>");
    scanf("%d",&y);
    result = power(x,y);
    printf("%d",result);
    return 0;
}
int power(int x,int y){
    int i;
    int result=x;
    for(i=0;i<y-1;i++){
        result = result*x;
    }
    return result;
}