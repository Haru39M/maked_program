from bs4 import BeautifulSoup as bs4
import urllib.request
url = ""
next_url = ""
index = 1

url = "https://e-hentai.org/s/e3ceee6c1b/1743644-1"#url

while 1:
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}#firefoxに偽装
    request = urllib.request.Request(url=url, headers=headers)#リクエストはheaderとurlの組み合わせ？
    html = urllib.request.urlopen(request)
    soup = bs4(html,"html.parser")
    result = str(soup.find_all("div",id = "i3"))
    result = result.split()
    #print(result)
    for i in range(len(result)):
        if "src" in result[i]:#画像のurlを含んだ要素を取り出す
            img_result = result[i]
            break
    for i in range(len(result)):
        if "href" in result[i]:#次のページのurlを含んだ要素を取り出す
            next_url_result = result[i]
            break
    img_url = img_result[5:-1]#画像のurl抽出
    next_url = next_url_result[6:-1]
    #print(result)
    print(img_url)
    print(next_url)

    request = urllib.request.Request(url=img_url, headers=headers)
    img_url=urllib.request.urlopen(request).read()
    file_name = "scrap/img/"+str(index)+".jpg"
    with open(file_name,"wb") as aaa:
        aaa.write(img_url)
        aaa.close()
    
    if url == next_url:
        break
    else:
        url = next_url
        index += 1