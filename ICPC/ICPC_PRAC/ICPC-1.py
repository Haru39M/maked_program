while True:
    n,m = list(map(int,input().split(" ")))#n生徒数m科目

    if n == 0 and m == 0:
        break

    if not((n >= 1 and n <= 1000) and (m >= 1 and m <= 50)): 
        quit()


    stud = []*(m+1)#ある生徒のm科目分の点数のリスト.+1は末行の0 0をいれるため
    subj = [0]*n#ある科目のn人分の点数のリスト
    SUM = 0#合計点数を保持しておく変数
    sum = []#合計点数を入れるリスト
    Num_stud = 0#生徒番号
    Num_subj = 0#科目番号

    for i in range(m+1):#+1は末行の0 0をいれるため
        stud.append(list(map(int,input().split(" "))))
    print(stud)

    for Num_stud in range(n):
        SUM = 0#初期化
        for Num_subj in range(m):
            SUM += stud[Num_subj][Num_stud]#点数をm(科目)回加算していく
        sum.append(SUM)#科目毎の合計をsumリストへ追加
    print(sum)
    print(max(sum))

