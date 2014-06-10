from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')
def user(request, offset):
	return HttpResponse("User is %s" %offset)