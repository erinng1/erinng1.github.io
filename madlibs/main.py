import webapp2
import jinja2
import os
import urllib2
import json

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class MadlibsHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('ml.html')
		self.response.write(template.render())

	def post(self):
		charName = self.request.get('charName')
		pronoun = self.request.get('pro')
		adjective = self.request.get('adj')
		adjective2 = self.request.get('adj2')
		adjective3 = self.request.get('adj3')
		animal = self.request.get('animal')
		food = self.request.get('food')

		template = jinja_environment.get_template('ml_out.html')
		self.response.write(template.render({
		'charName' : charName,
		'pro' : pronoun,
		'adj' : adjective,
		'adj2' : adjective2,
		'adj3' : adjective3,
		'animal' : animal,
		'food' : food,
		}))

class RandomHandler(webapp2.RequestHandler):
	def get(self): 
		response = urllib2.urlopen('https://randomuser.me/api/?results=10')
		content = response.read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template('user.html')
		self.response.out.write(template.render({
				'contents' : content_dictionary
			}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/madlibs', MadlibsHandler),
    ('/random', RandomHandler),
], debug=True)
