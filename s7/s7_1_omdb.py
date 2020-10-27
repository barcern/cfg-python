# Example using OMDB

import requests
import json

#endpoint = "http://www.omdbapi.com/?i=tt3896198&apikey=c3b050a5&s=Harry+Potter"
endpoint = "http://www.omdbapi.com"
query_params = {
    "i" : "tt3896198",
    "apikey" : "c3b050a5",
    "s" : "Harry Potter",
}

#response = requests.get(endpoint)
response = requests.get(endpoint, params=query_params)
print(response.status_code)

results = json.loads(response.content)
#results =  response.json()

films = results['Search']

for film in films:
    print(film['Title'])

