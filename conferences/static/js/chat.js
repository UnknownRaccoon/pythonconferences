$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname +
        '?companion=' + companion + '&' + 'user=' + user);

    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chat")
        var ele = $('<div></div>')
        ele.append(
            $("<p></p>").text(data.sender)
        )
        ele.append(
            $("<p></p>").text(data.text)
        )
        ele.append(
            $("<p></p>").text(data.date)
        )

        chat.append(ele)
    };

    $("#chatform").on("submit", function(event) {
        var message = {
            //handle: $('#handle').val(),
            message: $('#id_text').val(),
            sender: user,
            recipient: companion,
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
});
