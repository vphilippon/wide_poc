import re
import os

from genshi.template import TemplateLoader
from cide.utilities.controller404 import Controller404

class Server(object):
  
  def __init__(self):
    # map urls to functions
    self.urls = [
      (r'^$', self.index),
      (r'hello/?$', self.hello),
      (r'hello/(.+)$', self.hello),
      (r'template/?$', self.my_template),
      (r'template/(.+)$', self.my_template)
    ]
    
    self.error_404 = Controller404()
    
    # Used to load any template
    self.loader = TemplateLoader(os.path.join(os.path.dirname(__file__), 
                                              'static/templates'),
                                 auto_reload=True)
  
  def __call__(self, environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')    
    for regex, callback in self.urls:
      match = re.search(regex, path)
      if match is not None:
        environ['cide.url_args'] = match.groups()
        return callback(environ, start_response)
    return self.error_404.error(environ, start_response)
  
  def index(self, environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Index - Hello World']
    
  def hello(self, environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello - Hello World']
    
  def my_template(self, environ, start_response):
    tmpl = self.loader.load('template1.html')
    res = b'{0}'.format(tmpl.generate(TestVar="This line was added dynamically"))
    start_response('200 OK', [('Content-Type', 'html')])    
    return [res]
