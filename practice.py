import requests

api_key = 'ffb3895b-821b-4843-88fd-9dba3ae23265'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
word = 'potato'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions)