from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

# Create your models here.


class Pokemon(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    img_url = models.CharField(max_length=10000, default=None, null=True, blank=True)
    hp = models.IntegerField()
    armor = models.IntegerField()
    attack = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Duelo(models.Model):
    challenger = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    winner = models.TextField(default=None, blank=True, null=True)


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class ChallengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DueloSerializer(serializers.ModelSerializer):
    challenger = ChallengerSerializer()
    pokemon = PokemonSerializer()

    class Meta:
        model = Duelo
        fields = ["pk", "challenger", "pokemon"]
