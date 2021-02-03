function post_metoo(ele) {//pythonへ送る情報の前処理。htmlからデータをとってきてresultという名前のjson形式にする
    // window.alert("clicked!");//動作チェック用
    var id_value = ele.id;//投稿のidをとってくる
    var metoo_value = $('#metoo'+ele.id).text();
    var result = JSON.stringify({"id":id_value,"metoo":metoo_value}); // eleのプロパティとしてidを取得し、id_valueというjsonにする
    // window.alert(result);//動作チェック用
    $.ajax({//指定したurlにdataを送る。成功or失敗でthen以降の処理が分岐する。
      type: 'POST',
      url: '/metoo_post',//このURLにアクセスする。blog.pyの/metoo_postがついてる関数が実行されてjsonがjsに返される
      data: result,//データには最初は何も入っていない
      contentType: 'application/json',
    }).then(
      function (data){//成功したときの処理。この中は見かけの書き換え。pythonから返されたjsonからデータを取ってきて書き換える。
        // window.alert("success!");//動作チェック用
        //↓index.htmlに書いたid = metoo の部分を、pythonから送られたjsonデータに書き換える処理。
        var metoo = JSON.parse(data.ResultSet).metoo//.metooのところはpythonから送られたjsonのキー。metoo数はpython側で既に+1されている。
        var post_id = JSON.parse(data.ResultSet).id//.idのところはpythonから送られたjsonのキー
        document.getElementById('metoo'+post_id).innerHTML = metoo//index.htmlのid="metoo"を探してタグに囲まれた値をmetooに書き換える
      },
      function (){
        window.alert("failed!");
      }
    )
  }