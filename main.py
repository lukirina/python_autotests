"""
test api
"""
import requests
URL = 'https://api.pokemonbattle.me'
TOKEN = '6e691c5fa100ca68bb852da6604629af'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
          
body = {
    "name": "generate",
    "photo": "generate"
}
response=requests.post(url=f'{URL}/v2/pokemons', json=body, headers=HEADERS) #создание покемона
print(response.text)

POKEMON_ID=response.json()['id'] #сохраняем айдишник созданного покемона

new_body = {
    "pokemon_id": POKEMON_ID,
    "name": "Юккич",
    "photo": "https://dolnikov.ru/pokemons/albums/079.png"
}
 
response=requests.put(url=f'{URL}/v2/pokemons', json=new_body, headers=HEADERS) #смена имени покемона
print(response.text)

body_pokeball = {
    "pokemon_id": POKEMON_ID
}
response=requests.post(url=f'{URL}/v2/trainers/add_pokeball', json=body_pokeball, headers=HEADERS) #поймать покемона в покеболл
print(response.text)