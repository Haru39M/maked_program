function post_metoo(ele) {//pythonへ送る情報の前処理。htmlからデータをとってきてresultという名前のjson形式にする
    // window.alert("clicked!");//動作チェック用
    var id_value = ele.id;//投稿のidをとってくる
    var metoo = $('#metoo_value'+ele.id).text();
    var result = JSON.stringify({"id":id_value,"metoo":metoo}); // eleのプロパティとしてidを取得し、id_valueというjsonにする
    // window.alert(result);//動作チェック用
    $.ajax({//指定したurlにdataを送る。成功or失敗でthen以降の処理が分岐する。
      type: 'POST',
      url: '/metoo_post',//このURLにアクセスする。blog.pyの/metoo_postがついてる関数が実行されてjsonがjsに返される
      data: result,//データには最初は何も入っていない
      contentType: 'application/json',
    }).then(
      function (data){//成功したときの処理。この中は見かけの書き換え。pythonから返されたjsonからデータを取ってきて書き換える。
        // window.alert("success!");//動作チェック用
        // window.alert(data);
        // console.log("testlog");
        // const metoo = JSON.parse(data.ResultSet).metoo//.metooのところは←jsonのキー.index.htmlに書いたid = metoo の部分にjsonデータから取り出して入れる。
        document.getElementById('metoo_value'+ele.id).innerHTML = Number(metoo)+1//index.htmlのid="metoo"を探してタグに囲まれた値をmetooに書き換える
      },
      function (){
        window.alert("failed!");
      }
    )
  }