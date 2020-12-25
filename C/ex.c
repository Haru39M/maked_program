#include <stdio.h>
#define NUM 5
/*
int main(void){
	int i,k,tmp = 0;
	int score[5];
	score[0] = 35;
	score[1] = 65;
	score[2] = 78;
	score[3] = 46;
	score[4] = 10;

	for(i=0;i<4;i++){
		for(k=i+1;k<5;k++){
			if(score[i]<score[k]){
				tmp = score[i];
				score[i] = score[k];
				score[k] = tmp;
			}
		}
	}
	for(i=0;i<5;i++){
		printf("%d\n",score[i]);
	}
}
int main(void){
	int test[NUM];
	int tmp;
	int i,j,s,t;
	
	printf("input %d people's score\n",NUM);
	for(i=0;i<NUM;i++){
		scanf("%d",&test[i]);
	}
	for(s=0;s<NUM-1;s++){
		for(t=s+1;t<NUM;t++){
			if(test[t]>test[s]){
				tmp = test[t];
				test[t] = test[s];
				test[s] = tmp;
			}
		}
	}
	for(j=0;j<NUM;j++){
		printf("number %d people's score is %d\n",j+1,test[j]);
	}
	return 0;
}
int main(void){
	int sum[3];
	int price[3];
	int num[3];
	int i,allsum=0;
	price[0] = 1000;
	price[1] = 2000;
	price[2] = 3000;
	
	num[0] = 2;
	num[1] = 1;
	num[2] = 2;
	
	for(i=0;i<3;i++){
		sum[i] = price[i]*num[i];
		printf("%d\n",sum[i]);
		allsum += sum[i];
	}
	printf("%d\n",allsum);
	
	return 0;
}
#define PNUM 5
int main(void){
	int i=0;
	int sum=0;
	int weight[PNUM] = {50,49,100,70,99};
	int hist[PNUM] = {0,0,0,0,0};
	
	for(i=0;i<PNUM;i++){
		printf("%d:%d\n",i,weight[i]);
		sum += weight[i];
		if(weight[i]>99){
			hist[0] += 1;
		}else if(weight[i]>49){
			hist[1] += 1;
		}else if(weight[i]>-1){
			hist[2] += 1;
		}
	}
	printf("%d\n",sum);
	printf("%f\n",(double)sum/5);
	
	for(i=2;i>-1;i--){
		printf("%d\n",hist[i]);
	}
	
	return 0;
}
int main(void){
	char str[] = "hello";
	int i;
	
	printf("Hello\n");
	
	for(i=0;str[i]!='\0';i++){
		printf("%c*",str[i]);
	}
	printf("\n");
	return 0;
}
int main(void){
	char str[10];
	int i,times = 0;
	printf("Input str:\n");
	//input
	scanf("%s",str);
		
	//calc
	for(i=0;str[i]!='\0';i++){
		printf("%c\n",str[i]);
		if(str[i] == 'a'){
			times += 1;
		}
	}
	//output
	printf("%d\n",times);
	return 0;
}*/
int main(void){
	int x[2][2] = {{1,2},{3,4}};
	int y[2][2] = {{5,6},{7,8}};
	int sum[2][2];
	int i,j = 0;
	
	for(i=0;i<2;i++){	
		for(j=0;j<2;j++){
			sum[i][j] = x[i][j]+y[i][j];
			printf("%2d",sum[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}

































