function post_metoo() {
    //window.alert("metoo 2 clicked!");
    $.ajax({
        type: 'POST',
        url: '/metoo_post',//このURLにアクセスされるとjsonを返す
        data: '',
        contentType: 'application/json',
    })
    .then(
        // 1つめは通信成功時のコールバック
        function (data) {
            $("#results").append(data);
        },
        // 2つめは通信失敗時のコールバック
        function () {
            alert("読み込み失敗");
            console.log;
    });
  }