h,w = map(int,input().split())#縦h横wマス
li = list()

i = 0
while i < h:
    li.append(list(map(int,input().split())))
    i += 1
min_block = min([min(x) for x in li])#最小値を出す

rm_block = 0
for i in range(h):
    rm_block += (sum(li[i])-(w*min_block))#i行の合計から最小値のみだった場合の合計を引くと、取り除く数になる
print(rm_block)

