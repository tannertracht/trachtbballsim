from corestuff.generateplayer import Player
from .models import Team

def createteam(newip = 0):
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
	
	
	# New Opposing Team
	
	pointguard = Player(1)
	shootingguard = Player(2)
	smallforward = Player(3)
	powerforward = Player(4)
	center = Player(5)
	newOpposingTeam = Team()
	newOpposingTeam.PointGuardFirstName = pointguard.firstName
	newOpposingTeam.PointGuardLastName = pointguard.lastName
	newOpposingTeam.PointGuardWeight = pointguard.weight
	newOpposingTeam.PointGuardHeight = pointguard.height
	newOpposingTeam.PointGuardScoring = pointguard.scoring
	newOpposingTeam.PointGuardPassing = pointguard.passing
	newOpposingTeam.PointGuardDefense = pointguard.defense
	newOpposingTeam.ShootingGuardFirstName = shootingguard.firstName
	newOpposingTeam.ShootingGuardLastName = shootingguard.lastName
	newOpposingTeam.ShootingGuardWeight = shootingguard.weight
	newOpposingTeam.ShootingGuardHeight = shootingguard.height
	newOpposingTeam.ShootingGuardScoring = shootingguard.scoring
	newOpposingTeam.ShootingGuardPassing = shootingguard.passing
	newOpposingTeam.ShootingGuardDefense = shootingguard.defense
	newOpposingTeam.SmallForwardFirstName = smallforward.firstName
	newOpposingTeam.SmallForwardLastName = smallforward.lastName
	newOpposingTeam.SmallForwardWeight = smallforward.weight
	newOpposingTeam.SmallForwardHeight = smallforward.height
	newOpposingTeam.SmallForwardScoring = smallforward.scoring
	newOpposingTeam.SmallForwardPassing = smallforward.passing
	newOpposingTeam.SmallForwardDefense = smallforward.defense
	newOpposingTeam.PowerForwardFirstName = powerforward.firstName
	newOpposingTeam.PowerForwardLastName = powerforward.lastName
	newOpposingTeam.PowerForwardWeight = powerforward.weight
	newOpposingTeam.PowerForwardHeight = powerforward.height
	newOpposingTeam.PowerForwardScoring = powerforward.scoring
	newOpposingTeam.PowerForwardPassing = powerforward.passing
	newOpposingTeam.PowerForwardDefense = powerforward.defense
	newOpposingTeam.CenterFirstName = center.firstName
	newOpposingTeam.CenterLastName = center.lastName
	newOpposingTeam.CenterWeight = center.weight
	newOpposingTeam.CenterHeight = center.height
	newOpposingTeam.CenterScoring = center.scoring
	newOpposingTeam.CenterPassing = center.passing
	newOpposingTeam.CenterDefense = center.defense
	newOpposingTeam.ip = 0
	
	# Set new user teams opposing team to new opposing teams primary keys
	newTeam.OpposingTeam = 0
	newOpposingTeam.OpposingTeam = 0
	
	# Save both new teams to create the pk
	
	newOpposingTeam.save()
	newTeam.save()
	
	# set the pks to opposite teams
	newTeam.OpposingTeam = newOpposingTeam.pk
	newOpposingTeam.OpposingTeam = newTeam.pk
	
	# Save again
	newOpposingTeam.save()
	newTeam.save()
	

		
		





		

