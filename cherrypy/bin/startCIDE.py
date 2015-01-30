import cherrypy
from cide.index import Welcome

# Read configuration ...

# starts on 8080
#cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(Welcome())
