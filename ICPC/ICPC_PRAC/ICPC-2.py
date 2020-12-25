
while True:
    ave_income = 0#平均所得
    under_people = 0#平均所得以下の人数


    n = int(input())

    if n == 0:
        break

    income = list(map(int,input().split(" ")))
    #print(n)
    #print(income)
    
    for i in income:
        ave_income += i
    ave_income /= n
        
    #print(ave_income)

    for i in range(n):
        if income[i] <= ave_income:
            under_people += 1
    print(under_people)