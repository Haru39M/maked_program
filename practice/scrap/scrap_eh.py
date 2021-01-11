from bs4 import BeautifulSoup as bs4
import urllib.request
import os
url = ""
next_url = ""
index = 1
cant_use_c = ['/',':','*','?','"','<','>','|']#フォルダ名に使えない文字

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}#firefoxに偽装
url = input("最初の画像のページのURLを入力>>")#url

while 1:
    request = urllib.request.Request(url=url, headers=headers)#リクエストはheaderとurlの組み合わせ？
    html = urllib.request.urlopen(request)#urlを開いてhtmlに格納
    soup = bs4(html,"html.parser")#ソースを抽出
    result = str(soup.find_all("div",id = "i3"))#soupからdivタグのid="i3"のやつを探してresultに格納
    result = result.split()#空白で区切る
    for i in range(len(result)):
        if "src" in result[i]:#画像のurlを含んだ要素を取り出す
            img_result = result[i]
            break
    for i in range(len(result)):
        if "href" in result[i]:#次のページのurlを含んだ要素を取り出す
            next_url_result = result[i]
            break
    img_url = img_result[5:-1]#画像のurl抽出
    next_url = next_url_result[6:-1]#次のページのURL抽出

    title = str(soup.find_all("h1"))[5:-6]#タイトルを抽出
    for i in range(len(cant_use_c)):#タイトルにフォルダ名として使えない文字があれば
        if cant_use_c[i] in title:
            title = title.replace(cant_use_c[i],"")#空白に置き換える
    if not os.path.exists("scrap/"+title):#もし存在していなければ、タイトル名のフォルダを作る
        os.mkdir("scrap/"+title)

    request = urllib.request.Request(url=img_url, headers=headers)#画像のurlへアクセスする為のリクエストを作成
    img_url=urllib.request.urlopen(request).read()#画像のurlを開いて読み込み

    file_name = str(index)+".jpg"
    file_pass = "scrap/"+title+"/"+file_name#ファイルのパスと名前を作る
    with open(file_pass,"wb") as aaa:#パスを開く。無ければ作られる。
        aaa.write(img_url)#書き出し
        aaa.close()#保存
    
    if url == next_url:#次のページがなければ終了
        print(str(index)+"個目の画像をダウンロードしました。")
        print(str(index)+"個の画像をダウンロードしました。")
        break
    else:#あれば続行
        print(str(index)+"個目の画像をダウンロードしました")
        url = next_url
        index += 1