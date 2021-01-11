#空辞書の作成
activities={}
activities=dict()

#辞書の初期化
activities={"Monday":"バスケ"}

#辞書への追加
activities["Sunday"]="ハイキング"

print(activities["Sunday"])

input_key="everyday"
input_value="通学"
activities[input_key]=[input_value,input_value]

print(activities)

#辞書の特定のキーを持つ要素の削除
del activities["Sunday"]

print(activities)

#辞書のキーに特定の値が含まれるかの判定
print("Sunday" in activities)
print("Monday" in activities)

#タプルの使い方
#タプルは定義（宣言）したら変更できないリスト
tuple_sample=("apple",3,90.4)
print(tuple_sample)
print(tuple_sample[0])

#セット（集合）型
#セットは重複を許さない
flavor=["apple","soda","chocolate","apple","grape","grape","soda"]
flavor_set=set(flavor)

print(flavor_set)

#セット型の宣言
flavor_set_A={"apple","peach","soda"}
print(type(flavor_set_A))

flavor_set_B={"apple","soda","chocolate"}
print(flavor_set_A ^ flavor_set_B)
print(flavor_set_A | flavor_set_B)
print(flavor_set_A & flavor_set_B)


