from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home2', views.home1, name = 'home1'),
    path('list_view', views.list_view, name = 'list_view'),
    path('list_view_template', views.list_view_template, name = 'list_view_template'),
    path('<int:id>', views.list_view_template1, name = 'list_view_template1'),
    path('create_view', views.create_view, name = 'create_view'),
    path('<int:id>/edit', views.update_view, name = 'update_view'),

]
