from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    year_released = models.IntegerField()
    player_count = models.IntegerField()
    est_play_time = models.IntegerField()
    age_recommendation = models.IntegerField()