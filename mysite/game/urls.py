from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='homescreen'),
	path('sim', views.simulationscreen, name='simulationscreen'),
	path('simulation', views.simulation, name='simulation'),
	path('coaching', views.coaching, name='coaching'),
	path('coachingupdate', views.coachingupdate, name='coachingupdate'),
	]
