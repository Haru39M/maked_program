kosuu = 0#三角形の個数
data_num = int(input())
num = list(map(int,input().split(" ")))#辺の長さを入れる
num.sort()
print("{}\n{}".format(data_num,num))
#num = list(set(num))#同じものがあれば削除。ついでに降順にソートしてくれる
#print(num)
""" 
for i in range(data_num):
    if i == data_num-1:
        continue #終端なら次の要素は見ない
    elif num[i] == num[i+1]:
        del(num[i])
#data_num = len(num)#削除したのでデータ数を更新
print("{},{}".format(data_num,num))
"""

""" #data_num = len(num)#データ数を更新
#まず３つ選ぶ全通りを計算
#nCrだから
i = 0
N = 1
R = 1
while i < 3:
    N *= (data_num-i)
    R *= i+1
    i+=1
nCr = N/R
print(nCr) """
#三角形の個数をカウント
count = list()
for i in range(data_num-2):
    for j in range(i+1,data_num-1):
        for k in range(j+1,data_num):
            print("index:[{}][{}][{}] = ".format(i,j,k),end="")
            if num[i]+num[j]>num[k] and num[i]+num[k]>num[j] and num[j]+num[k]>num[i] and num[i] != num[j] and num[j] != num[k]:
                print("{},{},{}".format(num[i],num[j],num[k]))
                count.append("{},{},{}".format(num[i],num[j],num[k]))
            else:
                print()
    #count = list(set(count))
print(count)
print(len(count))

#all main
""" kosuu = 0
data_num = int(input())
num = list(map(int,input().split(" ")))
num.sort()
count = list()
for i in range(data_num-2):
    for j in range(i+1,data_num-1):
        for k in range(j+1,data_num):
            if num[i]+num[j]>num[k] and num[i]+num[k]>num[j] and num[j]+num[k]>num[i] and num[i] != num[j] and num[j] != num[k]:
                count.append("{},{},{}".format(num[i],num[j],num[k]))
print(len(count)) """










#last successed
data_num = int(input())
num = list(map(int,input().split(" ")))
num.sort()
count = 0
for i in range(data_num-2):
    for j in range(i+1,data_num-1):
        for k in range(j+1,data_num):
            if num[i]+num[j]>num[k] and num[i]+num[k]>num[j] and num[j]+num[k]>num[i] and num[i] != num[j] and num[j] != num[k]:
                count += 1
print(count)



