import random
import webapp2
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('worlderinn.html')
        self.response.write(template.render())

class CountHandler(webapp2.RequestHandler):
    def get(self):
    	for i in range(10):
    		self.response.write(i),
    		self.response.write('<br>')

class ErinnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Erinn')

class FCHandler(webapp2.RequestHandler):
    def get(self):
		fortunes = ['something bad', 'something good', 'something mysterious']
		rand_fortune = random.choice(fortunes)
		self.response.write(rand_fortune) 

class AdditionHandler(webapp2.RequestHandler):
    def get(self):
    	x = random.randint(0, 100)
    	y = random.randint(0,100)
        logging.info(x)
        logging.info(y)
        self.response.write(x + y)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/erinn', ErinnHandler),
    ('/fc', FCHandler),
   	('/add', AdditionHandler)
], debug=True)
