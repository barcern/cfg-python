# I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
# Pokemon. Save their names and moves into a file called 'pokemon.txt'

import requests
import random
import json

url = "https://pokeapi.co/api/v2/pokemon/"
filename = "s6_h1.txt"

for i in range(6):
    random_id = str(random.randint(1, 893))
    poke_url = url + random_id
    r = requests.get(poke_url)
    data = json.loads(r.content)
    name = data['name']
    store = random_id + " " + name + "\n"
    with open(filename, "a") as f:
        f.write(store)
