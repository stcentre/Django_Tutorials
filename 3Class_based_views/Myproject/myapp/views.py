from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect 
from .models import *
from .forms import *
from django.urls import reverse
from django.views.generic import TemplateView , View

"""
Class Based views give us a lot of shortcuts from function based views.
The things about classes and classbased view is Inheritance.Thats the biggest advantages of Class Based views
over the function based views is because our functions cant actually inhert from another function but 
as we know classes can be.
"""
#context 
class HomeView(TemplateView):
	template_name = 'myapp/firstview.html'
	def get_context_data(self,*args,**kwargs):
		context = super(HomeView, self).get_context_data(*args,**kwargs)
		context["name"]="Amanpreet Singh"
		return context

class SomeView(View):
	def get(self,request):
		return HttpResponse("Hello Some View")