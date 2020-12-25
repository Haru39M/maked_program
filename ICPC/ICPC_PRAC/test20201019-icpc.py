n,m = list(map(int,input().split(" ")))#n生徒数m科目
p = [0]*m#初期化
Num_n = 0 #生徒番号
Num_m = 0 #科目番号
sum = 0
print(p)
#p[科目番号][生徒番号]であることに注意
for i in range(m):
    p[i] = list(map(int,input().split(" ")))
print(p)

for i in range(n):#生徒数だけ繰り返す
    for j in range(m):#科目数だけ繰り返す
        sum += p[Num_m][Num_n]#合計点数に追加
        print("p["+str(Num_m)+"]["+str(Num_n)+"]="+str(sum))
        Num_m += 1#次の科目へ
    sum = 0#合計点数を初期化
    Num_n += 1#次の生徒へ
"""while i < 3:
    score = list(map(int,input().split(" ")))#点数のリスト
    subj[m] = score
    m += 1
    i += 1
print(subj)"""