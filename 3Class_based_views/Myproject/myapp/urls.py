from django.contrib import admin
from django.urls import path , include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.HomeView.as_view(), name = 'first'),
	path('someview/', views.SomeView.as_view(), name = 'someview'),
	path('about', TemplateView.as_view(template_name='myapp/about.html'), name = 'about'),

]
