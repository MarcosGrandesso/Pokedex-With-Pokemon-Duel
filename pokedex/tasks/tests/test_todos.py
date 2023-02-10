import json

from model_bakery import baker
from pokedex.accounts.models import User
from pokedex.accounts.tests import fixtures
from pokedex.base.models import Duelo, Pokemon
from pokedex.tasks.models import Todo


def test_criar_tarefa_sem_login(client):
    resp = client.post("/api/tasks/add", {"new_task": "walk the dog"})
    assert resp.status_code == 401


def test_criar_tarefa_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/tasks/add", {"new_task": "walk the dog"})
    assert resp.status_code == 200


def test_criar_tarefa_com_login(client, db):
    fixtures.user_jon()
    Todo.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/tasks/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"todos": [{"description": "walk the dog", "done": False, "id": 1}]}


def test_get_pokemon(client, db):
    user = baker.make(User, username="jon")
    pokemon = baker.make(Pokemon, owner=user)

    client.force_login(user)
    resp = client.post("/api/get-pokemon")
    pok = json.loads(resp.content)
    pok = json.loads(pok)

    assert resp.status_code == 200
    assert pok[0]["fields"]["title"] == pokemon.title


def test_get_duelo(client, db):

    user = baker.make(User, username="jon")
    desafiante = baker.make(User, username="desafiante")
    pokemon = baker.make(Pokemon, owner=user)
    duelo = baker.make(Duelo, challenger_id=desafiante.id, pokemon_id=pokemon.id)

    client.force_login(user)
    resp = client.post("/api/get-duelos")
    resp_content = json.loads(resp.content)

    assert resp.status_code == 200
    assert resp_content[0]["pk"] == duelo.id
