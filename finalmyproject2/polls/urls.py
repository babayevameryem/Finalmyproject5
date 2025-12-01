# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),     
    path("hello123/", views.hello, name="hello") 
]

