#include<stdio.h>
double calc(int weight,int height);
void hantei(double bmi);

int main(void){
	int weight,height;
	double bmi;
	do{
		printf("input weight,height\n");
		scanf("%d,%d",&weight,&height);
	}while(!((weight>0)&&(height>0)));
	bmi = calc(weight,height);
	printf("BMI = %.1f",bmi);
	hantei(bmi);
	
	return 0;
}

double calc(int weight,int height){
	double bmi;
	bmi = (double)weight/(((double)height/100)*((double)height/100));
	return bmi;
}

void hantei(double bmi){
	if(bmi<25){
	printf("(標準です)\n",bmi);
		if(bmi<18.5){
			printf("(やせ型です)\n",bmi);
		}
	}else{
		printf("(肥満です)\n",bmi);
	}
}
