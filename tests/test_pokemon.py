import requests
import pytest
URL = 'https://api.pokemonbattle.me'
TRAINER_ID = '3440'
TRAINER_NAME = 'Иннокентий'
TOKEN = 'USER_TOKEN'
HEADERS = {'Content-Type' : 'application/json',
           'trainer_token' : TOKEN  }

def test_status_code ():
    response = requests.get(url= f'{URL}/v2/trainers', params = {"trainer_id" : TRAINER_ID})  # проверка статус кода
    assert response.status_code == 200, 'Unexpected status code'



def test_get_trainers_by_id_check_name():
    response = requests.get(url= f'{URL}/v2/trainers', params = {"trainer_id" : TRAINER_ID}, timeout=5) # проверка имени и города тренера
    
    assert response.json()['data'][0]['trainer_name'] == TRAINER_NAME