from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='index'),
    path('academic-calendar/', calendar, name ='calendar'),
    path('school-fee/',school_fee, name='school_fee'),
    path('noc/', noc, name='noc'),
    path('rte/', rte, name='rte'),
    path('water-sanitation-certificate/', water_sanitation_certificate, name='water_sanitation_certificate'),
    path('school_fee/',school_fee, name='school_fee'),

]

