import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd1d7e2cd65ce593763197ef3713a2baa'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_registr_pocemon = {
    "name": "Kliplik",
    "photo_id": 35
}
body_modify = {
    "pokemon_id": "367712",
    "name": "kurlik",
    "photo_id": 290
}

body_in_poceboll = {
    "pokemon_id": "367712"
}


'''response = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_registr_pocemon) 

print(response.text)'''

'''response_Modify = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_modify)

print(response_Modify.text)'''

response_in_poceboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_poceboll)

print(response_in_poceboll.text)