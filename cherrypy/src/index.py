import os
import cherrypy
from genshi.template import TemplateLoader

from time import sleep
from pdb import set_trace as dbg

template_dir = "templates"
loader = TemplateLoader(template_dir, auto_reload=True, max_cache_size=100)
loader = TemplateLoader(os.path.join(os.path.dirname(__file__), 'templates'),
                                 auto_reload=True) 
class Welcome(object):
    
    @cherrypy.expose
    def index(self):
        cherrypy.session.release_lock()
        sleep(5)
        return "hello4"

    @cherrypy.expose
    def gen(self):
        tmpl = loader.load('template1.html')
        # set args in generate as key1=val1, key2=val2
        stream =  tmpl.generate()
        return stream.render('html')

    @cherrypy.expose
    def gen2(self):
        tmpl = loader.load('template2.html')
        # set args in generate as key1=val1, key2=val2
        stream =  tmpl.generate(var1='banana')
        return stream.render('html')

