# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 
from django.views.generic import FormView, View
from django.http import JsonResponse

from .forms import ContactForm

# Create your views here.

class ContactView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		template = "contact.html"
		return render(request, template, context)


class ContactFormView(FormView):
	form_class = ContactForm
	template_name = 'contact/contact.html'
	success_url = '/contact-created/'

	def form_invalid(self, form):
		response = super(ContactFormView, self).form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
	def form_valid(self, form):
		response = super(ContactFormView, self).form_invalid(form)
		print form.cleaned_data
		if self.request.is_ajax():
			print(form.cleaned_data)
			data = {
				'message': "Successfully submitted form data"
			}
			return JsonResponse(data)
		else:
			return response


def contact(request):
	title = 'Contact'
	form = ContactForm(request.POST or None)
	confirm_message = None
	if form.is_valid():
		# print request.POST
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = "Message from Dive Team"
		message = '{0} {1}'.format(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo  = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
		title = "Thanks!"
		confirm_message = "Thanks for the message. We will get right back to you as soon as possible"
		form = None
	context = { 'title': title,  'form': form , 'confirm_message': confirm_message, }
	template = 'contact.html'
	return render(request, template, context)

