while True:
    n = int(input())
    if n == 0:
        break
    w = list(map(int, input().split()))
    print(w)
    i=0
    flag = 0
    count = 0
    while i<n:
        if w[i] == 2 and flag == 0:
            flag = 1
        elif w[i] == 0 and flag == 1:
            flag = 2
        elif w[i] == 2 and flag == 2:
            flag = 3
        elif w[i] == 0 and flag == 3:
            count += 1
            flag = 0
            #break
        else:
            #print("!!")
            flag = 0
        #print(w[i], flag, count, i)
        i += 1
    print(count)