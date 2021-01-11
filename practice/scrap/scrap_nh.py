from bs4 import BeautifulSoup as bs4
import urllib.request
import os
url = ""
next_url = ""
index = 1
cant_use_c = ['/',':','*','?','"','<','>','|']#フォルダ名に使えない文字

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}#firefoxに偽装
url = input("最初の画像のページのURLを入力>>")#url
request = urllib.request.Request(url=url, headers=headers)#リクエストはheaderとurlの組み合わせ？
html = urllib.request.urlopen(request)#urlを開いてhtmlに格納
soup = bs4(html,"html.parser")#ソースを抽出

while 1:
    result = str(soup.find_all("section",id = "image-container")).split()#soupからdivタグのid="i3"のやつを探してresultに格納
    for i in range(len(result)):
        if "src" in result[i]:#画像のurlを含んだ要素を取り出す
            img_result = result[i]
            break
    img_url = img_result[5:-6]+str(index)+".png"#画像のurl抽出。拡張子は場合によって変える必要あり

    last_url_result = str(soup.find_all("a",class_="last")).split()
    for i in range(len(last_url_result)):
        if "href" in last_url_result[i]:#最期のページのurlを含んだ要素を取り出す
            last_url = last_url_result[i]
            break
    last_index = last_url[6:-4].split("/")[-2]#最期のページの番号抽出

    title = str(soup.find_all("title")).split()#タイトルを抽出
    title = title[:int(title.index("Page"))]#余分な要素以外を取り出して更新
    title = " ".join(title)#空白で繋げる
    title = title[8:-2]#余分な要素以外を取り出して更新
    
    for i in range(len(cant_use_c)):#タイトルにフォルダ名として使えない文字があれば
        if cant_use_c[i] in title:
            title = title.replace(cant_use_c[i],"")#空白に置き換える
    if not os.path.exists("scrap/"+title):#もし存在していなければ、タイトル名のフォルダを作る
        os.mkdir("scrap/"+title)

    request = urllib.request.Request(url=img_url, headers=headers)#画像のurlへアクセスする為のリクエストを作成
    img_url=urllib.request.urlopen(request).read()#画像のurlを開いて読み込み

    file_pass = "scrap/"+title+"/"+str(index)+".jpg"#ファイルのパスと名前を作る
    with open(file_pass,"wb") as aaa:#パスを開く。無ければ作られる。
        aaa.write(img_url)#書き出し
        aaa.close()#保存
    
    if int(index) == int(last_index):#次のページがなければ終了
        print(str(index)+"個目の画像をダウンロードしました。")
        print(str(index)+"個の画像をダウンロードしました。")
        break
    else:#あれば続行
        print(str(index)+"個目の画像をダウンロードしました")
        # url = next_url
        index += 1