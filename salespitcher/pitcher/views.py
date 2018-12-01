from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView
#from django.http import HttpResponse

# Create your views here.
#'''
class index(TemplateView):
	template_name = "index.html"

class new_player(TemplateView):
	template_name = "new_player.html"

class loading_area(TemplateView):
	template_name = "loading.html"

class game_room(TemplateView):
	template_name = "game_room.html"
#'''

'''
def index(request):
	return render(request, 'index.html',{})

def new_player(request):



	return render(request, 'new_player.html', {})

def loading_area(request):
	return render(request, 'loading.html',{})

def game_room(request):
	return render(request, 'game_room.html',{})


# functions...
def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		return x_forwarded_for.split(',')[-1].strip()
	return request.META.get('REMOTE_ADDR')

#'''