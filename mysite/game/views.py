from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team
from .startgame import createteam
from .simulation import RunSim

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
	PointGuardInfo = [team.PointGuard.FirstName, team.PointGuard.LastName, team.PointGuard.Weight, 
					team.PointGuard.Height, team.PointGuard.Scoring, team.PointGuard.Passing, team.PointGuard.Defense]
	ShootingGuardInfo = [team.ShootingGuard.FirstName, team.ShootingGuard.LastName, team.ShootingGuard.Weight, 
					team.ShootingGuard.Height, team.ShootingGuard.Scoring, team.ShootingGuard.Passing, team.ShootingGuard.Defense]
	SmallForwardInfo = [team.SmallForward.FirstName, team.SmallForward.LastName, team.SmallForward.Weight, 
					team.SmallForward.Height, team.SmallForward.Scoring, team.SmallForward.Passing, team.SmallForward.Defense]					
	PowerForwardInfo = [team.PowerForward.FirstName, team.PowerForward.LastName, team.PowerForward.Weight, 
					team.PowerForward.Height, team.PowerForward.Scoring, team.PowerForward.Passing, team.PowerForward.Defense]
	CenterInfo = [team.Center.FirstName, team.Center.LastName, team.Center.Weight, 
					team.Center.Height, team.Center.Scoring, team.Center.Passing, team.Center.Defense]
	
	OpposingPointGuardInfo = [opposingTeam.PointGuard.FirstName, opposingTeam.PointGuard.LastName, opposingTeam.PointGuard.Weight, 
					opposingTeam.PointGuard.Height, opposingTeam.PointGuard.Scoring, opposingTeam.PointGuard.Passing, opposingTeam.PointGuard.Defense]
	OpposingShootingGuardInfo = [opposingTeam.ShootingGuard.FirstName, opposingTeam.ShootingGuard.LastName, opposingTeam.ShootingGuard.Weight, 
					opposingTeam.ShootingGuard.Height, opposingTeam.ShootingGuard.Scoring, opposingTeam.ShootingGuard.Passing, opposingTeam.ShootingGuard.Defense]
	OpposingSmallForwardInfo = [opposingTeam.SmallForward.FirstName, opposingTeam.SmallForward.LastName, opposingTeam.SmallForward.Weight, 
					opposingTeam.SmallForward.Height, opposingTeam.SmallForward.Scoring, opposingTeam.SmallForward.Passing, opposingTeam.SmallForward.Defense]					
	OpposingPowerForwardInfo = [opposingTeam.PowerForward.FirstName, opposingTeam.PowerForward.LastName, opposingTeam.PowerForward.Weight, 
					opposingTeam.PowerForward.Height, opposingTeam.PowerForward.Scoring, opposingTeam.PowerForward.Passing, opposingTeam.PowerForward.Defense]
	OpposingCenterInfo = [opposingTeam.Center.FirstName, opposingTeam.Center.LastName, opposingTeam.Center.Weight, 
					opposingTeam.Center.Height, opposingTeam.Center.Scoring, opposingTeam.Center.Passing, opposingTeam.Center.Defense]
	
	return render(request, 'game/home.html', {'PointGuard': PointGuardInfo, 'ShootingGuard': ShootingGuardInfo, 'SmallForward': SmallForwardInfo, 'PowerForward': PowerForwardInfo, 'Center': CenterInfo,
							'OpposingPointGuard': OpposingPointGuardInfo, 'OpposingShootingGuard': OpposingShootingGuardInfo, 'OpposingSmallForward': OpposingSmallForwardInfo, 'OpposingPowerForward': OpposingPowerForwardInfo, 'OpposingCenter': OpposingCenterInfo})
		
def simulation(request):
	newip = get_client_ip(request)
	gameResults = RunSim(newip)
	#print(gameResults)
	return JsonResponse(gameResults)
		
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip			