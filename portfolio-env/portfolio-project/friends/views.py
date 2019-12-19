from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def intro(request):
	return render(request, 'intro.html')

def find(request):
	return render(request, 'find.html')

def write(request):

	return render(request, 'write.html' )

def info(request):
	return render(request, 'info.html')

def signin(request):
	return render(request, 'signin.html')





	
# Create your views here.
