function command (command, data, port, callback) {
    var sendData = {
        "command":command,
        "kwargs":data
    };
    $.getJSON(
        self.location.hostname + ':' + port.toString(),
        sendData,
        callback
    );
}