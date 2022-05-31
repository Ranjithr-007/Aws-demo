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
    path('society-registration-certificate', society_registration_certificate, name='society_registration_certificate'),
    path('pta/', pta, name='pta'),
    path('smc/', school_managing_commitee, name='school_managing_commitee'),
    path('building-safety', building_safety, name='building_safety'),
    path('fire-safety', fire_safety, name='fire_safety'),
    path('deo', deo, name='deo'),
]

