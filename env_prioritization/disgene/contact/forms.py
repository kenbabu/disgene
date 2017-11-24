from django import forms
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
class ContactForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, required=False)
	email = forms.EmailField()
	comment = forms.CharField(label='Comment', widget=forms.Textarea)

class TestForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, required=False,)
	