from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='index'),
    path('academic-calendar/', calendar, name ='calendar'),
<<<<<<< HEAD
    path('school_fee/',school_fee, name='school_fee')
]
=======
]
>>>>>>> cbc8ab5d28d437ac5f2355fa3abcff7f9149c16f
