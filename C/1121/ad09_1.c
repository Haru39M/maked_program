#include <stdio.h>
int num;
void pri(num){
  printf("%d台目の車を買いに行きます。\n",num);
  printf("通帳をATMに入れます。\n");
  printf("暗証番号を入力します。\n");
  printf("金額を指定します。\n");
  printf("お金を受け取ります。\n");
  printf("お金と通帳を確認します。\n");
  printf("車を買いました。\n");
  printf("\n");
}

int main(void){
  for(num=1;num<4;num++){
    pri(num);
  }
  return (0);

}