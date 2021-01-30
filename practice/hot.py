R = 0#抵抗(ohm)
ro = 20.53#1mあたりの抵抗(ohm/m)
L = 0.5/5#長さ(m)
V = 0#電圧(V)
P = 0#ジュール熱(J)
t = 0#時間(s)
M = 0#水の質量(g)
dC = 0#上げる温度

M = int(input("水の質量(g)を入力"))
V = int(input("電圧を入力"))
dC = int(input("何度上げる？"))
R = ro*L/2
t = 4.2*dC*M*R/(V*V)
print("{}分{}秒".format(t//60,t%60))