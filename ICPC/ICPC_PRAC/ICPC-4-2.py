while True:
    w = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        w.append(input().split())
    i = 0
    flag = 0
    s = 0
    output = 0
    break_flag = 0
    while i<n:
        #print(w[i])
        #print(len(str(w[i]))-4)
        if s == 0 and flag == 0:
            output = i+1
        s += int(len(str(w[i]))-4)
        if s == 5 and flag == 0:
            flag = 1
            s = 0
        elif s == 7 and flag == 1:
            flag = 2
            s = 0
        elif s == 5 and flag == 2:
            flag = 3
            s = 0
        elif s == 7 and flag == 3:
            flag = 4
            s = 0
        elif s == 7 and flag == 4:
            flag = 5
            break
        elif (flag == 0 or flag == 2) and s >= 6:
            flag = 0
            s = 0
            i = output-1
        elif (flag == 1 or flag == 3 or flag == 4) and s >= 8:
            flag = 0
            s = 0
            i = output-1
        print("sum "+str(s)+" flag "+str(flag)+" i "+str(i+1))
        i += 1
    print(output)