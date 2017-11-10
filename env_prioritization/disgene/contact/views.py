# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 

from .forms import ContactForm

# Create your views here.

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

