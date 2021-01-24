from pixivpy3 import *
import os
import time

pixivID = "28407048"

#folder check
if not os.path.exists("./pixiv_images"):
    os.mkdir("./pixiv_images")
if not os.path.exists("./pixiv_images/bookmark"):
    os.mkdir("./pixiv_images/bookmark")

#api login
aapi = AppPixivAPI()
aapi.login("harutowakayama3@gmail.com","Harusamebiyori3")

#os.mkdir("./pixiv_images") 初回起動時のみ実行

bookmark_count=input("your bookmark count number please.\n only public bookmark:")
bookmark_count=int(bookmark_count)//30+1

json_user_collect = aapi.user_bookmarks_illust(pixivID, restrict='public')
while bookmark_count > 0:
    print("#"+str(bookmark_count))
    num=len(json_user_collect.illusts)
    
    bookmark_count=bookmark_count-1
    for illust in json_user_collect.illusts[:num]:
        writer = str(illust.user.id)
        if not os.path.exists("./pixiv_images/bookmark/"+writer):
            os.mkdir("./pixiv_images/bookmark/"+writer)
        savepath="./pixiv_images/bookmark/"+writer

        URL = illust.image_urls.large
        filename = ""
        X = list(URL)
        Y = [i for i, x in enumerate(X) if x == '/']
        Z = [i for i, x in enumerate(X) if x == 'g']
        imax = X[-1]
        i = Y[-1]
        j = Z[-1]
        while i <= j:
            filename = filename + str(X[i])
            i += 1
        filename = filename.replace("/","")
        filename = filename.replace(".jpg",".png")
        
        aapi.download(illust.image_urls.large,path=savepath,name=filename)
        print("#"+str(writer)+":"+str(illust.title)+":"+filename)
        time.sleep(0.5)
    if bookmark_count>0:
        next_url=json_user_collect.next_url
        next_qs=aapi.parse_qs(next_url)
        json_user_collect=aapi.user_bookmarks_illust(**next_qs)
