from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('account')

@view_function
def process_request(request):
	
	params = {}
	#user = hmod.User.object.get(id=request.session)
  
	return templater.render_to_response(request, 'account_info.html')