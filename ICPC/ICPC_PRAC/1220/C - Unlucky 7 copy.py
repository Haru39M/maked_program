# count = 0
# num8 = ""
# num10 = int(input())
# num10_bk = 0
# count_bk = 0
# shinsu = 2
# new_num8 = 0


# # num10が何桁か調べる
# i = 0
# while True:
#     keta = num10//10**i
#     if keta < 10:
#         keta = i+1
#         break
#     i += 1
# print("ケタ:"+str(keta))

# #num10を分解
# for i in range(keta):
#     if not int(str(num10)[i]) == 0:
#         num10_bk = int(str(num10)[i])*10**((keta-1)-i)
#         print(num10_bk)

#         # 7を含まない数の個数
#         if int(str(num10_bk)[0]) >= 7:#最上位ケタが7以上なら
#             count_bk = int(str(num10_bk)[0])-1  # 最上位ケタで使える数の個数はそのケタの数-2(0と7が使えないので)
#         else:#6以下なら
#             count_bk = int(str(num10_bk)[0])  # 最上位ケタで使える数の個数は0以外
#         count_bk *= 9#それ以外のケタは7以外
#     count += count_bk
# print("カウント:"+str(count))

# i = 1
# while True:
#     if i > keta-1:
#         break
#     if int(str(num10)[i]) == 7:
#         count *= int(str(num10)[i])  # 使える数の個数はそのケタの数
#     else:
#         count = int(str(num10)[i])-1  # 使える数の個数はそのケタの数-1(7が使えないので)
    
#     i += 1
# print("カウント:"+str(count))
# num10set = set(range(7,num10,10))#10進数で表したときに１の位に7を含む
# print(num10set)
# num8set = set(range(7,num10,8))#8進数で表したときに7を含む
# print(num8set)


# for i in range(num10):
#     if not('7' in list(str(num10))):#10進数に含まれていなければ8進数の判断を始める
#         count += 1#10進数に含まれてたので+1

#         while True:#8進数に変換
#             amari = str(num10%8)
#             num8 += amari
#             num10 //= 8
#             if int(num10) < 8:
#                 break
#         num8 += str(num10)
#         new_num8 = ''.join(list(reversed(num8)))

#         if not('7' in list(new_num8)):#判定
#             count += 1
# print(count)

# for i in range(num10):
#     if not('7' in list(str(num10))):#10進数に含まれていなければ8進数の判断を始める
#         count += 1#10進数に含まれてたので+1

#         while True:#8進数に変換
#             amari = str(num10%shinsu)
#             num8 += amari
#             num10 //= shinsu
#             if int(num10) < shinsu:
#                 break
#         num8 += str(num10)
#         new_num8 = ''.join(list(reversed(num8)))
#         print(str(shinsu)+"進数にすると:"+str(new_num8))

#         if not('7' in list(new_num8)):#判定
#             count += 1
# print(count)

# num10 = int(input())
# count = 0
# num8 = 0
# for i in range(num10):
#     num8 = int(oct(i)[2:])
#     #print("10進数{}:{}".format(i,"7" in str(i)))
#     #print("8進数{}:{}".format(num8,"7" in str(num8)))
#     #print()
#     if not(("7" in str(i)) or ("7" in str(num8))):
#         count += 1
# print(count)

num10 = int(input())
count = 0
num8 = 0
i = 1
while i <= num10:
    print(str(i)+":")
    num8 = int(oct(i)[2:])
    if (not("7" in str(i)) and (not("7" in str(num8)))):
        count += 1
    i += 1
print(count)

# num8 = int(oct(num10)[2:])
# print(num10)
# print(num8)
# print("7" in str(num10))
# print("7" in str(num8))
