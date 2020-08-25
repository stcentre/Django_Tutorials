from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect 
from .models import *
from .forms import *
from django.urls import reverse

#views take some sort of the url and they return a response

#This is just a hard coded view This is not what we want to do at all its just an for first understanding
def home(request):
	print(request) #print wsgi get request 
	print(dir(request)) #print the availble methods thaat we can use on particular request
	print(request.method) #print the method which http method
	print(request.get_full_path()) #/ the url that is being routed on this function
	return HttpResponse("<h2>This is my first View that is on home page </h2>")

"""
When we are making a request or when a request happens there are couple of thinngs that go on.
One of them is it goes through this concept called middleware which is basically like this 
middle ground between a request and a response.
Middelware does some stuff in between coming to this actual function.
So basically when a request happen to our website our website send back a response and 
Django handles that interchange by going first through middelware like first its routed and 
then it goes through middleware and then it goes to a view and then he goes back through
middleware and then its goes back to the user.
"""
#dynamic response
def home1(request):
	response = HttpResponse()
	response.write("<p>This is my another home1 fucntion</p>")
	response.write("<p>This is my another home1 fucntion</p>")
	response.write("<p>This is my another home1 fucntion</p>")
	response.write("<p>This is my another home1 fucntion</p>")
	print(response.status_code) #wil print 200
	"""
	response.write(<h2>Page not Found</h2>)
	response.write(<h6>(404)</h6>)
	response.status_code = 404
	#this is how you can make your own page not found.
There are stuff for django built in but its was just for showing how we can make our own
	"""
	return response
	#either you can write the stuff in shell or in views
	#return HttpResponseRedirect('https://github.com/aman64039/Advance_Python_Tutorials')
	#will redirect to given url

"""
Four Diffrent views that we are going to want to have for a lot of our apps.This is a very
important concept when it comes to building web application in our views because with this
concept our entire app is going to built on. So lets have a look.
CRUD : Create , Retrieve , Update , Delete
"""
def list_view(request):
	#orm query to retrive the data availble in the database
	list_data = Student.objects.all()
	return HttpResponse(list_data)

"""
Template Rendring:
Template Rending allows us to make html smarter.We can render a template by a fucntion name as 
render which is defualt imported in views file from django shortcuts.
render function consist of 3 parameter named as request , path of the template and context(in dict)
"""
def list_view_template(request):
	#orm query to retrive the data availble in the database
	list_data = Student.objects.all()
	return render(request,'myapp/firstview.html',{'data':list_data})
"""
Lets you wnat to get the detail of the person on the basis of his id
#we can implement by this
data = Student.objects.get(id=1)
#perfectly work but what if the id is not availble we will get an error taht dosent exist
#instead of this we can handle it by showing 404 by using follwing way
try:
	data = data = Student.objects.get(id=1)
except:
	#django built in 404
	raise Http404

#Another way
data = get_object_or_404(Student,id=10)
#we can also use the filter that we discuss later on

"""
def list_view_template1(request,id=None):
	#orm query to retrive the data availble in the database
	list_data = get_object_or_404(Student,id=id)
	return HttpResponse(list_data)

#createView
def create_view(request):
	form = StudentForm()
	print(request.method)
	#one way
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			data = Student.objects.all()
			print(data)
			HttpResponseRedirect('/create_view')
		form = StudentForm()
	return render(request,'myapp/create.html',{'form':form})
	#another way of getting the form
	#form = StudentForm(request.POST or None)

def update_view(request,id = None):
	data = get_object_or_404(Student,id=id)
	form = StudentForm(request.POST or None , instance=data)
	if form.is_valid():
		data = form.save()
		data.save()
		return HttpResponseRedirect(reverse('list_view_template'))
	return render(request,'myapp/update.html',{'form':form,'data':data})


def search_view(request):
	pass