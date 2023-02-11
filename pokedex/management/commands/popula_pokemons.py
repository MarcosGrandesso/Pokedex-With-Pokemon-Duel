import requests
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from pokedex.base.models import Duelo, Pokemon


class Command(BaseCommand):
    help = "popula pokes"

    def handle(self, *args, **kwargs):
        # pokelist = {'title':'bug', 'type':'bug', 'img_url': "hhh",'hp': 11,'armor': 44,'attack':50, }
        # for poke in pokelist:
        #     Pokemon.objects.create(title=poke['title'], type=poke['type'],
        #     img_url=poke['img_url'],hp=poke["hp"], armor=poke['armor'],
        #      attack=poke['attack'])
        # pokemons_list = []

        for i in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
            response = requests.get(url)
            pokemon_data = response.json()

            # pokemon = {
            #     "title": pokemon_data["name"],
            #     "type": pokemon_data["types"][0]["type"]["name"],
            #     "img_url": pokemon_data["sprites"]["front_default"],
            #     "hp": pokemon_data["stats"][5]["base_stat"],
            #     "armor": pokemon_data["stats"][3]["base_stat"],
            #     "attack": pokemon_data["stats"][4]["base_stat"],
            # }
            Pokemon.objects.create(
                title=pokemon_data["name"],
                type=pokemon_data["types"][0]["type"]["name"],
                img_url=pokemon_data["sprites"]["front_default"],
                hp=pokemon_data["stats"][5]["base_stat"],
                armor=pokemon_data["stats"][3]["base_stat"],
                attack=pokemon_data["stats"][4]["base_stat"],
            )

        user = User.objects.create_user(username='adm',password='password')
        Duelo.objects.create(challenger_id=user.id, pokemon_id=48)
        self.stdout.write(self.style.SUCCESS("pokemon criando"))
