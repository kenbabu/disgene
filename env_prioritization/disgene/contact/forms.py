from django import forms
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
class ContactForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, required=False)
	email = forms.EmailField()
	comment = forms.CharField(label='Comment', widget=forms.Textarea)

	def send_mail(self):
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = "Message from Dive Team"
		message = '{0} {1}'.format(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo  = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
		