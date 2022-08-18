# Project: Review Collector - Author: Enda Monks - Date of Completion: 2022-08-05
# --------------------------------------------------------------------------------
# Milestone 1 - Scrape and save href links to every album-specific-page on MetaCritic site.
#             - List of strings is stored locally on a JSON file
#             - Print report to show how many links were collected
# --------------------------------------------------------------------------------

import requests # requires install
import bs4 # requires install
import json # requires install

from consts import *
from utils import *

def main_ms1():
    sess = requests.Session() 
    sess.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    # collect hrefs for all album specific pages on website:
    hrefList = []
    for genre in MC_GENRES: # loop through music genres
        
        # navigate to page 1: List of albums corresponding with current genre
        albumsByGenreUrl = HOME_URL + "/browse/albums/genre/name/" + genre + "?view=condensed"
        result = sess.get(albumsByGenreUrl)
        type(result)
        soup = bs4.BeautifulSoup(result.text, "lxml") # get html result for this page

        # collect each album's corresponding href 
        for a in soup.findAll('a', href=True): 
            href = a.get('href')
            if (href.find("/music/", 0) != -1 and href.find("critic-reviews") == -1 
                                            and href.find("user-reviews") == -1): 
                hrefList.append(a.get('href'))
        # --

        # get element for last page number
        lastPg = soup.select('.last_page > .page_num')
        
        # get the page count for this genre's album directory 
        for a in lastPg:
                pageCount = int(a.getText())    
        print("[" + genre + "] Page Count: " +  str(pageCount)) # debug
        
        for i in range(1, pageCount): # start new loop to access next pages for this genre

            random_sleep(DEEP_SLEEP)
            nextUrl = HOME_URL + "/browse/albums/genre/name/" + genre + "?view=condensed&page=" + str(i)
            result = sess.get(nextUrl)
            type(result)
            soup = bs4.BeautifulSoup(result.text, "lxml") # get html result for this page
            # collect each album's corresponding href
            for a in soup.findAll('a', href=True): 
                href = a.get('href')
                if (href.find("/music/", 0) != -1 and href.find("critic-reviews") == -1 
                                            and href.find("user-reviews") == -1): 
                    hrefList.append(a.get('href'))
            # --
        # -- end iteration for next pages
        random_sleep(DEEP_SLEEP)
    # -- end iteration for this genre

    dictionary = dict.fromkeys(hrefList) # remove duplicates from list
    uniqueHrefs = list(dictionary)

    jsonObj = json.dumps(uniqueHrefs, indent=4) # convert final results to json

    with open("json/albumHrefs.json", "w") as outfile: # saving to json file
        outfile.write(jsonObj)

    # report
    print("Href Total")
    print("==========")
    print(len(uniqueHrefs))

        




