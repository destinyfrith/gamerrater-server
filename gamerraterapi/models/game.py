from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    number_of_players = models.IntegerField()
    year_released = models.IntegerField()
    time_to_play = models.CharField(max_length=50)
    age_recommendation = models.IntegerField()
    gamer = models.ForeignKey("Gamer", null=True, on_delete=models.CASCADE)
