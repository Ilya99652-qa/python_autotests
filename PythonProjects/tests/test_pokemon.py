import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd1d7e2cd65ce593763197ef3713a2baa'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '38345'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers/{38345}', headers = HEADER)
    assert response.status_code == 200

def test_part_of_response():
    response_get  = requests.get(url = f'{URL}/trainers/{38345}', headers = HEADER)
    assert response_get.json()['trainer_name'] == 'Ashiko'

@pytest.mark.parametrize('key, value', [('trainer_name','Ashiko' ), ('id', TRAINER_ID), ('city', 'Piter')])
def test_parametrize(key, value) :
    response_parametrize = requests.get(url = f'{URL}/trainers/{38345}', headers = HEADER)
    assert response_parametrize.json() [key] == value