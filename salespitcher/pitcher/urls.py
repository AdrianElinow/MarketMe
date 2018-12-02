from django.conf.urls import url

from . import views

#'''
urlpatterns = [
	url(r'^pitcher/', views.index, name='index'),
	url(r'^index$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^new_player/$', views.new_player, name="new_player"),
	#url(r'^get_player_name/$', views.get_player_name, name="get_player_name"),
	url(r'^gameroom/$', views.game_room, name='gameroom'),
	url(r'^loading/$', views.loading_area, name='loading'),
	#url(r'^$' views.index, name='index'),
]
#'''