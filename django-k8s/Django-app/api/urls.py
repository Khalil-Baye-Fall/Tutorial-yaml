from django.urls import path
from .views import *


urlpatterns = [
    path('home', Welcome, name='Welcome'),
    path('second', SecondPage, name='Second Page')
]