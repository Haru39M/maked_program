#include <stdio.h>
int calc_remainder(int a,int b,int *syou);

int main(void){
	int a,b,syou,amari;
	
	printf("calculate a/b.\n");
	
	printf("a = ?:");
	scanf("%d",&a);
	printf("%d putted address:%p \n",a,&a);
	
	printf("b = ?:");
	scanf("%d",&b);
	printf("%d putted address:%p \n",b,&b);
	
	amari = calc_remainder(a,b,&syou);
	
	printf("%d / %d = %d, amari is %d \n",a,b,syou,amari);
	
	return 0;
}

int calc_remainder(int a,int b,int *syou){
	int amari;
	*syou = a/b;
	amari = a%b;
	return amari;
}
