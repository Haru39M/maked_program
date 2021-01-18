#include <stdio.h>
#define NUM 5
#define LEN 100
int main(void){
    char c;
    char stations[NUM][LEN] = {"mikage","kobe","okamoto","rokko","ojikoen"};
    int i=0;
    char *j;
    int count[NUM]={0};
    printf("input a character:\n");
    scanf("%c",&c);
    for(i=0;i<NUM;i++){
        for(j=stations[i];*j!='\0';j++){
            if(*j == c){
                count[i] += 1;
            }
        }
    }
    for(i=0;i<NUM;i++){
        printf("%s : ",stations[i]);
        printf("%d\n",count[i]);
    }
    
    return 0;
}