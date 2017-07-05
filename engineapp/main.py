import webapp2
import random

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class FCHandler(webapp2.RequestHandler):
    def get(self):
		fortunes = ['something bad', 'something good', 'something mysterious']
		rand_fortune = random.choice(fortunes)
		self.response.write(rand_fortune) 

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fort', FCHandler)
], debug=True)
