import numpy as np
import random
size = int(input("Input Size"))
cellXf = np.zeros((size,size))
cellX = [[]*size,[]*size]
print(cellX)
#cellX = [[int(i) for i in cellX],[int(i) for i in cellX]]

m = 0
n = 0
for m in range(size):
    for n in range(size):
        cellX[m][n] = int(cellXf[m][n])
        cellX[m][n]=random.randint(0,1)
        print(" {} ".format(cellX[m][n]),end="")
    print()
