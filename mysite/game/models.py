from django.db import models
	
class Player(models.Model):
	FirstName = models.CharField(max_length = 30)
	LastName = models.CharField(max_length = 30)
	Height = models.CharField(max_length = 5)
	Weight = models.CharField(max_length = 3)
	Scoring = models.IntegerField()
	Passing = models.IntegerField()
	Defense = models.IntegerField()
	ShootFirst = models.BooleanField(default = False)
	PassFirst = models.BooleanField(default = False)
	CatchAndShoot = models.BooleanField(default = False)
	HelpDefender = models.BooleanField(default = False)
	DenyShot = models.BooleanField(default = False)
	DenyPass =  models.BooleanField(default = False)
	
	
class Team(models.Model):
	PointGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pointguard')
	ShootingGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shootingguard')
	SmallForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='smallforward')
	PowerForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='powerforward')
	Center = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='center')
	User = models.IntegerField()
	OpposingTeam = models.IntegerField()
	