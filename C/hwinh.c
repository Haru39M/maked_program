#include <stdio.h>
#define PNUM 10
int main(void){
	int score[PNUM] = {89,90,50,49,100,9,70,69,79,80};
	//int index[PNUM];
	int hist[PNUM+1];
	int i,k,tmp=0;
	for(i=0;i<PNUM-1;i++){
		for(k=i+1;k<PNUM;k++){
			if(score[i]>score[k]){
				tmp = score[i];
				score[i] = score[k];
				score[k] = tmp;
			}
		}
	}
	for(i=1;i<PNUM+1;i++){
	/*
		index[i-1] = (int)(score[i-1]/10);
		if(index[i-1] > 1){
			index[i-1] = 0;
		}
		printf("%d %d %d\n",score[i-1],index[i-1],hist[i-1]);
	}*/
		if(score[i]>99){
			hist[11]+=1;
		}else if(score[i]>99){
			hist[10]+=1;
		}else if(score[i]>89){
			hist[9]+=1;
		}else if(score[i]>79){
			hist[8]+=1;
		}else if(score[i]>69){
			hist[7]+=1;
		}else if(score[i]>59){
			hist[6]+=1;
		}else if(score[i]>49){
			hist[5]+=1;
		}else if(score[i]>39){
			hist[4]+=1;
		}else if(score[i]>29){
			hist[3]+=1;
		}else if(score[i]>19){
			hist[2]+=1;
		}else if(score[i]>9){
			hist[1]+=1;
		}else if(score[i]>-1){
			hist[0]+=1;
		}
		for(i=0;i<12;i++){
			printf("%d-%d+9:%d",i,i,hist[i]);
		}
	}
}
