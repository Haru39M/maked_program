wordlist = list()
worddict = dict()
times = 0
i = 0
with open("sampletext1015.txt", "r") as sampletext:
    for word in sampletext:#平文を単語ごとに分割してwordlistに格納
        wordlist = word.split(" ")
    for i in range(len(wordlist)):#単語数を記録してworddictに格納
        worddict[wordlist[i]] = 0
        i += 1
    for i in range(len(wordlist)):#単語数を記録
        times = worddict[wordlist[i]]
        worddict[wordlist[i]] = times + 1
        i += 1
    for i in range(len(worddict)):
        print(wordlist[i])
    