from django.shortcuts import render_to_response


def index(request):
	return render_to_response('index.html')


def user(request, id=None):
	pass

def team(request, id=None):
	pass