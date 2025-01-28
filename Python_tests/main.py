import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aaefabca85a6fd375522a2232b1cb61e'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : f'{TOKEN}'}
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
body_rename_pokemon = {
    "pokemon_id": "203482",
    "name": "Lizazavr",
    "photo_id": -1
}

body_catch_in_pokeball = {
    "pokemon_id": "203482"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create_pokemon) # Запрос на создание покемона
print(response_create.text)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_rename_pokemon) # Запрос на изменение покемона
print(response_rename.text)

response_catch_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_catch_in_pokeball) # Запрос на ловлю покемона в покебол
print(response_catch_in_pokeball.text)

message = response_catch_in_pokeball.json()['message'] # Попробовал отдельно вывести сообщение ответа в терминал
print(message) 