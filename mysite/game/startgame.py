from corestuff.generateplayer import player
from .models import Team, Player

def createteam(newip = 0):
	pointguard = player(1)
	shootingguard = player(2)
	smallforward = player(3)
	powerforward = player(4)
	center = player(5)
	
	modelPG = Player()
	modelSG = Player()
	modelSF = Player()
	modelPF = Player()
	modelC = Player()
	
	modelPG.FirstName = pointguard.firstName
	modelPG.LastName = pointguard.lastName
	modelPG.Weight = pointguard.weight
	modelPG.Height = pointguard.height
	modelPG.Scoring = pointguard.scoring
	modelPG.Passing = pointguard.passing
	modelPG.Defense = pointguard.defense
	modelSG.FirstName = shootingguard.firstName
	modelSG.LastName = shootingguard.lastName
	modelSG.Weight = shootingguard.weight
	modelSG.Height = shootingguard.height
	modelSG.Scoring = shootingguard.scoring
	modelSG.Passing = shootingguard.passing
	modelSG.Defense = shootingguard.defense
	modelSF.FirstName = smallforward.firstName
	modelSF.LastName = smallforward.lastName
	modelSF.Weight = smallforward.weight
	modelSF.Height = smallforward.height
	modelSF.Scoring = smallforward.scoring
	modelSF.Passing = smallforward.passing
	modelSF.Defense = smallforward.defense
	modelPF.FirstName = powerforward.firstName
	modelPF.LastName = powerforward.lastName
	modelPF.Weight = powerforward.weight
	modelPF.Height = powerforward.height
	modelPF.Scoring = powerforward.scoring
	modelPF.Passing = powerforward.passing
	modelPF.Defense = powerforward.defense
	modelC.FirstName = center.firstName
	modelC.LastName = center.lastName
	modelC.Weight = center.weight
	modelC.Height = center.height
	modelC.Scoring = center.scoring
	modelC.Passing = center.passing
	modelC.Defense = center.defense
	
	modelPG.save()
	modelSG.save()
	modelSF.save()
	modelPF.save()
	modelC.save()
	
	newTeam = Team()
	newTeam.PointGuard = modelPG
	newTeam.ShootingGuard = modelSG
	newTeam.SmallForward = modelSF
	newTeam.PowerForward = modelPF
	newTeam.Center = modelC
	newTeam.ip = newip
	
	
	
	
	# New Opposing Team
	
	pointguard = player(1)
	shootingguard = player(2)
	smallforward = player(3)
	powerforward = player(4)
	center = player(5)
	
	CPUmodelPG = Player()
	CPUmodelSG = Player()
	CPUmodelSF = Player()
	CPUmodelPF = Player()
	CPUmodelC = Player()
	
	CPUmodelPG.FirstName = pointguard.firstName
	CPUmodelPG.LastName = pointguard.lastName
	CPUmodelPG.Weight = pointguard.weight
	CPUmodelPG.Height = pointguard.height
	CPUmodelPG.Scoring = pointguard.scoring
	CPUmodelPG.Passing = pointguard.passing
	CPUmodelPG.Defense = pointguard.defense
	CPUmodelSG.FirstName = shootingguard.firstName
	CPUmodelSG.LastName = shootingguard.lastName
	CPUmodelSG.Weight = shootingguard.weight
	CPUmodelSG.Height = shootingguard.height
	CPUmodelSG.Scoring = shootingguard.scoring
	CPUmodelSG.Passing = shootingguard.passing
	CPUmodelSG.Defense = shootingguard.defense
	CPUmodelSF.FirstName = smallforward.firstName
	CPUmodelSF.LastName = smallforward.lastName
	CPUmodelSF.Weight = smallforward.weight
	CPUmodelSF.Height = smallforward.height
	CPUmodelSF.Scoring = smallforward.scoring
	CPUmodelSF.Passing = smallforward.passing
	CPUmodelSF.Defense = smallforward.defense
	CPUmodelPF.FirstName = powerforward.firstName
	CPUmodelPF.LastName = powerforward.lastName
	CPUmodelPF.Weight = powerforward.weight
	CPUmodelPF.Height = powerforward.height
	CPUmodelPF.Scoring = powerforward.scoring
	CPUmodelPF.Passing = powerforward.passing
	CPUmodelPF.Defense = powerforward.defense
	CPUmodelC.FirstName = center.firstName
	CPUmodelC.LastName = center.lastName
	CPUmodelC.Weight = center.weight
	CPUmodelC.Height = center.height
	CPUmodelC.Scoring = center.scoring
	CPUmodelC.Passing = center.passing
	CPUmodelC.Defense = center.defense
	
	CPUmodelPG.save()
	CPUmodelSG.save()
	CPUmodelSF.save()
	CPUmodelPF.save()
	CPUmodelC.save()
	
	newOpposingTeam = Team()
	newOpposingTeam.PointGuard = CPUmodelPG
	newOpposingTeam.ShootingGuard = CPUmodelSG
	newOpposingTeam.SmallForward = CPUmodelSF
	newOpposingTeam.PowerForward = CPUmodelPF
	newOpposingTeam.Center = CPUmodelC
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
	

		
		





		

