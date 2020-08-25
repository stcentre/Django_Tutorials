from django.db import models

# Create your models here.
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
	created = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name
