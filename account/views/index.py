from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random

templater = get_renderer('account')

@view_function
def process_request(request):
  
  #request.session['hey'] = 'world'
  
  #print('>>>>>>>>>>>>>',request.session['hey'])
  
  return templater.render_to_response(request, 'index.html')