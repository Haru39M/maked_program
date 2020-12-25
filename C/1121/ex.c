#include <stdio.h>
int i;

/* void buy(void){
    printf("Hello C World!\n");
} */

/* void buy(int x){
    printf("%d 万円の車を買いました\n",x);
} */

/* void pri1(int num){
    printf("Your student number is %d\n",num);
} */

/* void buy(int kakaku1,int kakaku2){
    printf("%d %d\n",kakaku1,kakaku2);
} */

/* void birth(int M,int D){
    printf("Your birth day is %d/%d\n",M,D);
} */

/* int comp(int x,int y){
    if(x<y){
        printf("%d is bigger than %d\n",y,x);
    }else if(y<x){
        printf("%d is bigger than %d\n",x,y);
    }else{
        printf("same value\n");
    }
} */

/* int powfun(int x,int y){
    int num=x;
    for(i=0;i<y-1;i++){
        num = num*x;
    }

    printf("%d",num);
} */

double area(double x,double y){
    double area;
    area = x*y;
    return area;
}

int main(void){
    double num1,num2,AREA;
    scanf("%lf",&num1);
    scanf("%lf",&num2);
    AREA = area(num1,num2);
    printf("area is %f",AREA);
    return 0;
}