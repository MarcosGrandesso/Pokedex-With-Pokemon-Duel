import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from pokedex.base.models import Duelo, DueloSerializer, Pokemon

# from base.poke_svc import serializa_pokes


def dapau(request):
    raise Exception("break on purpose")


def create_pokemon(request):

    body = request.body
    data = json.loads(body.decode("utf-8"))

    Pokemon.objects.create(
        title=data["title"],
        type=data["type"],
        img_url=data["img_url"],
        hp=data["hp"],
        armor=data["armor"],
        attack=data["attack"],
    )
    return HttpResponse()


def get_pokemons(request):
    pokemons_do_usuario_logado = Pokemon.objects.filter(owner_id=request.user.id)
    data = serializers.serialize("json", pokemons_do_usuario_logado)
    return JsonResponse(data, safe=False)


def get_duelos(request):
    duelos_disponiveis = Duelo.objects.filter(winner__isnull=True).exclude(
        challenger_id=request.user.id
    )

    serializer = DueloSerializer(duelos_disponiveis, many=True)

    return JsonResponse(serializer.data, safe=False)


def finish_duelo(request):
    body = request.body
    data = json.loads(body.decode("utf-8"))

    vencedor = User.objects.get(id=data["winner"]["owner"])
    duelo = Duelo.objects.get(id=data["duel"]["pk"])
    premio = Pokemon.objects.get(title=data["loser"]["title"])

    duelo.winner = vencedor.id
    premio.owner_id = vencedor.id
    premio.save()
    duelo.save()

    return JsonResponse({}, safe=False)


def create_duelo(request):
    body = request.body
    data = json.loads(body.decode("utf-8"))

    poke = Pokemon.objects.get(title=data["name"])
    Duelo.objects.create(challenger_id=request.user.id, pokemon_id=poke.id)
    return JsonResponse({}, safe=False)
