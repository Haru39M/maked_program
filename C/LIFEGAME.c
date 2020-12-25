#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#define M 30
#define N 30
int main(void){
	int matrix[M][N];//m*n matrix
	int galaxy[9][9] = {{1,1,0,1,1,1,1,1,1},{1,1,0,1,1,1,1,1,1},{1,1,0,0,0,0,0,0,0},{1,1,0,0,0,0,0,1,1},{1,1,0,0,0,0,0,1,1},{1,1,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1,1},{1,1,1,1,1,1,0,1,1},{1,1,1,1,1,1,0,1,1}};
	int tmp[M][N];
	int i,m,n,seed,times,count = 0;
	int PMX,PMY,L,R,U,D = 0;
	int Dead = 0;
	int Alive = 1;
	char DRAW[2] = {' ','#'};
	//input part
	printf("input random seed\n");
	scanf("%d",&seed);
	srand(seed);
	printf("input times\n");
	scanf("%d",&times);
	//set first random 0 or 1 only once
	for(m=0;m<M;m++){
		for(n=0;n<N;n++){
			matrix[m][n] = rand()%2;//random dead or alive
			printf("%2d",matrix[m][n]);
		}
		printf("\n");
	}

	//set galaxy
	
	for(m=0;m<M;m++){
		for(n=0;n<N;n++){
			matrix[m][n] = 0;
			printf("%2d",matrix[m][n]);
		}
		printf("\n");
	}
	for(m=0;m<9;m++){
		for(n=0;n<9;n++){
			matrix[m+M/2-4][n+N/2-4] = galaxy[m][n];
			printf("%2d",matrix[m][n]);
		}
		printf("\n");
	}

	i=0;
	while(i<times){
		//copy matrix to tmp part
		for(m=0;m<M;m++){
			for(n=0;n<N;n++){
				tmp[m][n] = matrix[m][n];
			}
		}
		//count part
		for(m=0;m<M;m++){
			for(n=0;n<N;n++){
				count = 0;
				L=-1;
				R=1;
				U=-1;
				D=1;
				if(m==0){//leftside
					L = 0;
				}else if(m==M){//rightside
					R = 0;
				}
				if(n==0){//upside
					U = 0;
				}else if(n==N){//downside
					D = 0;
				}
				for(PMX = L;PMX<=R;PMX++){
					for(PMY = U;PMY<=D;PMY++){
						if((PMX==0)&&(PMY==0)){
						}
						else if(matrix[m+PMX][n+PMY]==1){
							count += 1;
						}
					}
				}
				//reloading part
				if(matrix[m][n] == Dead){
					if(count == 3){
						tmp[m][n] = Alive;//born
					}
				}
				else if(matrix[m][n] == Alive){
					if(count <= 1){
						tmp[m][n] = Dead;//dead
					}
					else if(count <= 3){
						tmp[m][n] = Alive;//alive
					}
					else{
						tmp[m][n] = Dead;//dead
					}
				}
			}
		}
		// copy tmp to matrix part
		for(m=0;m<M;m++){
			for(n=0;n<N;n++){
				matrix[m][n] = tmp[m][n];
			}
		}
		//print part
		system("cls");
		printf("time:%d\n",i+1);
		for(m=0;m<M;m++){
			for(n=0;n<N;n++){
				printf("%2c",DRAW[matrix[m][n]]);
			}
			printf("\n");
		}
		printf("\n");
		Sleep(250);
		i+=1;
	}
	return 0;
}