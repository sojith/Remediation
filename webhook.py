from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
from urllib.parse import unquote
from json.encoder import JSONEncoder
import json
import os

class handler_class(CGIHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200, message="Sojith Sugadan")
        self.end_headers()
        print(self.headers['Content-Length'])
        payload=str(self.rfile.read(int(self.headers['Content-Length'])))
#        print(payload)
        payload_formatted = payload.replace('b\'','').replace('\\n','').replace('\'','')
#        print(payload_formatted)  
        payload_json=json.loads(payload_formatted)     
        print(payload_json)          
        print(str(payload_json["ProblemTitle"]))
        os.system('ssh mint@192.168.225.138 sh /home/mint/Projects/Monitoring/Remediation/trigger.sh')

server_class=HTTPServer
#handler_class=BaseHTTPRequestHandler

server_address = ('', 8000)
httpd = server_class(server_address, handler_class)
httpd.serve_forever()

