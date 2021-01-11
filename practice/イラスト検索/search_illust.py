from pixivpy3 import PixivAPI
from pixivpy3 import AppPixivAPI

import json
import os
from time import sleep

Search_Tag = input("検索タグを入力して下さい>>")
Search_Score = int(input("最低スコアを入力して下さい>>"))
Search_PageNum = int(input("検索ページ数を入力して下さい>>"))

def login(id, password):
    api = PixivAPI()#pixivapi関数を変数apiに代入すると同じ関数として扱える。つまり名前を短くしてるだけ
    api.login(id, password)#この関数にidとpasswordを渡せばログインしてくれる
    return api

def search_and_save(apilogin, searchtag, min_score, range_num, directory):
    api = apilogin
    aapi = AppPixivAPI()

    saving_dir_path = os.path.join(directory, searchtag)#検索タグを保存フォルダ名とする(ディレクトリ名\検索タグ)os.path.join()は与えられた２つの文字列を\でくっつけてパスの形にする。
    
    if not os.path.exists(saving_dir_path):#保存フォルダが存在しなければ
        os.mkdir(saving_dir_path)#作る

    for page in range(1, range_num + 1):#検索するページ数回繰り返す
        json_result = api.search_works(searchtag, page=page, mode='tag')
        illust_len = len(json_result.response)
    print(json_result)
    print(type(json_result))
    print(illust_len)
    #     for i in range(0, illust_len):
    #         illust = json_result.response[i]
    #         score = illust.stats.score

    #         if score <= min_score:
    #             continue
    #         else:
    #             print("漫画:" + str(illust.page_count) + "ページ") if illust.is_manga else print("イラスト")
    #             if illust.is_manga:
    #                 print(">>> title:", illust.title)
    #                 manga_info = api.works(illust.id)
    #                 for page_no in range(0, manga_info.response[0].page_count):
    #                     page_info = manga_info.response[0].metadata.pages[page_no]
    #                     aapi.download(page_info.image_urls.large, path=saving_dir_path)
    #                     sleep(1)
    #             else:
    #                 print(">>> title:", illust.title)
    #                 aapi.download(illust.image_urls.large, path=saving_dir_path)
    #                 sleep(1)

def main():
    searchtag = Search_Tag  #検索タグを入力。半角スペースで分けることで複数タグ検索可能
    min_score = Search_Score    #このスコア以上のイラストのみDL
    range_num = Search_PageNum   #この値のページまで検索。1p当たり30枚
    directory = 'saveP'  #指定したディレクトリの下に検索タグ名のフォルダを作成して，そこに保存します

    apilogin  = login("harutowakayama3@gmail.com", "Harusamebiyori3") #ユーザ名とパスワード入力してログイン

    search_and_save(apilogin, searchtag, min_score, range_num, directory)#検索して保存

if __name__ == '__main__':
    main()
