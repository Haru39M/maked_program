while True:
    n,m = list(map(int,input().split(" ")))#n生徒数m科目

    if n == 0 and m == 0:
        break
    if not((n >= 1 and n <= 1000) and (m >= 1 and m <= 50)): 
        quit()

    stud = []*m#ある生徒のm科目分の点数のリスト
    subj = [0]*n#ある科目のn人分の点数のリスト
    stud_sum = [0]*n#生徒全員の合計点数を入れるリスト
    Num_stud = 0#生徒番号
    Num_subj = 0#科目番号

    for i in range(m):#リストstud[]の中にリストをm科目数分作り、そのリストの中にinputされた数字列ex(10 20 30 etc...)をスペースでsplitして格納。つまり、n生徒数分の点数が入ったリストがm科目数分リストstud[]の中に作られる。。
        stud.append(list(map(int,input().split(" "))))

    #合計点数の計算。stud_sumリストにn生徒数回数分、m科目回数分の合計点数を格納していく。
    for Num_stud in range(n):#n生徒数回数分
        for Num_subj in range(m):#m科目回数分
            stud_sum[Num_stud] += stud[Num_subj][Num_stud]#点数をm(科目)回加算していく
    print(max(stud_sum))#n生徒数のm科目数の合計点数から最大値を検索して表示

