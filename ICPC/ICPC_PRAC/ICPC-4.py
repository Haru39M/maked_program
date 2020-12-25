
while True:
    x = (5,7,5,7,7)
    flag = 0

    w = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        w.append(input().split())
    i = 0#単語の行番号
    
    s = 0#単語の文字数
    output = 0#短歌が始まる行の変数
    while i<n:
        #print(w[i])
        #print(len(str(w[i]))-4)
        s += int(len(str(w[i]))-4)
        #print("{}:{}").format(w[i],s)
        #print(x[tapnum])
        print("文字数"+str(s))
        if s == x[flag]:
            output = i+1
            print("行"+str(output))
            flag += 1
            s = 0
        else:
            s = 0
            flag = 0
            print("!!!!!!!!")
        """
        if s == 5 and flag == 0:
            flag = 1
            output = i
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
            output = 0
            s = 0
        elif (flag == 1 or flag == 3 or flag == 4 or flag == 5) and s >= 8:
            flag = 0
            output = 0
            s = 0
        """
        #print(s, flag)
        i += 1
    #print(output)