from django.db import models
from django.contrib.auth.models import User

class GameImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images_uploaded")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='images')
    url = models.CharField(max_length=500)