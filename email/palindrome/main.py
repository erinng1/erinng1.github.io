import webapp2
import jinja2
import os
import random


def is_palindrome(word):
	first_half = None
	second_half = None


	if len(word) % 2 == 0:
		first_half = len(word) / 2
		second_half = len(word) / 2
	else:
		first_half = (len(word) / 2) + 1
		second_half = len(word) / 2

	first_half = word[:first_half]
	second_half = word[second_half:]
	second_half = second_half[::-1]	

	if first_half == second_half:
		return word + ' is a palindrome!'
	else:
		return word + ' is not a palindrome...'
		
class MainHandler(webapp2.RequestHandler):
    def get(self):
		palindrome = is_palindrome('kayak')
		self.response.write(palindrome)

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class TemplateHandler(webapp2.RequestHandler):
	def get(self):
		palindrome = is_palindrome('kayak')
		#see lfancyaddhandler for temp change
		#template = jinja_environment.get_template("temp.html")
		self.response.write(template.render(
			{'palindrome': palindrome}
			))
			
class FCHandler(webapp2.RequestHandler):
	def get(self):
		fortune = ['you will graduate', 'you will step on a lego', 'you will encounter a dog today']
		pickFort = random.choice(fortune)
		template = jinja_environment.get_template("fortune.html")
		self.response.write(template.render(
			{'fortune' : pickFort}))
			
class FancyAddHandler(webapp2.RequestHandler):
	def get(self): 
		x = random.randint(0,1000)
		y = random.randint(0,1000)
		answer = x + y
		template = jinja_environment.get_template("temp.html")
		self.response.write(template.render(
			{'answer' : answer}))	

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/template', TemplateHandler),
    ('/fc', FCHandler),
    ('/fa', FancyAddHandler)
], debug=True)
