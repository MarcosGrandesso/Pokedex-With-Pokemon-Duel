from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
    path(
        "create-pokemon", views.create_pokemon
    ),  # endpoint interno pra eu n ter q consumir a pokeapi
    path("get-pokemon", views.get_pokemons),
    path("get-duelos", views.get_duelos),
    path("finish-duelo", views.finish_duelo),
    path("create-duelo", views.create_duelo),
]
