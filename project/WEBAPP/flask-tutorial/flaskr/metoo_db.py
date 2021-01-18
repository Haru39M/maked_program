# ここから↓サイトのやつ
from flaskr.db import get_db

# データベースからmetooを取得
def get_metoo():
    table = 'eval'
    id_list = get_id_list(table)
    id_one = id_list('evaluated_post_id')
    sql = 'SELECT metoo FROM '+ table + ' WHERE id ='+ str(id_one)
    metoo = execute_sql(sql)
    # 取得データは一つだけなのでここで0を指定しておく
    return metoo[0]

# DBに接続してsqlを実行
def execute_sql(sql):
    db = get_db()
    db.execute(sql)
    result = db.fetchall()
    db.close()
    return result

# 指定したtableのID一覧を取得
def get_id_list(table):
    sql = 'SELECT evaluated_post_id FROM '+ table
    id_list = execute_sql(sql)
    return id_list