from bs4 import BeautifulSoup as bs4
import urllib.request
import os

#for make pdf
import img2pdf
from PIL import Image # img2pdfと一緒にインストールされたPillowを使います

ismakepdf = bool(input("ダウンロード後にpdfを作成しますか？1:yes 0:no"))
ismakepdfonly = bool(input("既にある画像からpdfを作成しますか？1:yes 0:no"))

def save():
    index = 1
    cant_use_c = ['/',':','*','?','"','<','>','|']#フォルダ名に使えない文字

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}#firefoxに偽装
    url = input("最初の画像のページのURLを入力>>")#url
    request = urllib.request.Request(url=url, headers=headers)#リクエストはheaderとurlの組み合わせ？
    html = urllib.request.urlopen(request)#urlを開いてhtmlに格納
    soup = bs4(html,"html.parser")#ソースを抽出
    while 1:
        result = str(soup.find_all("section",id = "image-container")).split()#soupからdivタグのid="i3"のやつを探して、空白で区切ってリストresultに格納
        
        #url生成
        for i in range(len(result)):#リストresultから画像のurlを含んだ要素を探す
            if "src" in result[i]:#最初に見つかったものを取り出す
                img_result = result[i].replace('src="',"").replace('"',"").split("/")[:-1]#画像のurl(画像番号と拡張子除く)
                img_result = "/".join(img_result)+"/"#/で結合
                img_kakuchoushi = "." + result[i].replace('src="',"").replace('"',"").split("/")[-1].split(".")[-1]#拡張子
                break
        img_url = img_result+str(index)+img_kakuchoushi#画像のurl生成。
        print("画像のURL:{}".format(img_url))

        last_url_result = str(soup.find_all("a",class_="last")).split()
        for i in range(len(last_url_result)):
            if "href" in last_url_result[i]:#最期のページのurlを含んだ要素を取り出す
                last_url = last_url_result[i]
                break
        last_index = last_url[6:-4].split("/")[-2]#最期のページの番号抽出

        #タイトル生成
        title = str(soup.find_all("title")).split()#タイトルを抽出
        title = title[:int(title.index("Page"))]#余分な要素以外を取り出して更新
        title = " ".join(title)#空白で繋げる
        title = title[8:-2]#余分な要素以外を取り出して更新
        
        #フォルダ生成
        for i in range(len(cant_use_c)):#タイトルにフォルダ名として使えない文字があれば
            if cant_use_c[i] in title:
                title = title.replace(cant_use_c[i],"")#空白に置き換える
        if not os.path.exists("scrap/"+title):#もし存在していなければ、タイトル名のフォルダを作る
            os.mkdir("scrap/"+title)

        
        request = urllib.request.Request(url=img_url, headers=headers)#画像のurlへアクセスする為のリクエストを作成
        img=urllib.request.urlopen(request).read()#画像のurlを開いて読み込み

        file_pass = "scrap/"+title+"/"+str(index)+img_kakuchoushi#ファイルのパスと名前を作る
        
        with open(file_pass,"wb") as aaa:#パスを開く。無ければ作られる。
            aaa.write(img)#書き出し
            aaa.close()#保存
        
        if int(index) == int(last_index):#次のページがなければ終了
            print(str(index)+"個目の画像をダウンロードしました。")
            print(str(index)+"個の画像をダウンロードしました。")
            if ismakepdf == True:
                make_pdf(title,img_kakuchoushi)
            break#while文を抜ける
        else:#あれば続行
            print(str(index)+"/"+str(last_index)+"個目の画像をダウンロードしました")
            index += 1

def make_pdf(folder_name,kakuchoushi):#読み込む画像フォルダを入力。pdfのファイル名はフォルダ名と同じになる。
    pdf_FileName = "scrap/{}/{}.pdf".format(folder_name,folder_name) # 出力するPDFの名前
    png_Folder = "scrap/{}/".format(folder_name) # 画像フォルダ
    extension  = kakuchoushi # 拡張子がPNGのものを対象

    with open(pdf_FileName,"wb") as f:
        # 画像フォルダの中にあるPNGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(img2pdf.convert([Image.open(png_Folder+j).filename for j in os.listdir(png_Folder)if j.endswith(extension)]))

if __name__ == '__main__':
    if ismakepdfonly == False:
        folder_name = input("フォルダ名を入力してください")
        kakuchoushi = input("拡張子を入力してください(例: .jpg)")
        make_pdf(folder_name,kakuchoushi)
    else:
        save()