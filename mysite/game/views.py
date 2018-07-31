from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Team
from .forms import LoginForm
from .startgame import createteam
from .simulation import RunSim
from .updatemodels import updatePlayer

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
					form = LoginForm()
					return render(request, 'game/home.html', {'form': form, 'exists': 'Team name is already taken'})
				user = User.objects.create_user(username = form.cleaned_data["team_name"], password = form.cleaned_data["team_password"])
			request.session['user'] = user.pk
			login(request, user)
			return HttpResponseRedirect('sim')
			
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect('sim')
		else:
			form = LoginForm()
			return render(request, 'game/home.html', {'form': form})



def simulationscreen(request):
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
		createteam(user)
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
			
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	
	
	
	
	
	
	
	
	