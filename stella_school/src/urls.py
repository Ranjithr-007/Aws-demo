from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='index'),
    path('academic-calendar/', calendar, name ='calendar'),
    path('school_fee/',school_fee, name='school_fee'),
]

