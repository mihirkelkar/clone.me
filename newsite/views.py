from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context
def index(request):
	return render_to_response('index.html')
def user(request, offset):
#	c = Context({'name' : "Mihir Kelkar"})
#	return render(request, "page.html", c)
	return HttpResponse("I am user " + offset)

def make(request):
	return render_to_response("make.html")