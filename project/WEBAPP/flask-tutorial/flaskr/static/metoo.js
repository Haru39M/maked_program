function post_metoo() {
    window.alert("clicked!");
    $.ajax({
      type: 'POST',
      url: '/metoo_post',//このURLにアクセスされるとjsonを返す
      data: '',
      contentType: 'application/json',
      success: function (data) {
        window.alert("success!");
        window.alert("success2");
        const metoo = JSON.parse(data.ResultSet).metoo//.metooのところは←jsonのキー.index.htmlに書いたid = metoo の部分にjsonデータから取り出して入れる。blog.pyでデータベースから取り出したデータをjsonにして、/metoo_postにアクセスされるとidにデータを入れる
        const test = "234"//試験用
        document.getElementById('metoo').innerHTML = metoo
        document.getElementById('test').innerHTML = test//試験用
      }
    })
  }