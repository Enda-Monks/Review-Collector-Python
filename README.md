

# Review-Collector-Python
Assembles Collection of Critic &amp; User Reviews from the Web

## Milestone 1 
- Scrapes and saves href links to every album-specific-page on MetaCritic site

- List of strings is stored locally on a JSON file

- Prints report to show how many links were collected

## Milestone 2 
- Reads MetaCritic urls from JSON file obtained in ms1 and places in list

- Prompts user to input a letter from the alphabet or quit (Loop starts here)

- Iterates through all album pages which begin with this letter

- Scrapes fields for corresponding Album and Review class properties

- Writes collection of Album objects to new local JSON file (End of loop)

## Milestone 3 
- Instantiates connection to elastic search index via .env file

- Loads Album data from locally stored JSON files  (loop starts here)

- POST each collection of Albums to database

- Displays success message                         (loop ends here)


## Requirements: 
- see poetry.lock for reqs

- import elasticbud seperately

    ```pip install git+https://github.com/z-tasker/elasticbud.git```





