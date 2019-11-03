from django.urls import path, include, reverse, re_path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    re_path(r'^create_status', create_status, name='status')
]