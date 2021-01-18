#include <stdio.h>
int main(void){
    char *name[100][100];
    int height[100] = {0};
    int n=0;
    int i=0;
    int count_s=0;
    int count_m=0;
    int count_l=0;
    int count_xl=0;
    printf("人数？\n");
    scanf("%d",&n);
    //printf("%d",n);

    //input
    do
    {
        printf("%d番目: 名前 身長(cm)?\n",i+1);
        scanf("%s %d",&name[i],&height[i]);

        //judge
        if(height[i] <= 165){
            count_s += 1;
        }else if(height[i] <= 175){
            count_m += 1;
        }else if(height[i] <= 180){
            count_l += 1;
        }else{
            count_xl += 1;
        }

        i++;
    } while (i<n);

    //print
    for(i=0;i<n;i++){
        printf("[%d] %s = %d cm\n",i+1,name[i],height[i]);
    }

    printf("Size:S (%d 人)\n",count_s);
    for(i=0;i<n;i++){
        if(height[i] <= 165){
            printf("%s ,",name[i]);
        }
    }
    printf("\n");
    printf("Size:M (%d 人)\n",count_m);
    for(i=0;i<n;i++){
        if((165 < height[i])&&(height[i] <= 175)){
            printf("%s ,",name[i]);
        }
    }
    printf("\n");
    printf("Size:L (%d 人)\n",count_l);
    for(i=0;i<n;i++){
        if((175 < height[i])&&(height[i] <= 180)){
            printf("%s ,",name[i]);
        }
    }
    printf("\n");
    printf("Size:XL (%d 人)\n",count_xl);
    for(i=0;i<n;i++){
        if(height[i] > 180){
            printf("%s ,",name[i]);
        }
    }
    printf("\n");
    return 0;
}