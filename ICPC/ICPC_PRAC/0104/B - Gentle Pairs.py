times = int(input())
count = 0

li = list()
for i in range(times):
    l = list(map(int,input().split()))
    li.append(l)
# print(li)

for i in range(times-1):
    for j in range(times - i - 1):
        katamuki = (li[i+1+j][1] - li[i][1])/(li[i+1+j][0] - li[i][0])
        # print(katamuki)
        if katamuki >= -1 and katamuki <= 1:
            count += 1
print(count)