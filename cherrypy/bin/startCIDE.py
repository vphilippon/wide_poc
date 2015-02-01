import sys, os
from cherrypy import (config as server_conf, 
                      quickstart)
from cide.index import Welcome
from pdb import set_trace as dbg

#static_base_path = os.path.dirname(os.path.abspath(os.getcwd()))

#conf = dict()
#conf = {
#  '/': {
#    'tools.sessions.on': True,
#    'tools.staticdir.root': static_base_path,
#    'tools.sessions.locking': 'explicit'
#  },
#  '/static': {
#    'tools.staticdir.on': True,
#    'tools.staticdir.dir': '..:/public'
#  }
#}

conf = sys.argv[1]
server_conf.update(conf)
quickstart(Welcome(), "/", conf)
