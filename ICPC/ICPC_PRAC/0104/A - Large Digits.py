a,b = map(int,input().split())
sa = 0
sb = 0
while a > 0:
    sa += a % 10
    a //= 10
while b > 0:
    sb += b % 10
    b //= 10
if sa > sb:
    print(sa)
else:
    print(sb)