import re
from django.db import models
from django.core.exceptions import ValidationError

def validation_email(value):
	regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
	match = re.match(regex,value)
	if match is None:
		raise ValidationError("Not a valid email")
	return value




"""
python manage.py makemigrations: Every time you change models.py(Its just a setting up
the database changes)

python manage.py migrate: That actually ran the database changes(It actually runs them)
"""
# Create your models here.
#In this we are going to store information of the studnet

class Student(models.Model):
	courses = [
	('python','Python'),
	('java','Java'),
	('ror','Ruby on Rails'),
	('js','JavaScript'),
	('npm','NodeJs'),
	]
	name = models.CharField(max_length=120)
	contact = models.PositiveIntegerField()
	course = models.CharField(max_length=250, choices=courses)
	# email = models.EmailField(null=True, blank=True) #built in validation
	# mobile = models.PositiveIntegerField(null=True, blank=True) #built in validation
	created = models.DateTimeField(auto_now_add=True, blank=True)
	active = models.BooleanField(default=True)
	#active = models.BooleanField(null=True) #This is not a fine way
	#active = models.NullBooleanField() #this will work
	#for more about the fields please check the mention link
	#https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types
	"""
blank=True, null=True: blank=Truelet Django know that time filed can is optional.
If time filed is not provided, null=Trueallow database save NULL for the time field.
	"""
	email = models.CharField(max_length=240,null=True,blank=True,validator=[validation_email])
	#custom validation for this email, it dosent make any sense but just for better understanding the validation
	#for Python 3x version
	def __str__(self):
		return self.name

	"""
	for Python 2x version
	def __unicode__(self):
		return self.name

	"""
	# class Meta:
	# 	unique_together = [('email','mobile')] both email and mobile will be unique togeather.

