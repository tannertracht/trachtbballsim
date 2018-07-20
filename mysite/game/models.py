from django.db import models
	
class Player(models.Model):
	FirstName = models.CharField(max_length = 30)
	LastName = models.CharField(max_length = 30)
	Height = models.CharField(max_length = 5)
	Weight = models.CharField(max_length = 3)
	Scoring = models.IntegerField()
	Passing = models.IntegerField()
	Defense = models.IntegerField()
	
class Team(models.Model):
	PointGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pointguard')
	ShootingGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shootingguard')
	SmallForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='smallforward')
	PowerForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='powerforward')
	Center = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='center')
	ip = models.GenericIPAddressField()
	OpposingTeam = models.IntegerField()
	