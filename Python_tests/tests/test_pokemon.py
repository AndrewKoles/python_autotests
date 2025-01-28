import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aaefabca85a6fd375522a2232b1cb61e'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : f'{TOKEN}'}
Trainer_id = 18848

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'Андрюха'
    