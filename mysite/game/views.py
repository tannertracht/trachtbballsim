from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team
from .startgame import createteam
from .simulation import RunSim
from .updatemodels import updatePlayer

# Create your views here.
def index(request):
	#Team.objects.all().delete()
	newip = get_client_ip(request)
	teams = Team.objects.filter(ip=newip).count()
	if teams >= 1:
		# If team already exists with this IP
		print("User Team Exists")
	else:
		# If team doesn't exist yet
		createteam(newip)
		print("Creating Team")

	team = Team.objects.get(ip=newip)
	opposingTeam = Team.objects.get(OpposingTeam = team.pk)
	
	return render(request, 'game/home.html', {'PointGuard': team.PointGuard, 'ShootingGuard': team.ShootingGuard, 'SmallForward': team.SmallForward, 'PowerForward': team.PowerForward, 'Center': team.Center,
							'OpposingPointGuard': opposingTeam.PointGuard, 'OpposingShootingGuard': opposingTeam.ShootingGuard, 'OpposingSmallForward': opposingTeam.SmallForward, 'OpposingPowerForward': opposingTeam.PowerForward, 'OpposingCenter': opposingTeam.Center})
		
def simulation(request):
	newip = get_client_ip(request)
	gameResults = RunSim(newip)
	#print(gameResults)
	return JsonResponse(gameResults)
	
def coaching(request):
	teamip = get_client_ip(request)
	team = Team.objects.get(ip=teamip)
	player_dict = {'PointGuard': team.PointGuard, 'ShootingGuard': team.ShootingGuard, 'SmallForward': team.SmallForward, 'PowerForward': team.PowerForward, 'Center': team.Center}
	return render(request, 'game/coachesoffice.html', player_dict)
	
def coachingupdate(request):
	ip = get_client_ip(request)
	updatePlayer(ip, request.POST)
	return HttpResponse('saved')
			
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip			