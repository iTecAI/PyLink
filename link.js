function command (command, data, port, callback) {
    var sendData = {
        "command":command,
        "kwargs":data
    };
    $.getJson(
        self.location.hostname + ':' + port.toString(),
        sendData,
        callback
    );
}