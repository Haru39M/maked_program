"""
l = []

l.append(5)
l.append(3.14)
l.append(1)
l.append("hoge")
l.append("hige")

for value in l:
    print(value)

for l in range(len(l)):
    print(l[l])
"""
"""
d = dict()
d["jhon"] = 21#key & value must be set
d["stive"] = 49
d["tony"] = 30
d["robin"] = 18
d["jack"] = 23

print(d)

for key in d.keys():#dのキーをひとつずつkeyに代入
    print(key,d[key])
"""

freq = dict()
with open("sampletext1015.txt","r") as f:
    for line in f:
        words = line.split()
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        for k,v in freq.items():
            print(k,v)

