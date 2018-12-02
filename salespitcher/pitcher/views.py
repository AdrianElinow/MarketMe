from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse
from .forms import NewPlayerForm, TaglineForm, Vote

#'''
def index(request):
	return render(request, 'index.html',{})

def new_player(request):
	if request.method == "POST":
		form = NewPlayerForm(request.POST)
		if form.is_valid():
			# submit username here
			return HttpResponseRedirect( reverse('loading') )
	else:
		form = NewPlayerForm(initial={'player_name':'player'})

	context = {'form': form}

	return render(request, 'new_player.html', context)

def loading_area(request):
	return render(request, 'loading.html',{})

def game_room(request):
	return render(request, 'game_room.html',{})

# functions...

def submit_tagline(request):
	if request.method == 'POST':
		form = TaglineForm(request.POST)
		print("FORM ->->->",form)
		#
		

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		return x_forwarded_for.split(',')[-1].strip()
	return request.META.get('REMOTE_ADDR')

#'''