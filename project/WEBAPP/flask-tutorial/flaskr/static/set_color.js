function post_color(ele,color) {//pythonへ送る情報の前処理。htmlからデータをとってきてresultという名前のjson形式にする
    // window.alert("clicked!");//動作チェック用
    // window.alert("color is "+color);
    var id_value = ele.id;//投稿のidをとってくる
    // window.alert("id_value is "+id_value);
    var result = JSON.stringify({"id":id_value,"color":color}); // eleのプロパティとしてidを取得し、id_valueというjsonにする
    var url = '/set_color';
    // window.alert(url);
    // window.alert(result);//動作チェック用
    $.ajax({//指定したurlにdataを送る。成功or失敗でthen以降の処理が分岐する。
      type: 'POST',
      url: url,//このURLにアクセスする。blog.pyの/metoo_postがついてる関数が実行されてjsonがjsに返される
      data: result,//データには最初は何も入っていない
      contentType: 'application/json',
    }).then(
      function (data){//成功したときの処理。この中は見かけの書き換え。pythonから返されたjsonからデータを取ってきて書き換える。
        // window.alert("success!");//動作チェック用
        //↓index.htmlに書いたid = metoo の部分を、pythonから送られたjsonデータに書き換える処理。
        // var color = JSON.parse(data.ResultSet).color//.metooのところはpythonから送られたjsonのキー。metoo数はpython側で既に+1されている。
        // var post_id = JSON.parse(data.ResultSet).id//.idのところはpythonから送られたjsonのキー
        // document.getElementById('color-disp').innerHTML = 'changed'//index.htmlのid="metoo"を探してタグに囲まれた値をmetooに書き換える
        changecolor(color,id_value);
      },
      function (){
        window.alert("failed!");
      }
    )
  }
  function changecolor(color_num,id){
    var color_array = {0:'#00000008',1:'#D43761',2:'#EBAC48',3:'#5A4FF6',4:'#99D437'};
    document.getElementById('color-disp-'+id).style.backgroundColor = color_array[color_num];
  }