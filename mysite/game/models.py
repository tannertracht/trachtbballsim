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
	FreeAgent = models.BooleanField(default = False)
	
	
class Team(models.Model):
	PointGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pointguard')
	ShootingGuard = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shootingguard')
	SmallForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='smallforward')
	PowerForward = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='powerforward')
	Center = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='center')
	User = models.IntegerField()
	OpposingTeam = models.IntegerField()
	
class Season(models.Model):
	UserTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='userteam')
	Record = models.CharField(max_length = 5)
	CurrentWeek = models.IntegerField(default = 1)
	WeekOneOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekOne')
	WeekTwoOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekTwo')
	WeekThreeOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekThree')
	WeekFourOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekFour')
	WeekFiveOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekFive')
	WeekSixOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekSix')
	WeekSevenOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekSeven')
	WeekEightOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekEight')
	WeekNineOpponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='WeekNine')
	WeekOneResult = models.CharField(max_length = 9)
	WeekTwoResult = models.CharField(max_length = 9)
	WeekThreeResult = models.CharField(max_length = 9)
	WeekFourResult = models.CharField(max_length = 9)
	WeekFiveResult = models.CharField(max_length = 9)
	WeekSixResult = models.CharField(max_length = 9)
	WeekSevenResult = models.CharField(max_length = 9)
	WeekEightResult = models.CharField(max_length = 9)
	WeekNineResult = models.CharField(max_length = 9)
	
	