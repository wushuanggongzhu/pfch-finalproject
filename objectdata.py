import requests
import json
import csv

# Open up the previously created JSON file with objectIDs
with open('object_ids.json', 'r') as f:
    object_ids = json.load(f)

# We are going to write the objectID info/catalog into a CSV file    
with open('object_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Object ID', 'Title', 'Object Date', 'Accession Date', 'Earliest Date', 'Latest Date', 'Period', 'Dynasty', 'Medium', 'Classification', 'Artist Suffix']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each object ID and send it to the API. This API is different, since we're looking for object information
    for object_id in object_ids:
        url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}'
        response = requests.get(url)

        # This tells us if it's working
        if response.status_code == 200:
            # Parse the response as JSON
            data = response.json()

            # These are the fields that I want, you can update them depending on the info you wish to retrieve
            title = data['title']
            objectdate = data['objectDate']
            accessiondate = data['accessionYear']
            earlydate = data['objectBeginDate']
            enddate = data['objectEndDate']
            period = data['period']
            dynasty = data['dynasty']
            medium = data['medium']
            classification = data['classification']
            artistsuffix = data.get('artistSuffix', '')

            # Write this info into your CSV file
            writer.writerow({
                'Object ID': object_id,
                'Title': title,
                'Object Date' : objectdate,
                'Accession Date' : accessiondate,
                'Earliest Date' : earlydate,
                'Latest Date' : enddate,
                'Period' : period,
                'Dynasty': dynasty,
                'Medium': medium,
                'Classification': classification,
                'Artist Suffix': artistsuffix
            })

        else:
            print(f'Sorry, failed request for object ID {object_id}')