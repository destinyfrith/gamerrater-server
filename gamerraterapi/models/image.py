from django.db import models

class Image(models.Model):
    
    image = models.CharField(max_length=55)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)