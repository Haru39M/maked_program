//12071149 Haruto Wakayama
#include <stdio.h>
int main(void){
    int list[5][5] = {{3,6,10,4,2},{5,12,9,6,7},{4,7,3,2,1},{11,9,8,3,4},{7,4,2,5,8}};//m*n list
    int tmp[5][5] = {{3,6,10,4,2},{5,12,9,6,7},{4,7,3,2,1},{11,9,8,3,4},{7,4,2,5,8}};
    int PMX=0;
    int PMY=0;
    int x=0;
    int y=0;
    int sum=0;
    int ave=0;

    printf("input image\n");
    for(x=0;x<5;x++){
        for(y=0;y<5;y++){
            printf("%4d",list[x][y]);
        }
        printf("\n");
    }
    printf("\n");


    //初期化
    x=1;
    y=1;
    for(x=1;x<4;x++){
        for(y=1;y<4;y++){
            for(PMX = -1;PMX<2;PMX++){
                for(PMY=-1;PMY<2;PMY++){
                    sum += list[x+PMX][y+PMY];
                }
            }
            ave = sum/9;
            tmp[x][y]=ave;
            sum = 0;
        }
    }
    
    printf("output image\n");
    for(x=0;x<5;x++){
        for(y=0;y<5;y++){
            printf("%4d",tmp[x][y]);
        }
        printf("\n");
    }
}