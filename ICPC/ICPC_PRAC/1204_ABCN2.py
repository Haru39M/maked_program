""" #1
n = int(input())
a = 1
count = 0
double = 0
#while a*a<n:#cを求める必要は無い。a*a<nとなる条件の上で、aを増やして行ってn/aをする。もしa*a = nならdoubleに+1してcountを2倍したあとに引く。
for a in range(1,n+1):
    for b in range(1,n+1):
        if a*b <= n:#c=0となるケースを含めて計算
            count += 1
        if a*b == n:#c=0となるケースを除く回数をカウント
            double += 1
print("count:{}".format(count))
print("double:{}".format(double))
print(count-double)


#2
n = int(input())
a = 1
b = 1
count = 0
#cを求める必要は無い。a*a<nとなる条件の上で、aを増やして行ってn/aをする。もしa*a = nならdoubleに+1してcountを2倍したあとに引く。
#while a*a<n and a < n+1:
for a in range(1,n+1):
    for b in range(1,n+1):
        if a*b < n:
            count += 1
print("count:{}".format(count))
print(count)


#3
n = int(input())
a = 1
b = 1
count = 0
double = 0
while a*a<n:
    while b < n:
        if a*b < n:
            count += 1
        if a*b == n:
            double += 1
        b += 1
    a += 1
print("count:{}".format(count))
print("double:{}".format(double))
print(count*2-double)


#4
n = int(input())
a = 1
b = 1
count = 0
double = 0
#cを求める必要は無い。aとbが定まればcも一つに定まる。a*a<nとなる条件の上で、aを増やして行ってn/aをする。もしa*a = nならdoubleに+1してcountを2倍したあとに引く。
#while a*a<n and a < n+1:
for a in range(1,n):
    if a*a<n:#=を含むとcが0のときなのでNG
        for b in range(1,n):
            if a*b < n:
                count += 1
print("count:{}".format(count))
print("double:{}".format(double))
print(count) """


#5一番いい感じ
n = int(input())
count = 0
for a in range(1,n):
    for b in range(1,n//a+1):
        if a*b < n:
            #print("{},{}".format(a,b))
            count += 1
#print("count:{}".format(count))
print(count)

#6
n = int(input())
count = 0
for a in range(1,n):
    for b in range(1,n//a+1):
        if a*b < n and a>=b:
            #print("{},{}".format(a,b))
            count += 2
            if a==b:#aとbが同じなら重複した組み合わせなので1引く
                #print("!!!{},{}".format(a,b))
                count -= 1
#print("count:{}".format(count))
print(count)