from django import forms

class SearchForm(forms.Form):
	search_term = forms.CharField(label='Search Term')

	def  valid_term(self):
		data = self.cleaned_data['search_term']
		if len(data) < 3:
			raise forms.ValidationError("Input keyword is too short!")
		return data
