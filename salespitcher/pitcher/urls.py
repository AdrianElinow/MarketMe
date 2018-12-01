from django.conf.urls import url

from . import views

#'''
urlpatterns = [
	url(r'^pitcher/', views.index.as_view(), name='index'),
	url(r'^index$', views.index.as_view(), name='index'),
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^new_player/$', views.new_player.as_view(), name="newplayer"),
	url(r'^gameroom/$', views.game_room.as_view(), name='gameroom'),
	url(r'^loading/$', views.loading_area.as_view(), name='loading'),
	#url(r'^$' views.index, name='index'),
]
#'''