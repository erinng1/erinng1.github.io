import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from datetime import datetime

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Student(ndb.Model):
	name = ndb.StringProperty()
	timestamp = ndb.DateTimeProperty()
	uni = ndb.StringProperty()
	study = ndb.StringProperty()
	hobby = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('datain.html')
		self.response.write(template.render())

	def post(self):
		name = self.request.get('name')
		uni = self.request.get('uni')
		study = self.request.get('study')
		hobby = self.request.get('hobby')
		timestamp = datetime.now()
		data_model = Student(name = name, uni = uni, study = study, hobby = hobby, timestamp = timestamp)
		data_key = data_model.put()

class OneUserHandler(webapp2.RequestHandler):
	def get(self):
		# name = self.request.get('name')
		# uni = self.request.get('uni')
		# study = self.request.get('study')
		# hobby = self.request.get('hobby')
		# data_model = Student(namem = name, uni = uni, study = study, hobby = hobby)
		data_key = Student.query().order(-Student.timestamp)
		data_name = data_key.get().name
		data_uni = data_key.get().uni
		data_study = data_key.get().study
		data_hobby = data_key.get().hobby
		#data_query = Student.query().fetch(limit=1)
		#list_of_data = data_query.fetch(limit=1)
		template = jinja_environment.get_template('oneu.html')
		self.response.write(template.render({
			'name' : data_name,
			'uni' : data_uni,
			'study' : data_study,
			'hobby' : data_hobby
		}))

class UserOutputHandler(webapp2.RequestHandler):
	def get(self):
		data_query = Student.query()
		list_of_data = Student.query().fetch()
		template = jinja_environment.get_template('dataout.html')
		self.response.write(template.render({'data' : list_of_data}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/oneu', OneUserHandler),
    ('/dout', UserOutputHandler),
], debug=True)
