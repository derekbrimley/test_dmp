from django import forms

class UserForm(forms.Form):
	first_name = forms.CharField(max-length=50)
	last_name = forms.CharField(max-length=50)
	username = forms.CharField(max-length=50)
	password = forms.CharField(max-length=50)
	