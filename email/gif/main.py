import webapp2
import json
import urllib2
import jinja2
import os
from urllib import urlencode

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('gif.html')
		self.response.write(template.render())

	def post(self):
		q = self.request.get("sQuery")
		api_key = 'dc6zaTOxFJmzC'
		limit = 20
		rating = 'g' #'pg'
		parameters = {'q': q, 'api_key': api_key, 'limit': limit, 'rating': rating}
		giphy_data_source = urllib2.urlopen(
		"http://api.giphy.com/v1/gifs/search?"+urlencode(parameters))
		giphy_json_content = giphy_data_source.read()
		parsed_giphy_dictionary = json.loads(giphy_json_content)
		gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
		# self.response.write(gif_url)
		contents = parsed_giphy_dictionary
		template = jinja_environment.get_template('search.html')
		self.response.write(template.render({
				'contents': contents,
			}))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
