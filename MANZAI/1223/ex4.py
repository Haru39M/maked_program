meats = ["豚肉","牛肉","鶏肉","羊肉","馬肉","人肉"]
vegetables = ["ブロッコリー","にんじん","レタス","白菜","アボカド"]
desserts = ["ケーキ","チョコレート","ゼリー","ドーナツ","プリン"]

for i,meat in enumerate(meats):
    print(i,meat)

for i,(m,v) in enumerate(zip(meats,vegetables)):
    print(i,m,v)

for m,v,d in zip(meats,vegetables,desserts):
    print(m,v,d)