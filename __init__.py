from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from subprocess import Popen
import json

class PyLink:
    class Handler(BaseHTTPRequestHandler):
        def __init__(self,request, client_address, server, link):
            super().__init__(request, client_address, server)
            self.link = link
        def do_GET(self):
            command_json = json.loads(self.rfile.read())
            code, data = self.link.commands[command_json['command']](command_json['kwargs'])

    def __init__(self,ip,server_port,api_port,directory=None,python_path='python',**commands):
        self.server = None
        self.api = ThreadingHTTPServer((ip,api_port),BaseHTTPRequestHandler)
        self.commands = commands
    
    def serve_forever(self):
        self.server = Popen([python_path,ip,server_port,str(directory)])
        self.api.serve_forever()
