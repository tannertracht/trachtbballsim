from corestuff.generateplayer import player, BlankPlayer
from .models import Team
import random

gameResults = {'Posession1OffensePlayer': None, 'Posession1DefensePlayer': None, 'Posession1Result': None, 'Posession1Score': None, 'Posession1RecievedPass': None,
	 'Posession2OffensePlayer': None, 'Posession2DefensePlayer': None, 'Posession2Result': None, 'Posession2Score': None, 'Posession2RecievedPass': None,
	 'Posession3OffensePlayer': None, 'Posession3DefensePlayer': None, 'Posession3Result': None, 'Posession3Score': None, 'Posession3RecievedPass': None,
	 'Posession4OffensePlayer': None, 'Posession4DefensePlayer': None, 'Posession4Result': None, 'Posession4Score': None, 'Posession4RecievedPass': None,
	 'Posession5OffensePlayer': None, 'Posession5DefensePlayer': None, 'Posession5Result': None, 'Posession5Score': None, 'Posession5RecievedPass': None,
	 'Posession6OffensePlayer': None, 'Posession6DefensePlayer': None, 'Posession6Result': None, 'Posession6Score': None, 'Posession6RecievedPass': None,
	 'Posession7OffensePlayer': None, 'Posession7DefensePlayer': None, 'Posession7Result': None, 'Posession7Score': None, 'Posession7RecievedPass': None,
	 'Posession8OffensePlayer': None, 'Posession8DefensePlayer': None, 'Posession8Result': None, 'Posession8Score': None, 'Posession8RecievedPass': None,
	 'Posession9OffensePlayer': None, 'Posession9DefensePlayer': None, 'Posession9Result': None, 'Posession9Score': None, 'Posession9RecievedPass': None,
	 'Posession10OffensePlayer': None, 'Posession10DefensePlayer': None, 'Posession10Result': None, 'Posession10Score': None, 'Posession10RecievedPass': None,}
	 
posessionCount = 1
userTeamScore = 0
opposingTeamScore = 0
shotMakeBarrier = 6
def RunSim(userIp):
	global gameResults
	userTeam, opposingTeam = importTeams(userIp)
	mergedTeams = userTeam
	for i in range(0, 5):
		# Matchup Function
		matchup(userTeam[i], opposingTeam[i], True, userTeam, opposingTeam)
		matchup(opposingTeam[i], userTeam[i], False, opposingTeam, userTeam)

	return gameResults
		
def updateResults(offensePlayer, defensePlayer, result, userOffense, recievedPass):
	global gameResults, posessionCount, userTeamScore, opposingTeamScore
	if result[0] == 1:
		if userOffense:
			userTeamScore += 2
		else:
			opposingTeamScore += 2
	gameResults['Posession{}OffensePlayer'.format(posessionCount)] = [offensePlayer.firstName, offensePlayer.lastName]
	gameResults['Posession{}DefensePlayer'.format(posessionCount)] = [defensePlayer.firstName, defensePlayer.lastName]
	gameResults['Posession{}Result'.format(posessionCount)] = result
	gameResults['Posession{}Score'.format(posessionCount)] = [userTeamScore, opposingTeamScore]
	gameResults['Posession{}RecievedPass'.format(posessionCount)] = recievedPass
	posessionCount += 1
	if posessionCount > 10:
		posessionCount = 1
		userTeamScore = 0
		opposingTeamScore = 0
			
def matchup(offensePlayer, defensePlayer, userOffense, offenseTeam = None, defenseTeam = None, recievedPass = False, passer = None):
	chance = random.randint(1,100)
	newOffenseTeam = offenseTeam[:]
	newDefenseTeam = defenseTeam[:]
	if recievedPass == True:
		passer = passer.firstName + " " + passer.lastName
	if chance <= 50 or recievedPass == True:
		# player shoots
		shotMadeChance = 1 if offensePlayer.scoring <= defensePlayer.defense else offensePlayer.scoring - defensePlayer.defense
		if (shotMadeChance > 6):
			shotMadeChance = 6
		barrier = random.randint(1, shotMakeBarrier)
		if (shotMadeChance >= barrier):
			# Shot made
			updateResults(offensePlayer, defensePlayer, [1, shotMadeChance/shotMakeBarrier, passer] , userOffense, recievedPass)
		else:
			# Shot Missed
			updateResults(offensePlayer, defensePlayer, [2, shotMadeChance/shotMakeBarrier, passer], userOffense, recievedPass)
	else:
		#player passes, calls matchup again
		newOffenseTeam.remove(offensePlayer)
		newDefenseTeam.remove(defensePlayer)
		sortedOffense, matchedDefense = bubbleSort(newOffenseTeam, newDefenseTeam)
		barrier = random.randint(1, 9)
		if offensePlayer.passing >= barrier:
			# Makes Good Pass
			passDestination = random.randint(2,3)
		else:
			# Makes bad pass
			passDestination = random.randint(0,1)
		matchup(sortedOffense[passDestination], matchedDefense[passDestination], userOffense, offenseTeam, defenseTeam, recievedPass = True, passer = offensePlayer)

def bubbleSort(alist, matchedList):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i].scoring>alist[i+1].scoring:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
				newTemp = matchedList[i]
				matchedList[i] = matchedList[i+1]
				matchedList[i+1] = newTemp  
				
	return alist, matchedList
		
				
def importTeams(userIp):
	team = Team.objects.get(ip=userIp)
	opposingTeam = Team.objects.get(OpposingTeam = team.pk)
	UserTeam = [BlankPlayer(1), BlankPlayer(2), BlankPlayer(3), BlankPlayer(4), BlankPlayer(5)]
	OpposingTeam = [BlankPlayer(1), BlankPlayer(2), BlankPlayer(3), BlankPlayer(4), BlankPlayer(5)]
	UserTeam[0].firstName = team.PointGuard.FirstName
	UserTeam[0].lastName = team.PointGuard.LastName
	UserTeam[0].height = team.PointGuard.Height
	UserTeam[0].weight = team.PointGuard.Weight
	UserTeam[0].scoring = team.PointGuard.Scoring
	UserTeam[0].passing = team.PointGuard.Passing
	UserTeam[0].defense = team.PointGuard.Defense
	UserTeam[1].firstName = team.ShootingGuard.FirstName
	UserTeam[1].lastName = team.ShootingGuard.LastName
	UserTeam[1].height = team.ShootingGuard.Height
	UserTeam[1].weight = team.ShootingGuard.Weight
	UserTeam[1].scoring = team.ShootingGuard.Scoring
	UserTeam[1].passing = team.ShootingGuard.Passing
	UserTeam[1].defense = team.ShootingGuard.Defense
	UserTeam[2].firstName = team.SmallForward.FirstName
	UserTeam[2].lastName = team.SmallForward.LastName
	UserTeam[2].height = team.SmallForward.Height
	UserTeam[2].weight = team.SmallForward.Weight
	UserTeam[2].scoring = team.SmallForward.Scoring
	UserTeam[2].passing = team.SmallForward.Passing
	UserTeam[2].defense = team.SmallForward.Defense
	UserTeam[3].firstName = team.PowerForward.FirstName
	UserTeam[3].lastName = team.PowerForward.LastName
	UserTeam[3].height = team.PowerForward.Height
	UserTeam[3].weight = team.PowerForward.Weight
	UserTeam[3].scoring = team.PowerForward.Scoring
	UserTeam[3].passing = team.PowerForward.Passing
	UserTeam[3].defense = team.PowerForward.Defense
	UserTeam[4].firstName = team.Center.FirstName
	UserTeam[4].lastName = team.Center.LastName
	UserTeam[4].height = team.Center.Height
	UserTeam[4].weight = team.Center.Weight
	UserTeam[4].scoring = team.Center.Scoring
	UserTeam[4].passing = team.Center.Passing
	UserTeam[4].defense = team.Center.Defense
	
	OpposingTeam[0].firstName = opposingTeam.PointGuard.FirstName
	OpposingTeam[0].lastName = opposingTeam.PointGuard.LastName
	OpposingTeam[0].height = opposingTeam.PointGuard.Height
	OpposingTeam[0].weight = opposingTeam.PointGuard.Weight
	OpposingTeam[0].scoring = opposingTeam.PointGuard.Scoring
	OpposingTeam[0].passing = opposingTeam.PointGuard.Passing
	OpposingTeam[0].defense = opposingTeam.PointGuard.Defense
	OpposingTeam[1].firstName = opposingTeam.ShootingGuard.FirstName
	OpposingTeam[1].lastName = opposingTeam.ShootingGuard.LastName
	OpposingTeam[1].height = opposingTeam.ShootingGuard.Height
	OpposingTeam[1].weight = opposingTeam.ShootingGuard.Weight
	OpposingTeam[1].scoring = opposingTeam.ShootingGuard.Scoring
	OpposingTeam[1].passing = opposingTeam.ShootingGuard.Passing
	OpposingTeam[1].defense = opposingTeam.ShootingGuard.Defense
	OpposingTeam[2].firstName = opposingTeam.SmallForward.FirstName
	OpposingTeam[2].lastName = opposingTeam.SmallForward.LastName
	OpposingTeam[2].height = opposingTeam.SmallForward.Height
	OpposingTeam[2].weight = opposingTeam.SmallForward.Weight
	OpposingTeam[2].scoring = opposingTeam.SmallForward.Scoring
	OpposingTeam[2].passing = opposingTeam.SmallForward.Passing
	OpposingTeam[2].defense = opposingTeam.SmallForward.Defense
	OpposingTeam[3].firstName = opposingTeam.PowerForward.FirstName
	OpposingTeam[3].lastName = opposingTeam.PowerForward.LastName
	OpposingTeam[3].height = opposingTeam.PowerForward.Height
	OpposingTeam[3].weight = opposingTeam.PowerForward.Weight
	OpposingTeam[3].scoring = opposingTeam.PowerForward.Scoring
	OpposingTeam[3].passing = opposingTeam.PowerForward.Passing
	OpposingTeam[3].defense = opposingTeam.PowerForward.Defense
	OpposingTeam[4].firstName = opposingTeam.Center.FirstName
	OpposingTeam[4].lastName = opposingTeam.Center.LastName
	OpposingTeam[4].height = opposingTeam.Center.Height
	OpposingTeam[4].weight = opposingTeam.Center.Weight
	OpposingTeam[4].scoring = opposingTeam.Center.Scoring
	OpposingTeam[4].passing = opposingTeam.Center.Passing
	OpposingTeam[4].defense = opposingTeam.Center.Defense
	
	return UserTeam, OpposingTeam
	

	
		
	


