# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from forms import LogForm   
from .models import GeneralLogger
from forms import LogForm

def LogViewTemplate(request):
    if request.method == 'POST':
        tmp = LogForm(request.GET)
        if tmp.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        tmp = LogForm()
    return render(request, 'logger.html', { 'form': tmp })

def SaveLogFromTemplate(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            path = cleaned['usr_filepath']
            message = cleaned['message']
            GeneralLogger(message=message, usr_filepath=path, sys_time=timezone.now()).save()
            return render(request, 'log-template-submit-thank.html', {})
        else:
            print(form.errors)
    return HttpResponse('<h3>Some error occurred while rendering the form</h3>')