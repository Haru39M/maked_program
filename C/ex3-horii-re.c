#include <stdio.h>
int main(){
    int youbi = 0;
    int matsu = 0;

    printf("一日の曜日を入力(日曜:0～土曜:6)");
    scanf("%d",&youbi);
    printf("末日を入力:");
    scanf("%d",&matsu);

    printf("Su ");
    printf("Mo ");
    printf("Tu ");
    printf("We ");
    printf("Th ");
    printf("Fr ");
    printf("Sa ");
    printf("\n");

    for(int day = 1;day <= matsu;day++){
        if(day < 10){
            printf(" ");
        }
        printf("%3d",day);
        youbi += 1;
        if(youbi == 7){
            printf("\n");
            youbi = 0;
        }
    }
    printf("\n");
    return 0;
}
