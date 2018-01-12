# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import request
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .forms import SearchForm
import  services

# Create your views here.

class OntologyMapView(TemplateView):
    template_name = 'ontomap_list.html'
    def get_context_data(self, *args, **kwargs):
        onto_list = services.map_ontologies('diabetes')
        term = "diabetes"

    		# context = {'ontology_list': onto_list}
    	return  super(OntologyMapView, self).get_context_data(*args, **kwargs)


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'ontomap.html'
    succes_url =reverse_lazy('ontomap-list')

    def form_valid(self, form):
        term = form.cleaned_data['search_term']
        sonto_list = services.map_ontologies(term)

        # print context
        return super(SearchFormView, self).form_valid(form)
    def get_context_data(self, *args, **kwargs):
        context = super(SearchFormView, self).get_context_data(*args, **kwargs)
        term = "This is my term"
        sonto_list = services.map_ontologies(term)
        return context
        

