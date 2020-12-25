while True:
    m, n, p = map(int, input().split())
    if m == 0 and n == 0 and p == 0:
        break
    c = []
    count = 0
    for j in range(m + 1):
        if j == p:
            c.append(1)
        elif j == 0:
            c.append(99)
        else:
            c.append(0)
    #print(c)
    for i in range(n):
        a, b = map(int, input().split())
        if c[a] == 1 or c[b] == 1:
            c[a] = 1
            c[b] = 1
        #print(c)
    j = 0
    for j in range(m + 1):
        if c[j] == 1:
            count += 1
    print(count)