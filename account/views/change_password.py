from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import password_reset
from django.core.mail import send_mail

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
	
###################################################
####FORGOT PASSWORD
@view_function
def forgot_password(request):
	params = {}
	
	form = ForgotPasswordForm()
	
	if request.method == "POST":
		username = request.POST['username']
		user = hmod.User.objects.get(username=username)
		email = user.email
		
		password_reset(request)
		# send_mail('Password Reset', 'Click the link below to reset your password. If you did not request a new password, disregard this email. The link below will expire in 24 hours. If you have any questions, please call 801-422-8080', 'group13chf@gmail.com',[email], fail_silently=False)
		
	params['form'] = form
	return templater.render_to_response(request,'change_password.forgot_password.html',params)
	
	
class ForgotPasswordForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username'
			}
		),
	)
	
	
	

	
	
	
	
	
	
	