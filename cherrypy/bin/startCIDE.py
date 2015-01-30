import sys, os
from cherrypy import (config as server_conf, 
                      quickstart)
from cide.index import Welcome


from pdb import set_trace as dbg

#conf = dict()
#conf['server.socket_host'] = '0.0.0.0'
#conf['server.socket_port'] = 8080
#conf['server.threadPool'] = 20 # does not seems to work
#conf['server.threadpool'] = 20

conf = {
  '/': {
    'tools.sessions.on': True,
     'tools.staticdir.root': os.path.abspath(os.getcwd())
  },
  '/static': {
    'tools.staticdir.on': True,
    'tools.staticdir.dir': './public'
  }
}

server_conf.update(conf)
quickstart(Welcome(), "/", conf)
