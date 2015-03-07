from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod
import random

templater = get_renderer('account')

@view_function
def process_request(request):
	params = {}

	if request.user.is_authenticated():
		user = hmod.User.objects.get(username=request.user)
		user_id = user.id
		params['user_id'] = user_id

	return templater.render_to_response(request, 'index.html',params)