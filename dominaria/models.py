from email.policy import default
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class Matchup(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='winner', null=True, blank=True, on_delete=models.CASCADE)
    games_won_by_p1 = models.PositiveIntegerField(default=0)
    games_won_by_p2 = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    # this is for when players are allowed to report their own matchups
    # reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("player1", "player2")

    def __str__(self):
        return str(self.player1) + ' vs. ' + str(self.player2)