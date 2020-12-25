shinsu = 8
count = 0
num8 = ""
num10 = int(input())
for i in range(num10):
    if not('7' in list(str(num10))):#10進数に含まれていなければ8進数の判断を始める
        count += 1#10進数に含まれてたので+1

        while True:#8進数に変換
            amari = str(num10%shinsu)
            num8 += amari
            num10 //= shinsu
            if int(num10) < shinsu:
                break
        num8 += str(num10)
        new_num8 = ''.join(list(reversed(num8)))

        if not('7' in list(new_num8)):#判定
            count += 1
print(count)