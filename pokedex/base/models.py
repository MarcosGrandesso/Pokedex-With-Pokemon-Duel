from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pokemon(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    img_url = models.CharField(max_length=10000, default=None, null=True,blank=True)
    hp = models.IntegerField()
    armor = models.IntegerField()
    attack =  models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Duelo(models.Model):
    challenger = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    winner = models.TextField(default=None, blank=True, null=True)