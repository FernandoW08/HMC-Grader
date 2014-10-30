# -*- coding: utf-8 -*-

'''
This module supports all of the forms for the site
'''

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SelectField
from wtforms import TextAreaField, BooleanField, FileField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email



# '''
# Account management forms
# '''
class SignInForm(Form):
	'''
	This form handles logging in a student. The user must enter their username and
	password and if they wish to store their credentials in a cookie they can
	click the remember me button.
	'''
	username = TextField('Username',validators=[Required('Please provide a username')])
	password = PasswordField('Password', validators=[Required()])
	remember = BooleanField('Remember Me')

class ChangePasswordForm(Form):
	'''
	This form allows a user to change their password. They must enter their old
	password and then enter a new password twice.
	'''
	oldPassword = PasswordField('Old Password', validators=[Required()])
	newPassword = PasswordField('New Password', validators=[Required()])
	newPasswordConf = PasswordField('Confirm New Password', validators=[Required()])

#TODO: Refactor to remove these forms
class ChangeFirstNameForm(Form):
	firstName = TextField('First Name')

class ChangeLastNameForm(Form):
	lastName = TextField('Last Name')

class ChangeEmailForm(Form):
	email = TextField('Email', validators=[Email()])


# '''
# Admin panel forms
# '''

class CreateCourseForm(Form):
	'''
	This form handles the creation of a new course.
	'''
	name = TextField("Course Name")
	semester = TextField("Semester")

class CreateUserForm(Form):
	'''
	This form handles the creation of a new user
	'''
	firstName = TextField("First Name")
	lastName = TextField("Last Name")
	username = TextField("Username")
	email = TextField("Email")
	password = PasswordField("Password")


# '''
# Instructor forms
# '''

class CreateAssignmentForm(Form):
	'''
	This form handles the creation of a new assignment group
	'''
	name = TextField("Assignment Group Name", validators=[Required()])

class AddUserCourseForm(Form):
	'''
	This form is for adding new users to a course
	'''
	uname = TextField("Username", validators=[Required()])

class ProblemOptionsForm(Form):
	'''
	This form handles all of the options for a form.
	It includes a hidden time field which contains a UTC ISO-formatted string
	each time the date or time fields change. This allows the system to be
	timezone independant.
	'''
	name = TextField("Problem Name")
	date = TextField("Due Date")
	time = TextField("Due Time")
	allowPartners = BooleanField("Allow Partners")
	hiddentime = TextField("")

class AddTestForm(Form):
	'''
	This form adds a test to a problem.
	'''
	testFile = FileField("File")
	testType = SelectField("Language")

class CourseSettingsForm(Form):
	'''
	This form handles changing course settings. (It may possibly be expanded in
	the future when we decide on more settings)
	'''
	anonymousGrading = BooleanField("Use anonymous grading")


# '''
# Student forms
# '''

class SubmitAssignmentForm(Form):
	'''
	This form handles taking a students files and assigning them a partner.
	'''
	files = FileField("Files")
	partner = SelectField("Partner")
