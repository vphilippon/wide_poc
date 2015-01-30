import cherrypy
from cide.index import Welcome

# Read configuration ...

#cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(Welcome())
