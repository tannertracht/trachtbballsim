from .models import Team

def updatePlayer(user, changedict):
	team = Team.objects.get(User=user)
	Oadjustment = changedict["offenseadjustment"]
	Dadjustment = changedict["defenseadjustment"]
	position = changedict["position"]
	if position == "Point Guard Coaching Table":
		changeCoachingAdjustments(team.PointGuard, Oadjustment, Dadjustment)
	elif position == "Shooting Guard Coaching Table":
		changeCoachingAdjustments(team.ShootingGuard, Oadjustment, Dadjustment)
	elif position == "Small Forward Coaching Table":
		changeCoachingAdjustments(team.SmallForward, Oadjustment, Dadjustment)
	elif position == "Power Forward Coaching Table":
		changeCoachingAdjustments(team.PowerForward, Oadjustment, Dadjustment)
	elif position == "Center Coaching Table":
		changeCoachingAdjustments(team.Center, Oadjustment, Dadjustment)



def changeCoachingAdjustments(player, Oadjustment, Dadjustment):
	# If changes were made to the coaching adjustments set everything to false
	# To ensure that only 1 is true at a time
	if Oadjustment != '0':
		player.ShootFirst = False
		player.PassFirst = False
		player.CatchAndShoot = False
		
	if Dadjustment != '0':
		player.HelpDefender = False
		player.DenyShot = False
		player.DenyPass = False
		
	if Oadjustment == '1':
		player.ShootFirst = True
	elif Oadjustment == '2':
		player.PassFirst = True
	elif Oadjustment == '3':
		player.CatchAndShoot = True

	
	
	if Dadjustment == '1':
		player.HelpDefender = True
	elif Dadjustment == '2':
		player.DenyShot = True
	elif Dadjustment == '3':
		player.DenyPass = True
		
	player.save()
	
	

	
		
	


