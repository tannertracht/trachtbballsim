from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Team, Player, Season
from .forms import LoginForm
from .startgame import createteam
from .simulation import RunSim
from .updatemodels import updatePlayer
import random

# Create your views here.
def index(request):
	#User.objects.all().delete()
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data["team_name"], password=form.cleaned_data["team_password"])
			if user is None:
				# No backend authenticated the credentials
				print("User doesn't exist, create user")
				if User.objects.filter(username= form.cleaned_data["team_name"]).exists():
					print("name exists")
					form = LoginForm()
					return render(request, 'game/home.html', {'form': form, 'exists': 'Team name is already taken'})
				user = User.objects.create_user(username = form.cleaned_data["team_name"], password = form.cleaned_data["team_password"])
			request.session['user'] = user.pk
			print(user.pk)
			login(request, user)
			return HttpResponseRedirect('sim')
			
	else:
		if request.user.is_authenticated:
			print("already auth")
			return HttpResponseRedirect('sim')
		else:
			form = LoginForm()
			
			return render(request, 'game/home.html', {'form': form})



def simulationscreen(request, is_season = False):
	#Team.objects.all().delete()
	# If user went directly to /sim/ and bypassed logging in error will occur. Need to check if user is logged in before 
	# Returning a view
	if request.user.is_authenticated == False:
		return HttpResponseRedirect('/')
	user = request.session['user']
	teams = Team.objects.filter(User=user).count()
	if teams >= 1:
		# If team already exists with this IP
		print("User Team Exists")
	else:
		# If team doesn't exist yet
		createteam(user, True)
		print("Creating Team")

	team = Team.objects.get(User=user)
	opposingTeam = Team.objects.get(OpposingTeam = team.pk)
	return render(request, 'game/simscreen.html', {'PointGuard': team.PointGuard, 'ShootingGuard': team.ShootingGuard, 'SmallForward': team.SmallForward, 'PowerForward': team.PowerForward, 'Center': team.Center,
							'OpposingPointGuard': opposingTeam.PointGuard, 'OpposingShootingGuard': opposingTeam.ShootingGuard, 'OpposingSmallForward': opposingTeam.SmallForward, 'OpposingPowerForward': opposingTeam.PowerForward, 'OpposingCenter': opposingTeam.Center})
		
def simulation(request):
	user = request.session['user']
	gameResults = RunSim(user)
	return JsonResponse(gameResults)
	
def coaching(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect('/')
	user = request.session['user']
	team = Team.objects.get(User=user)
	player_dict = {'PointGuard': team.PointGuard, 'ShootingGuard': team.ShootingGuard, 'SmallForward': team.SmallForward, 'PowerForward': team.PowerForward, 'Center': team.Center}
	return render(request, 'game/coachesoffice.html', player_dict)
	
def coachingupdate(request):
	user = request.session['user']
	updatePlayer(user, request.POST)
	return HttpResponse('saved')
			
			
def season_view(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect('/')
		
	user = request.session['user']
	team = Team.objects.get(User=user)
	season = Season.objects.get(UserTeam = team)
	free_agents = list(Player.objects.filter(FreeAgent = True).order_by('?')[:3])
	player_dict = {'PointGuard': team.PointGuard, 'ShootingGuard': team.ShootingGuard, 'SmallForward': team.SmallForward, 'PowerForward': team.PowerForward, 'Center': team.Center, 'FreeAgentOne': free_agents[0], 'FreeAgentTwo': free_agents[1], 'FreeAgentThree': free_agents[2],
					'WeekOneResult': season.WeekOneResult, 'WeekTwoResult': season.WeekTwoResult, 'WeekThreeResult': season.WeekThreeResult, 'WeekFourResult': season.WeekFourResult, 'WeekFiveResult': season.WeekFiveResult, 'WeekSixResult': season.WeekSixResult, 'WeekSevenResult': season.WeekSevenResult,
						'WeekEightResult': season.WeekEightResult, 'WeekNineResult': season.WeekNineResult, 'Record': season.Record}
	return render(request, 'game/seasonscreen.html', player_dict)
			
			
def seasonsim(request):
	return simulationscreen(request, is_season = True)
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	
	
	
	
	
	
	
	
	