from homepage.forms import UserForm

def user_form_upload(request)
	if request.method == 'GET':
		form = UserForm()
	else: