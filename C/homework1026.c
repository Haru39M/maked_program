//10271149 Haruto Wakayama
#include <stdio.h>
#include <math.h>
int main(void){
	int i;//フィボナッチ数列の項を求める回数

	//フィボナッチ数列の３項
	int fib0 = 0;//２つ前の項
	int fib1 = 1;//一つ前の項
	int fib2 = 0;//現在の項
	
	int num = 0;//フィボナッチ数列の項数
	double golden_ratio = 0e-10;//黄金比
	double golden_near = 0e-10;
	
	do{//numが2以上40以下でないなら繰り返す
		printf("Input num(2<=num<=40)?:");
		scanf("%d",&num);
		printf("Your input number --> %d \n",num);
	}while(!((2 <= num)&&(num <= 40)));
	
	//calc
	printf("F(0) = %d \n",fib0);
	printf("F(1) = %d \n",fib1);
	for(i=2;i<num;i++){
		fib2 = fib0 + fib1;
		printf("F(%d) : F(%d) + F(%d) --> %d + %d = %d  ",i,i-1,i-2,fib0,fib1,fib2);//フィボナッチ数の出力
		
		golden_near = (double)fib2/(double)fib1;
		printf("Near_Golden_Ratio : %.10lf \n",golden_near);//黄金比の近似値の出力
		
		//項を進める
		fib0 = fib1;
		fib1 = fib2;
	}

	printf("*****************Result******************\n");
	golden_ratio = (1+sqrt(5))/2;//黄金比を計算
	printf("Golden_Ratio : %.10f \n",golden_ratio);//出力
	printf("Near_Golden_Ratio : %.10lf \n",golden_near);//黄金比の近似値の出力

	return 0;
}
