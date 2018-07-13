from django.shortcuts import render
from corestuff.generateplayer import Player
from .models import Team
from .startgame import createteam

# Create your views here.
def index(request):
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
	PointGuardInfo = [team.PointGuardFirstName, team.PointGuardLastName, team.PointGuardWeight, 
					team.PointGuardHeight, team.PointGuardScoring, team.PointGuardPassing, team.PointGuardDefense]
	ShootingGuardInfo = [team.ShootingGuardFirstName, team.ShootingGuardLastName, team.ShootingGuardWeight, 
					team.ShootingGuardHeight, team.ShootingGuardScoring, team.ShootingGuardPassing, team.ShootingGuardDefense]
	SmallForwardInfo = [team.SmallForwardFirstName, team.SmallForwardLastName, team.SmallForwardWeight, 
					team.SmallForwardHeight, team.SmallForwardScoring, team.SmallForwardPassing, team.SmallForwardDefense]					
	PowerForwardInfo = [team.PowerForwardFirstName, team.PowerForwardLastName, team.PowerForwardWeight, 
					team.PowerForwardHeight, team.PowerForwardScoring, team.PowerForwardPassing, team.PowerForwardDefense]
	CenterInfo = [team.CenterFirstName, team.CenterLastName, team.CenterWeight, 
					team.CenterHeight, team.CenterScoring, team.CenterPassing, team.CenterDefense]
	return render(request, 'game/home.html', {'PointGuard': PointGuardInfo, 'ShootingGuard': ShootingGuardInfo, 'SmallForward': SmallForwardInfo, 'PowerForward': PowerForwardInfo, 'Center': CenterInfo,
							'OpposingPointGuard': Player(1), 'OpposingShootingGuard': Player(2), 'OpposingSmallForward': Player(3), 'OpposingPowerForward': Player(4), 'OpposingCenter': Player(5)})
							
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip			