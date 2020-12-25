while True:
    n = int(input())
    w = list(map(int,input().split()))
    print(w)
    
    i = 0
    flag = 0
    output = i
    count = 0

    while i<n:
        if flag == 0:
            output = i
        
        if w[i] == 2 and flag == 0:
            flag = 1
        elif w[i] == 0 and flag == 1:
            flag = 2
        elif w[i] == 2 and flag == 2:
            flag = 3
        elif w[i] == 0 and flag == 3:
            count += 1
            flag = 0
        else:
            flag = 0
        print(w[i],flag)

        i += 1
    print(count)