from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='index'),
    path('academic-calender/', calender, name ='calender'),
]
