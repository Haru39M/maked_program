while True:
    m, n, p = map(int, input().split())
    a = []
    b = []
    print(a,b)
    if m == 0 and n == 0 and p == 0:
        break

    c = []
    count = 0
    for j in range(m+1):
        if j == p:
            c.append(1)
        elif j == 0:
            c.append(99)
        else:
            c.append(0)
    print(c)

    #for i in range(n):

    i = 0
    """
    while i < n:
        a,b = map(int, input().split())
        print(a,b)
        if a == p or b == p:
            c[i] = 1
            print("a")
        else:
            print("error")
        i += 1
    #
    # j = 0
    # for j in range(m + 1):
    #     if c[j] == 1:
    #         count += 1
    #
    # print(count)
    # 
    """