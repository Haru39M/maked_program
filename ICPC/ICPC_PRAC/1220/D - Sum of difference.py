n = int(input())
num = list(map(int,input().split()))
num.sort(reverse=True)

dist = 0
# for i in range(n-1):
#     j = i+1
#     while j < n:
#         dist += num[i] - num[j]
#         j += 1
i = 0
j = 0
for i in range(n-1):
    # print("{}*{}-{}".format(n-i,num[i],sum(num[i+1:])))
    dist += (n-i)*num[i] - sum(num[i:])
print(dist)