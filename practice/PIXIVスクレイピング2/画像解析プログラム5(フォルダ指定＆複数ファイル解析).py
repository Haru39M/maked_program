import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import shutil
import os
S = 0
MAX = int(input("解析する数を入力してください",))
foldername = str(input("解析対象とするフォルダ名を入力してください",))
n = 1
while S < MAX:

    #foldernamelist = os.listdir(path="./pixiv_images/bookmark/")            #全フォルダ名をリスト化
    #foldername = foldernamelist[S]                                          #フォルダ名を指定
    filenamelist = os.listdir(path = "./pixiv_images/bookmark/"+foldername)
    if n < len(filenamelist):               #ファイル数が２以上の時
        del filenamelist[-1]                #パレットフォルダを除外
        filename = filenamelist[n-1]
        n += 1
    else:
        filename = filenamelist[0]
    cv2_img = cv2.imread("./pixiv_images/bookmark/"+foldername+"/"+filename)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img.shape
    cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))
    cv2_img.shape
    cluster = KMeans(n_clusters=5)
    cluster.fit(X=cv2_img)
    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,n_clusters=5, n_init=10, n_jobs=1, precompute_distances='auto',random_state=None, tol=0.0001, verbose=0)
    cluster.cluster_centers_
    cluster.cluster_centers_.shape
    format(255, '02x')
    '#%02x%02x%02x' % (255, 255, 255)
    cluster_centers_arr = cluster.cluster_centers_.astype(int, copy=False)
    from IPython.display import display
    for rgb_arr in cluster_centers_arr:
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        color_img = Image.new(mode='RGB', size=(32, 32), color=color_hex_str)
        display(color_img)
    IMG_SIZE = 64
    MARGIN = 15
    width = IMG_SIZE * 5 + MARGIN * 2
    height = IMG_SIZE + MARGIN * 2
    print(width, height)
    tiled_color_img = Image.new(mode='RGB', size=(width, height), color='#333333')

    for i, rgb_arr in enumerate(cluster_centers_arr):
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        color_img = Image.new(mode='RGB', size=(IMG_SIZE, IMG_SIZE),color=color_hex_str)
        tiled_color_img.paste(im=color_img,box=(MARGIN + IMG_SIZE * i, MARGIN))

    if not os.path.exists("./pixiv_images/bookmark/" + foldername + "/" + "パレット" + foldername):
        tiled_color_img.save("パレット" + filename)
        os.mkdir("./pixiv_images/bookmark/" + foldername + "/" + "パレット" + foldername)
        shutil.move("./パレット"+filename,"./pixiv_images/bookmark/" + foldername + "/" + "パレット" + foldername)
    print(foldername+"/"+filename)
    
    S += 1
