import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class EmailHandler(webapp2.RequestHandler):
	def get(self):
		emails = [
		  {'title': 'help', 'sender': 'fakeaccount@gmail.com'},
		  {'title': 'money pls', 'sender': 'fakeaccount@gmail.com'},
		  {'title': 'hey!', 'sender': 'a_friend@gmail.com'},
		  {'title': 'spam', 'sender': 'fakeaccount@gmail.com'},
		  {'title': 'day 11 hmwk', 'sender': 'drb@hampton.edu'},
		]
		template = jinja_environment.get_template('email.html')
		self.response.write(template.render({
					'emails': emails
				}))

class SumHandler(webapp2.RequestHandler):
	def get(self):
		first_num = self.request.get('num1')
		second_num = self.request.get('num2')

		total_sum = int(first_num) + int(second_num)

		template = jinja_environment.get_template('url.html')
		self.response.write(template.render(
			{
				'first_num' : first_num,
				'second_num' : second_num,
				'total_sum' : total_sum
			}))

class MoviesReviewHandler(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('name')
		length = self.request.get('length')
		num_reviews = self.request.get('num_reviews')
		stars = self.request.get('stars')

		template = jinja_environment.get_template('url.html')
		self.response.write(template.render(
			{
				'name' : name, 'length' : length, 'num_reviews' : num_reviews, 'stars' : stars, 
			}))

class MadlibHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('madlib.html')
		self.response.write(template.render())

	def post(self):
		charName = self.request.get('charName')
		adj = self.request.get('adj')
		adj2 = self.request.get('adj2')
		cartoon = self.request.get('cartoon')
		game = self.request.get('game')

		template = jinja_environment.get_template('madlib_out.html')
		self.response.write(template.render({
		'adj' : adj,
		'adj2' : adj2,
		'character' : charName,
		'cartoon' : cartoon,
		'game' : game,
		}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/email', EmailHandler),
    ('/sum', SumHandler),
    ('/movie', MoviesReviewHandler),
    ('/madlib', MadlibHandler)
], debug=True)
