# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings 

from django.template import loader, Context
from django.views.generic import FormView, View, TemplateView

from django.http import HttpResponse
import requests
from ontomap import services

from contact.forms import (
	ContactForm,
	TestForm,
	)

# Create your views here.

def search(request):
	form = TestForm()
	template = 'testform.html'
	zooma_url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue='
	error = False
	context= {'error':error, 'form':form}
	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			error = True
			return render(request, template, context)
		else:
			zooma_data = requests.get(zooma_url+'{0}'.format(name)).json()

			context = {'error':error, 'form':form, 'zooma_data': zooma_data, 'name':name}
	return render(request, template, context)

class ContactFormView(FormView):
	form_class = ContactForm
	template_name = 'contact.html'
	success_url = reverse_lazy('ontomaplist')

	def get_context_data(self, **kwargs):
		context = super(ContactFormView, self).get_context_data(**kwargs)
		context['jina'] = "Dread Pirate Roberts"
		print context
		return context

	def form_valid(self, form):
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = "Message from Dive Team"
		message = '{0} {1}'.format(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo  = [settings.EMAIL_HOST_USER]
		

		# template = loader.get_template('contact_template.txt')
		# context  = {
		# 	'contact_name': name,
		# 	'contact_email': emailFrom,
		# 	'message' : message
		# 	}
		# content = template.render(context)
		
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
		# print context
		return super(ContactFormView, self).form_valid(form)

class TestFormView(FormView):
	form_class = TestForm
	template_name = 'testform.html'
	success_url = reverse_lazy('searchtest')

	def form_valid(self, form):
		name = form.cleaned_data['name']
		jina = self.request.GET['name']

		# print(super(TestFormView, self).get_context_data(**kwargs))
		return super(TestFormView, self).form_valid(form)
	

	# def get_context_data(self, **kwargs):
	# 	context = super(TestFormView, self).get_context_data(**kwargs)
	# 	context['jina'] = "Enron"
	# 	return context



