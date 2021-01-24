/*
  学籍番号：12071149
  氏名：Haruto Wakayama
*/

#include <stdio.h>
#include <stdlib.h>

/* 勝率を計算する関数 */
double winning_rate(int *u, int *c)
{
  double rate = 0;
  double times = 0; //じゃんけんの回数
  /* 関数の中身を書くこと */
  while(1){
    if(*u == -1){
      break;
    }
    if ((*u + 1) % 3 == *c)
    { //ユーザーの手に１足して３で割った余りがコンピュータの手と同じなら勝ち
      rate += 1;
    }
    //次の手を見る
    u++;
    c++;
    times += 1;
  }

  rate /= times;//じゃんけんの回数で割る。
  return rate;
}

/* 結果をファイル出力する関数．絶対に変更しないこと！ */
void output(int *u, int *c, double r)
{
  FILE *f;
  f = fopen("output.txt", "w");
  for (; *u >= 0 && *u <= 2; u++, c++)
    fprintf(f, "%d %d\n", *u, *c);
  fprintf(f, "%f\n", r);
  fclose(f);
}

/* メイン関数 */
int main(void)
{

  /* 必要な変数があればここで宣言*/

  int hist_user[100] = {-1};                       /* ユーザの手を記憶 */
  int hist_comp[100] = {-1};                       /* コンピュータの手を記憶 */
  int i;                                           /* ループ変数 */
  char hands[3][100] = {"グー", "チョキ", "パー"}; //0グー1チョキ2パー
  /* 100回繰り返し．0~2以外の数字が入力されたらbreak */
  for (i = 0; i < 100; i++)
  {
    printf("グー(0),チョキ(1),パー(2)?\n");
    scanf("%d", &hist_user[i]);
    if ((hist_user[i] < 0) || (2 < hist_user[i]))
    { //0~2以外の数字が入力されたらbreak
      hist_user[i] = -1;
      break;
    }
    hist_comp[i] = rand() % 3;                                                                //コンピュータの手をランダムに入れる
    printf("%d:%s(you) vs. %s(computer)\n", i + 1, hands[hist_user[i]], hands[hist_comp[i]]); //表示
  }

  /* 
     以降は変更の必要なし 
  */

  /* 結果の表示 */
  printf("勝率 = %.3f\n",
         winning_rate(hist_user, hist_comp));

  /* 結果のファイル出力用．絶対に編集しないこと！ */
  output(hist_user, hist_comp, winning_rate(hist_user, hist_comp));

  return 0;
}
