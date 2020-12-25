xyz = [[[[1],[2],[3]],[[1],[2],[3]],[[1],[2],[3]]],[[[2]]],[[[3]]]]
"""x = []
y = []
z = []
lev = 3
for k in range(lev):
    z.append("Z"+str(k-1))
    xyz.append(z)
    for j in range(lev):
        y.append("Y"+str(j-1))
        xyz.append(y)
        for i in range(lev):
            x.append("X"+str(i-1))
            xyz.append(x)
print(xyz)"""
print(xyz[0][1][0])