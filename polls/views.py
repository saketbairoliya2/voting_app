from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, World. This is just the demo, lets see you on that side of the things.")
