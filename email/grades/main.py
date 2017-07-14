import jinja2
import os
import webapp2

from google.appengine.ext import ndb
 

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))
 
class Student(ndb.Model):
	name = ndb.StringProperty()
	LName = ndb.StringProperty()
	grade = ndb.IntegerProperty()
	school = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('student_input.html')
		self.response.write(template.render())#limit=2))

	def post(self):
		name = self.request.get('studentName')
		LName = self.request.get('studentLName')
		school = self.request.get('studentSchool')
		grade = self.request.get('studentGrade')
		grade = int(grade)
		student_model = Student(name = name, LName = LName, school = school, grade = grade)
		student_key = student_model.put()


		template = jinja_environment.get_template('student_added.html')
		self.response.write(template.render(
			{
			'name': name
			}))

class OneStudentHandler(webapp2.RequestHandler):
	def get(self):
		student_id = self.request.get('id')
		student_id = int(student_id)
		one_student = Student.get_by_id(student_id)
		template = jinja_environment.get_template('onestudent.html')
		self.response.write(template.render(
			{
			'student': one_student
			}))

class ListHandler(webapp2.RequestHandler):
	def get(self):
		student_query = Student.query(Student.grade >= 70).order(-Student.grade)
		list_of_students = Student.query().fetch()
		template = jinja_environment.get_template('list.html')
		self.response.write(template.render({'students' : list_of_students}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/list', ListHandler),
	('/onestudent', OneStudentHandler),
], debug=True)