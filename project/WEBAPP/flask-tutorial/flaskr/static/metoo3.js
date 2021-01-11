$(document).ready(function() {
    //formのsubmitボタンをクリック
    $('#form').on('submit', function (event) {
        //Ajax通信
        $.ajax({
            // data: {
            //     //form内inputの値、リクエスト(POST or GET),リクエスト先のURLを記述
            //     firstname: $('#firstname').val(),
            //     lastname: $('#lastname').val(),
            // },
            type: 'POST',
            url: '/'
        })
            //formの下に結果を表示
            .done(function (data) {
                $('#output').text(data.output).show();
            });
        event.preventDefault();
    });
});