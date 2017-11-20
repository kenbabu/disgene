# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request
from django.views.generic import TemplateView
import  services

# Create your views here.

class OntologyMapView(TemplateView):
	def get(self, request):
		onto_list = services.map_ontologies('diabetes')
		context = {'onto_list': onto_list}
		return render(request, 'ontomap_list.html', context)

