from django.urls import path, include, reverse, re_path
from .views import *

urlpatterns = [
    path('', book, name='book'),
]