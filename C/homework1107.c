#include <stdio.h>
int main(void){
    int h=0;//8回繰り返すfor文の変数
    int i=0;
    int k=0;
    int curlist[20];//現在の配列
    int nexlist[20];//次の配列
    char firlist[20];//文字列

    //配列を初期化
    for(i=0;i<20;i++){
        curlist[i] = 0;
        nexlist[i] = 0;
        //printf("first:%d\n",curlist[i]);
    }
    curlist[10] = 1;

    //最初の配列を入力
    /*
    i = 0;
    while(i<20){
        scanf("%d",&curlist[i]);
        printf("%d:%d\n",i,curlist[i]);
        i++;
    }
    scanf("%s",firlist[20]);
    printf("%s\n",firlist[20]);
    */

    //変換
    for(h=0;h<9;h++){
        i = 0;
        while(i<20-2){
            for(k=i;k<i+3;k++){
                if(curlist[k]==0){
                    if(curlist[k+1]==0){
                        if(curlist[k+2]==0){//000
                            nexlist[k+1]=0;
                        }
                        else if(curlist[k+2]==1){//001
                            nexlist[k+1]=1;
                        }
                    }
                    else if(curlist[k+1]==1){
                        if(curlist[k+2]==0){//010
                            nexlist[k+1]=0;
                        }
                        else if(curlist[k+2]==1){//011
                            nexlist[k+1]=1;
                        }
                    }
                }
                else if(curlist[k]==1){
                    if(curlist[k+1]==0){
                        if(curlist[k+2]==0){//100
                            nexlist[k+1]=1;
                        }
                        else if(curlist[k+2]==1){//101
                            nexlist[k+1]=0;
                        }
                    }
                    else if(curlist[k+1]==1){
                        if(curlist[k+2]==0){//110
                            nexlist[k+1]=1;
                        }
                        else if(curlist[k+2]==1){//111
                            nexlist[k+1]=0;
                        }
                    }
                }
            }
            i++;
        }
        //出力
        /*
        i = 0;
        while (i<20-2)
        {
            for(k=i;k<i+3;k++){
                printf("curlist[%d]:%d  nexlist[%d]:%d\n",k,curlist[k],k,nexlist[k]);
            }
            printf("\n");
            i++;
        }*/

        for(i=0;i<20;i++){
                //printf("curlist[%d]:%d  nexlist[%d]:%d\n",i,curlist[i],i,nexlist[i]);
                printf("%d",curlist[i]);
        }
        printf("\n");
        /*for(i=0;i<20;i++){
                printf("%d",nexlist[i]);
        }
        printf("\n");*/

        //変換後の配列をもとの配列にコピー
        for(i=0;i<20;i++){
                curlist[i]=nexlist[i];
        }
    }
}