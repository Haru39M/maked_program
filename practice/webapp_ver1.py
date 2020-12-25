youbi = int(input("１日の曜日を入力(0:日6:土)"))
matsu = int(input("末日を入力"))
day = 1

print("Su ",end="")
print("Mo ",end="")
print("Tu ",end="")
print("We ",end="")
print("Th ",end="")
print("Fr ",end="")
print("Sa ",end="")
print("")

for j in range(youbi):
    print("   ",end="")

for i in range(matsu):
    if day < 10:
        print(" ",end="")
    print(str(day)+" ",end="")

    if youbi == 6:
        print("")
    if youbi < 6:
        youbi += 1
    else:
        youbi = 0
    day += 1