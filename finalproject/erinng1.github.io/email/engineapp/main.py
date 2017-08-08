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

class GIFHandler(webapp2.RequestHandler):
	def get(self):
        giphy_data_source = urllib2.urlopen(
            "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write(gif_url)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fort', FCHandler),
    ('/gif', GIFHandler),
], debug=True)
