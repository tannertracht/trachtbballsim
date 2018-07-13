from django.db import models

class Team(models.Model):
	ip = models.GenericIPAddressField()
	PointGuardFirstName = models.CharField(max_length = 30)
	PointGuardLastName = models.CharField(max_length = 30)
	PointGuardHeight = models.CharField(max_length = 5)
	PointGuardWeight = models.CharField(max_length = 3)
	PointGuardScoring = models.IntegerField()
	PointGuardPassing = models.IntegerField()
	PointGuardDefense = models.IntegerField()
	ShootingGuardFirstName = models.CharField(max_length = 30)
	ShootingGuardLastName = models.CharField(max_length = 30)
	ShootingGuardHeight = models.CharField(max_length = 5)
	ShootingGuardWeight = models.CharField(max_length = 3)
	ShootingGuardScoring = models.IntegerField()
	ShootingGuardPassing = models.IntegerField()
	ShootingGuardDefense = models.IntegerField()
	SmallForwardFirstName = models.CharField(max_length = 30)
	SmallForwardLastName = models.CharField(max_length = 30)
	SmallForwardHeight = models.CharField(max_length = 5)
	SmallForwardWeight = models.CharField(max_length = 3)
	SmallForwardScoring = models.IntegerField()
	SmallForwardPassing = models.IntegerField()
	SmallForwardDefense = models.IntegerField()
	PowerForwardFirstName = models.CharField(max_length = 30)
	PowerForwardLastName = models.CharField(max_length = 30)
	PowerForwardHeight = models.CharField(max_length = 5)
	PowerForwardWeight = models.CharField(max_length = 3)
	PowerForwardScoring = models.IntegerField()
	PowerForwardPassing = models.IntegerField()
	PowerForwardDefense = models.IntegerField()
	CenterFirstName = models.CharField(max_length = 30)
	CenterLastName = models.CharField(max_length = 30)
	CenterHeight = models.CharField(max_length = 5)
	CenterWeight = models.CharField(max_length = 3)
	CenterScoring = models.IntegerField()
	CenterPassing = models.IntegerField()
	CenterDefense = models.IntegerField()
	
	
	def __str__(self):
		return self.ip
	