from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'ucmiAppUrls'

# Creating our api endpoints
urlpatterns = [
    path('form/', views.Formlist.as_view()),
    path('subscription/', views.Subscriiptionlist.as_view()),

]
