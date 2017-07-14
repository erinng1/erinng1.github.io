import webapp2
import jinja2
import os
from google.appengine.ext import ndb
 

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class Tweet(ndb.Model):
	name = ndb.StringProperty()
	text = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('tweetPage.html')
		self.response.write(template.render(limit=10))

	def post(self):
		name = self.request.get('name')
		text = self.request.get('text')
		stuff = Tweet(name = name, text = text)
		key = stuff.put()

		"""template = jinja_environment.get_template('added_tweet.html')
		self.response.write(template.render(
			{
			'name': name
			}))"""

class TweetLogHandler(webapp2.RequestHandler):
	def post(self):
		tweets_query = Tweet.query().fetch()
		tweets_query.get()
		template = jinja_environment.get_template('tweetPageOut.html')
		self.response.write(template.render({'tweet': tweets_query}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/tweets', TweetLogHandler)
], debug=True)
