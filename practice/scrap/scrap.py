from bs4 import BeautifulSoup as bs4
import urllib.request
index = 2
url = "https://e-hentai.org/s/e3ceee6c1b/1744500-"+str(index)#url
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}#firefoxに偽装
request = urllib.request.Request(url=url, headers=headers)#リクエストはheaderとurlの組み合わせ？
html = urllib.request.urlopen(request)
soup = bs4(html,"html.parser")
result = str(soup.find_all("img",id = "img"))
result = result.split()
for i in range(len(result)):
    if "https" in result[i]:
        result = result[i]
        break
img_url = result[5:-1]
print(result)
print(img_url)
print(type(img_url))
request = urllib.request.Request(url=img_url, headers=headers)
img_url=urllib.request.urlopen(request).read()
file_name = "scrap/img/"+str(index)+".jpg"
with open(file_name,"wb") as aaa:
    aaa.write(img_url)
    aaa.close()
# index += 1