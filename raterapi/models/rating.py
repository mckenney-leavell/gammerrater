from django.db import models
from django.contrib.auth.models import User

CHOICES = [(i,i) for i in range(11)]

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="rating")
    rating = models.IntegerField(choices=CHOICES)
    review = models.TextField()