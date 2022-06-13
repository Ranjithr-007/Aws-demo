import re
from django.contrib import messages
from multiprocessing import context
import os
from urllib import response
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.conf import settings



def homepage(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'We will get back to you shortly!!!')
            return redirect('index')
    return render(request, 'index.html', {'form': form})


def documents(request):
    return render(request, 'documents.html')

def calendar(request):
    return render(request, 'calendar.html')


def school_fee(request):
    return render(request, 'school_fee.html')

def noc(request):
    return render(request, 'noc.html')

def rte(request):
    return render(request, 'rte.html')

def water_sanitation_certificate(request):
    return render(request, 'sanitation_certificate.html')


def society_registration_certificate(request):
    return render(request, 'society_registration_certificate.html')


def pta(request):
    return render(request, 'pta.html')

def school_managing_commitee(request):
    return render(request, 'school_managing_commitee.html')


def building_safety(request):
    return render(request, 'building_safety.html')


def fire_safety(request):
    return render(request, 'fire_safety.html')


def deo(request):
    return render(request, 'deo.html')