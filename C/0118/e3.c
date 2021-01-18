#include <stdio.h>
void set_zero(int *p,int n){
    int i;
    for(i=0;i<n;i++){
        *p = 0;
        p++;
    }
}
int main(void){
    int num[5] = {1,2,3,4,5};
    int i;
    printf("before:");
    for(i=0;i<5;i++){
        printf("%d ",num[i]);
    }
    printf("\n");
    set_zero(num,5);
    printf("after:");
    for(i=0;i<5;i++){
        printf("%d ",num[i]);
    }
    printf("\n");
    
}