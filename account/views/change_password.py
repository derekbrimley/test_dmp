from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login


templater = get_renderer('account')

######################################################################
####CHANGE PASSWORD
@view_function
def process_request(request):
	params = {}
	
	user = hmod.User.objects.get(username=request.user)
	print('>>>>>>>>>>>>',user.id)
	user_id = user.id
	user_password = user.password
	
	form = ChangePasswordForm()
	
	if request.method=="POST":
		print("post")
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			user.set_password(form.cleaned_data['new_password'])
			user.save()
			password = request.POST['new_password']
			username = user.username
			try:
				user = authenticate(username = username, password = password)
				('>>>>>>>>>>>>',"authenticated")
			except:
				print('>>>>>>>>>>>>not authenticated')
			login(request,user)
			return templater.render_to_response(request,'new_password.html',params)
	params['form'] = form
	
	return templater.render_to_response(request,'change_password.html',params)
	
class ChangePasswordForm(forms.Form):
	new_password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'New Password'
			}
		),
		label = 'New Password',
	)
	
	