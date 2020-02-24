function command (command, data, port, callback) {
    var sendData = {
        "command":command,
        "data":data
    };
    $.getJson(
        self.location.hostname + ':' + port.toString(),
        sendData,
        callback
    );
}