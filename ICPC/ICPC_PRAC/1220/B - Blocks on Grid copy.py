h,w = map(int,input().split())#縦h横wマス
li = list()

i = 0
while i < h:
    li.append(map(int,input().split()))
    i += 1
    print(li)
min_block = min(li)

rm_block = 0

rm_block += sum(li) - w*h*min_block
print(rm_block)

