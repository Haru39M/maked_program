DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
-- DROP TABLE IF EXISTS eval;/* add for metoo */

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,/*ユーザーIDをプライマリキーとして宣言*/
  username TEXT UNIQUE NOT NULL,
  token TEXT DEFAULT NULL,/*pushbulletのトークン*/
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,/* 投稿のID */
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  nowtime TEXT,
  metoo INTEGER NOT NULL DEFAULT 0,
  task_color INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (author_id) REFERENCES user (id)/*著者IDを外部キーとすることでユーザーIDを紐付け。*/
  
);
/*MeToo機能用*/
-- CREATE TABLE eval(
--   evaluated_post_id INTEGER NOT NULL,/*評価された投稿のID。評価の合計がこのIDに紐付けられる*/
--   /*evaluated_author_id INTEGER NOT NULL,/*評価された人(著者)のID*/
--   /*evaluated_user_id INTEGER NOT NULL,/*評価した人(ユーザー)のID*/
--   /*isevaluated INTEGER NOT NULL DEFAULT 0,/* 評価したかどうかを保持しておく。0か1。これはユーザーごとに持っている値。評価ボタンが押された際に、+1するか-1するかをこの値によって決める */
--   metoo INTEGER NOT NULL DEFAULT 0,/*MeToo!の数を保存しておく。evaluated_idと同テーブルなので投稿ごとの評価を入れている*/
--   FOREIGN KEY (evaluated_post_id) REFERENCES post(id)/*評価を投稿ごとに付けるために、評価された投稿のIDと投稿IDを紐付け*/
--   /*FOREIGN KEY (evaluated_author_id) REFERENCES user(id)/*評価された人のIDをユーザーIDに紐付け*/
-- );