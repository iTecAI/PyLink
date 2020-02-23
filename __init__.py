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
            try:
                code, data = self.link.commands[command_json['command']](command_json['kwargs'])
                self.send_response(code)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(data),'utf-8'))
            except KeyError:
                self.send_response(404)
                self.end_headers()

    def __init__(self,ip,server_port,api_port,directory=None,python_path='python',**commands):
        self.server = None
        self.api = ThreadingHTTPServer((ip,api_port),BaseHTTPRequestHandler)
        self.commands = commands
        self.python_path = python_path
        self.ip = ip
        self.server_port = server_port
        self.directory = directory
    
    def serve_forever(self):
        self.server = Popen([self.python_path,self.ip,self.server_port,str(self.directory)])
        self.api.serve_forever()
