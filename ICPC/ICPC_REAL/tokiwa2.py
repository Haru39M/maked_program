while True:
    n = []
    m = []
    s = 0  #sum
    a = 0
    total = 0
    p = int(input())#割られる数
    if p == 0:
        break
    mini = p#最低値を割られる数pに設定(sがこれより大きくなることは無いため)
    i = 1#割る数
    #do-while的な書き方
    n.append(i)
    m.append(p)#最初はpを割るので
    print("割られる数"+str(p))
    print("N :"+str(n))
    print("M :"+str(m))
    
    while n[i-1] <= m[i-1]:
        n.append(i)
        m.append(m[i-1]//i)
        if n[i-1] > m[i-1]:
            break
        print("割られる数"+str(p))
        print("N(割る数) :"+str(n))
        print("M(商) :"+str(m))
        i += 1

    i = 0
    for i in range(len(n)):
        s = n[i] + m[i]
        if s < mini:
            mini = s
        print("mini : "+str(mini+1))