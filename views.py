from django.shortcuts import render
from .models import Friend
# Create your views here.


def home(request): 
	friends = Friend.objects
	return render(request, 'home.html', {'friends':friends})
