import cherrypy
from genshi.template import TemplateLoader

from time import sleep
from pdb import set_trace as dbg

template_dir = "templates"
loader = TemplateLoader(template_dir, auto_reload=True, max_cache_size=100)
 
class Welcome(object):
    
    @cherrypy.expose
    def index(self):
        sleep(5)
        return "hello4"
        #dbg()
        #tmpl = loader.load('template1.html')
        #return tmpl