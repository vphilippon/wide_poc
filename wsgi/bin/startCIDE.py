from wsgiref.simple_server import make_server
from cide.server import Server

port = 9889
host = 'localhost'

app = Server()
httpd = make_server(host, port, app)
httpd.serve_forever()