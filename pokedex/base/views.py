from pokedex.base.models import Pokemon
from django.http import HttpResponse

def dapau(request):
    raise Exception("break on purpose")

def create_pokemon(request):
    print(request)
    # Pokemon.objects.create(
    #     title=,
    #     type=,
    #     img_url=,
    #     hp=,
    #     armor=,
    #     owner=,
    #     attack=
    # )
    a = request.POST['name']
    return HttpResponse(a)