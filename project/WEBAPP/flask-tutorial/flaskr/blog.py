from flask import (
    # add for metoo
    Blueprint, flash, g, redirect, render_template, request, url_for, json, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
# from flaskr.metoo_db import get_metoo,get_id_list,execute_sql #add for metoo

# add for pushbullet
import requests
import json
from AddAPI.pushbullet import push_message
# addend
# add for get time(jst)
from datetime import timedelta, timezone, datetime
# addend
#add for ajax
import sys

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username, nowtime, metoo,task_color'# ここでuserテーブルのidとpostテーブルのauthor_idをコピーしてる？
        ' FROM post p JOIN user u ON p.author_id = u.id'#投稿IDと著者IDを紐付け
        ' ORDER BY created DESC'#作られた順にソート
    ).fetchall()  # リスト化。schema.sql内のデータをセレクトしてpostsというリストに入れていく
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    # add for timeget
    jst = timezone(timedelta(hours=9), 'JST')
    date = datetime.now(jst).strftime("%Y/%m/%d (%A) - %H : %M")
    # add end
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        metoo = int(0)#初期値
        error = None

        # add for pushbullet
        token = get_token()
        push_message(title, body,token)
        # addend

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                # postというテーブルのカラムtitle,body,author_idにデータを挿入する宣言
                'INSERT INTO post (title, body, author_id, nowtime, metoo)'
                ' VALUES (?, ?, ?, ?, ?)',  # 値がいくつあるかを宣言
                (title, body, g.user['id'], date,metoo)  # valuesにタプルとして値を代入
            )
            db.commit()  # 値を確定
            # 記事を書き終わるとindex.htmlに戻っている？
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(  # postに投稿ID、タイトル、本文、作成時刻、著者ID、著者名を格納
        'SELECT p.id, title, body, created, author_id, username ,metoo'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()#１件ずつデータを持ってくる

    if post is None:  # もしpostに何も入っていなければ404
        abort(404, "Post id {0} doesn't exist.".format(id))

    # もし著者IDとユーザーIDが異なれば本人じゃないので繋げない
    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):  # 投稿を更新(書き換え)
    post = get_post(id)  # 投稿IDの投稿を取得

    if request.method == 'POST':
        title = request.form['title']  # タイトルを取得
        body = request.form['body']  # 本文を取得
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):  # 投稿を削除。idは投稿ID
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

@bp.route('/metoo_post', methods=['POST'])#ホームで更新されるとこの関数が実行される
def insert_metoo():#データベースのmetooを更新する。idは投稿ID
    post_id = request.json['id']
    metoo = int(request.json['metoo'])+1#１増やす
    return_json = {'id':post_id,'metoo':metoo}#json形式で返すためにこの形にする
    #動作チェック用
    # print("result is {}".format(post_id))
    # print("clicked_python")
    # print("metoo is {}".format(metoo))

    # add for pushbullet
    post = get_post(post_id,check_author=False)#別ユーザーにお知らせするためにcheck_authorはFalse
    token = get_token()
    push_message(post['title'], post['body'],token)#タイトルと本文を送信
    # addend
    
    #データベースからmetooの数、評価された投稿のIDを取り出してmetoosというリストに入れる
    db = get_db()#データベースにアクセスする
    db.execute(
        'UPDATE post SET metoo = ?'
        'WHERE id = ?',#評価された投稿のIDと投稿のidを紐付け
        (metoo,post_id)
    )
    db.commit()
    return jsonify(ResultSet = json.dumps(return_json))#jsonをjsに返す

@bp.route('/set_token',methods=('GET','POST'))
def set_token_fun():
    # print("worked set_token")
    token_default = get_token()
    if request.method == 'POST':
        token = None
        token = request.form['token']
        # print(token)
        if token is not None:
            # print("token inputted!")
            db = get_db()
            db.execute(
                'UPDATE user SET token = ?'
                'WHERE id = ?',
                (token, g.user['id'])
            )
            db.commit()  # 値を確定
            return redirect(url_for('blog.index'))
    return render_template('blog/set_token.html',token_default = token_default)#set_token.htmlへレンダリング

def get_token():
    db = get_db()
    token = None
    token = db.execute(
        'SELECT token'
        ' FROM user'
        ' WHERE user.id = ?',
        (g.user['id'],)
    ).fetchone()
    # print(g.user['id'])
    return token[0]

@bp.route('/set_color', methods=('GET', 'POST'))
def set_task_color():
    print("worked set_task_color")
    post_id = request.json['id'][-1]
    color = request.json['color']
    print(post_id)
    print(color)
    db = get_db()
    color = db.execute(
        'UPDATE post SET task_color = ?'
        'WHERE id = ?',
        (color,post_id)
    )
    db.commit()
    return redirect(url_for('blog.index'))
    