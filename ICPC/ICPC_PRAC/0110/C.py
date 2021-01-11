n = int(input())
a = list(map(int,input().split()))
end = int(len(a))
end = int(end/2)
a_mae = a[:end]
a_ushiro = a[end:]
if max(a_mae) < max(a_ushiro):
    print(a_mae.index(max(a_mae))+1)
else:
    print(int(a_ushiro.index(max(a_ushiro)))+1+len(a_mae))