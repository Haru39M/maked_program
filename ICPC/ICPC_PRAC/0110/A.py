x,y = map(int,input().split())
if x-y > 3 or y-x >3:
    print("No")
elif x-y == 3 or y-x == 3:
    print("No")
else:
    print("Yes")