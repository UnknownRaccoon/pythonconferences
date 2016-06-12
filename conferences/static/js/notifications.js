$(function() {
    if(window.location.pathname.search('^/chat') === -1) {
        var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        var notification_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host +
            '/notifications?user=' + user);
        var counter = 0;
        notification_socket.onmessage = function(message) {
            var data = JSON.parse(message.data);
            var body = $('#notifications');
            var ele = $('<div id="notification' + counter + '"></div>');
            ele.append($("<p></p>").text(data.text));
            ele.append($("<p></p>").text(data.sender));
            counter++;
            body.append(ele);
            ele.fadeOut(5000);
        };
    }
});
