function post_metoo() {
    window.alert("clicked!");
    $.ajax({
      type: 'POST',
      url: '/metoo_post',//このURLにアクセスする。blog.pyの/metoo_postがついてる関数が実行されてjsonがjsに返される
      data: '',//データには最初は何も入っていない
      contentType: 'application/json',
      success: function (data) {
        window.alert("success!");//動作チェック用
        const metoo = JSON.parse(data.ResultSet).metoo//.metooのところは←jsonのキー.index.htmlに書いたid = metoo の部分にjsonデータから取り出して入れる。
        document.getElementById('metoo').innerHTML = metoo//index.htmlのid="metoo"を探してタグに囲まれた値をmetooに書き換える
      }
    })
  }