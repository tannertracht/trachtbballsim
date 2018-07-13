from corestuff.generateplayer import Player
from .models import Team

def createteam(newip):
	pointguard = Player(1)
	shootingguard = Player(2)
	smallforward = Player(3)
	powerforward = Player(4)
	center = Player(5)
	newTeam = Team()
	newTeam.PointGuardFirstName = pointguard.firstName
	newTeam.PointGuardLastName = pointguard.lastName
	newTeam.PointGuardWeight = pointguard.weight
	newTeam.PointGuardHeight = pointguard.height
	newTeam.PointGuardScoring = pointguard.scoring
	newTeam.PointGuardPassing = pointguard.passing
	newTeam.PointGuardDefense = pointguard.defense
	newTeam.ShootingGuardFirstName = shootingguard.firstName
	newTeam.ShootingGuardLastName = shootingguard.lastName
	newTeam.ShootingGuardWeight = shootingguard.weight
	newTeam.ShootingGuardHeight = shootingguard.height
	newTeam.ShootingGuardScoring = shootingguard.scoring
	newTeam.ShootingGuardPassing = shootingguard.passing
	newTeam.ShootingGuardDefense = shootingguard.defense
	newTeam.SmallForwardFirstName = smallforward.firstName
	newTeam.SmallForwardLastName = smallforward.lastName
	newTeam.SmallForwardWeight = smallforward.weight
	newTeam.SmallForwardHeight = smallforward.height
	newTeam.SmallForwardScoring = smallforward.scoring
	newTeam.SmallForwardPassing = smallforward.passing
	newTeam.SmallForwardDefense = smallforward.defense
	newTeam.PowerForwardFirstName = powerforward.firstName
	newTeam.PowerForwardLastName = powerforward.lastName
	newTeam.PowerForwardWeight = powerforward.weight
	newTeam.PowerForwardHeight = powerforward.height
	newTeam.PowerForwardScoring = powerforward.scoring
	newTeam.PowerForwardPassing = powerforward.passing
	newTeam.PowerForwardDefense = powerforward.defense
	newTeam.CenterFirstName = center.firstName
	newTeam.CenterLastName = center.lastName
	newTeam.CenterWeight = center.weight
	newTeam.CenterHeight = center.height
	newTeam.CenterScoring = center.scoring
	newTeam.CenterPassing = center.passing
	newTeam.CenterDefense = center.defense
	newTeam.ip = newip
	newTeam.save()
	

		
		





		

