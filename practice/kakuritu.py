new_inf = int(input("新規感染者を入力"))
day = int(input("何日後?"))
p = new_inf/1537000
p = 1-p
for i in range(day):
    p *= p
    print("day:["+str(i)+"]"+str(p)[1:])