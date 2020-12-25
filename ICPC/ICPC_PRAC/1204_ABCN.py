n = int(input())
a = 1
b = 1
c = 1
count = 0
double = 0
while n>c:
    nc = n-c
    for i in range(1,nc+1):#基本は1,3,5,7...と奇数で割っていく
        a = i
        print("({}-{})/{} = ".format(n,c,a),end="")
        if a*a <= nc:
            if (nc)%a == 0:
                b = int((nc)/a)
                print(b)
                count += 1
            if a*a == nc:
                double += 1
        else:
            print()
    c += 1
print(count*2-double)

""" n = int(input())
a = 1
b = 1
c = 1
abclist = list()
while n>c:
    for i in range(1,n+1):
        a = i
        if (n-c)%a == 0:
            b = int((n-c)/a)
            abclist.append(list("{}".format(b)))
    c += 1
print(len(abclist)) """
    