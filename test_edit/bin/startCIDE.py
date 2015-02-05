import sys
from cherrypy import (config as server_conf,
                      quickstart,
                      engine,
                      tools)
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from test_edit.index import Welcome

conf = sys.argv[1]
server_conf.update(conf)

WebSocketPlugin(engine).subscribe()
tools.websocket = WebSocketTool()

quickstart(Welcome(), "/", conf)
