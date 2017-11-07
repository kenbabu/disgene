# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
# from django.views import View

# Create your views here.

def home(request):
	return render(request, 'home.html', {"name": "Diseases" })

