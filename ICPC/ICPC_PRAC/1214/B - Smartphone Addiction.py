n, m, t = map(int, input().split(" "))
maxn = n
a = list()
b = list()
time = list()
di = list()

time.append(0)
for i in range(m):
    a.append(0)
    b.append(0)
    a[i],b[i] = map(int, input().split(" "))
    time.append(a[i])
    time.append(b[i])
time.append(t)

for i in range(2+2*m-1):
    di.append(time[i+1]-time[i])
print(di)

for i in range(len(di)):
    if i%2 == 1:
        if n+di[i] > maxn:
            n = maxn
        else:
            n+=di[i]
        #print(n)
    elif i%2 == 0:
        n -= di[i]
        #print(n)
    if n<=0:
        print("No")
if n>0:
    print("Yes")
print(n)