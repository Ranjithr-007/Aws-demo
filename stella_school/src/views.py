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

def calendar(request):
    return render(request, 'calender.html')


def school_fee(request):
    return render(request, 'school_fee.html')
