from django.contrib.auth import authenticate, login, logout


######################################################################
####LOGOUT PAGE
@view_function
def logout(request):
	logout(request)
	
	return HttpResponseRedirect('/homepage/')
