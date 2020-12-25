from turtle import *

numbers = [0,1]
for i in range(100):
    numbers.append(sum(numbers[-2::]))

i = 1
while True:
    forward(int(numbers[i]))
    left(90)
    i+=1
    if abs(pos())<1:
        break
input()