import cherrypy
class Welcome(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

