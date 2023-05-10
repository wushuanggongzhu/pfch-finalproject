import requests
import json

# This is my request for object IDs
base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?[params]'
payload = {
    'artistOrCulture': 'true',
    'q': 'china'
}

r = requests.get(base_url, params=payload)

# Make the response into Json
data = r.json()

# This gives you a list of objectIDs
object_ids = data['objectIDs']

# Finally, write these objectIDs into a json file
with open('object_ids.json', 'w') as f:
    json.dump(object_ids, f)