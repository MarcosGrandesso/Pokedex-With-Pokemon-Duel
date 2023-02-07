from django.urls import path

from . import views

urlpatterns = [
    path("dapau", views.dapau),
    path("create-pokemon", views.create_pokemon)
]
