# Project: Review Collector - Author: Enda Monks - Date of Completion: 2022-09-27
# -------------------------------------------------------------------------------
# Milestone 3 - Instantiate connection to elastic search collection via .env file
#             - Load Album data from locally stored JSON files  (loop starts here)
#             - POST each collection of Albums to database
#             - Display success message                         (loop ends here)
# -------------------------------------------------------------------------------
import os
import json
from pprint import pprint
from string import ascii_lowercase
import elasticbud # pip install git+https://github.com/z-tasker/elasticbud.git

def ms3():

    print()
    print("Album Collection to DB")
    print("======================")

    client = elasticbud.client.get_elasticsearch_client()

    # load local json data
    for letter in ascii_lowercase:

        print("Processing letter [" + letter + "] ...")
        
        if not os.path.exists("json/" + letter + "_albums.json"):
            print("File Not Found: Unable to load data for albums starting with [" + letter + ']')
            continue
        
        with open("json/" + letter + "_albums.json", 'r') as file:
            albums = json.load(file)
        
        for i in range(len(albums)): # break up dict to avoid overloading data transfer
            elasticbud.index_to_elasticsearch(client, "metacritic-album", [albums[i]], quiet=True) 
        print("Succesfully loaded [" + str(i+1) + "] albums starting with [" + letter + ']')
        
        elasticAlbums = client.search(index="metacritic-album")
        pprint("Current number of albums in DB is [" + str(elasticAlbums["hits"]["total"]["value"]) + "]")


