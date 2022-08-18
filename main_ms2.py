# Project: Review Collector - Author: Enda Monks - Date of Completion: 2022-08-11
# -------------------------------------------------------------------------------
# Milestone 2 - Read list of links from JSON file and place in list
#             - Prompt user to input a letter from the alphabet
#             - Iterate through all album pages which begin with this letter
#             - Scrape fields for Album and Review class properties
#             - Write collection of Review objects to new local JSON file
# -------------------------------------------------------------------------------
import requests # requires install
import bs4 # requires install
import json # requires install
from marshmallow import pprint
from consts import *
from utils import *
from reviews.Review import Review
from music.Album import Album, AlbumSchema

def main_ms2():
    
    sess = requests.Session() 
    sess.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    # Get list of links from file
    f = open('json/albumHrefs.json')
    albumHrefs = json.load(f)
    f.close() 

    print()
    print("Album Review Scraper")
    print("====================")

    exit = False
    while(not exit):

        # Aquire user's selection
        validInput = False
        exit = False
        while (not validInput):
            letter = input("Enter a letter or quit [0]: ")
            if(letter.isalpha()):
                letter = letter.lower()
                validInput = True
            elif(int(letter) == 0):
                exit = True
                validInput = True
            else:
                print("Error: You must input one letter from the alphabet or zero\n")
        if(exit == True):
            continue

        albums:Album = []
        # Get links for albums which start with letter input 
        currentHrefs = []
        for i in albumHrefs:
            if i.find("/music/" + letter, 0) != -1: 
                currentHrefs.append(i)

        if(len(currentHrefs) == 0):
            print("There are no albums starting with [" + letter + "] ...\n")
        else:
            print("Collecting data for [" + str(len(currentHrefs)) + "] albums starting with [" + letter + "] ...\n")

            for albumHref in currentHrefs: 
                # navigate to album specific page
                albumUrl = HOME_URL + albumHref
                result = sess.get(albumUrl)
                type(result)
                soup = bs4.BeautifulSoup(result.text, "lxml") # get html result for this page
                
                albumUrl = HOME_URL + albumHref
                result = sess.get(albumUrl)
                type(result)
                soup = bs4.BeautifulSoup(result.text, "lxml") # get html result for this page

                # get album title
                elements = soup.select('div > a > span > h1')
                title = list(elements)[0].getText()

                # get album artist name
                elements = soup.select('.band_name')
                artist = list(elements)[0].getText()

                # get date of album release
                elements = soup.select('li.release span[itemprop]')
                releaseDate = list(elements)[0].getText()

                # get genres
                genres = []
                elements = soup.select('li.product_genre span.data')
                for a in elements:
                    genres.append(a.getText())

                album = Album(title, artist, stringToDate(releaseDate, DATE_FORMAT), genres)

                # get critic review count
                elements = soup.select('span.distribution')
                critRevCount = list(elements)[0].getText().replace("out of ", "") # out of {totalCount}
                if len(critRevCount) == 0 or critRevCount == ' ':
                    critRevCount = 0
                else:
                    critRevCount = int(critRevCount)
                    if critRevCount > REV_PER_PG: # unlikely, but to be sure
                        critRevCount = REV_PER_PG

                # get user review count
                if len(list(elements)) < 4:
                    usrRevCount = 0
                else:    
                    usrRevCount = list(elements)[4].getText().replace("out of ", "")
                    if usrRevCount == ' ':
                        usrRevCount = 0
                    usrRevCount = int(usrRevCount)
                    if usrRevCount > U_REV_MAX:
                        usrRevCount = U_REV_MAX # to meet project requirements

                if critRevCount > 0: # ensure reviews exist

                    random_sleep(LIGHT_SLEEP)

                    # request Critic Review html for pg 1
                    criticUrl = HOME_URL + albumHref + "/critic-reviews"
                    result = sess.get(criticUrl)
                    type(result)
                    soup = bs4.BeautifulSoup(result.text, "lxml") 

                    # extract CriticReview data    

                    #score
                    criticScores = []
                    elements = soup.select('div.review_grade div.metascore_w')
                    for a in elements:
                        criticScores.append(a.getText().strip())

                    #publication
                    publications = []
                    elements = soup.select('div.review_critic div.source') # text with hyper link
                    for a in elements:
                        publications.append(a.getText().strip())

                    elements = soup.select('div.review_critic a.external') # text without hyper link
                    for a in elements:
                        publications.append(a.getText().strip())
                    

                    #content
                    criticContents = []
                    elements = soup.select('div.review_body')
                    for a in elements:
                        criticContents.append(a.getText().strip())
                    
                    #date
                    criticDates = []
                    elements = soup.select('div.review_critic div.date')
                    if len(elements) >= critRevCount: # ensure dates are included on this page
                        for a in elements:
                                criticDates.append(a.getText().strip())
                    else:
                        for i in range(critRevCount):
                                criticDates.append(None)

                    # initialize collection of CriticReview objects
                    criticReviews:Review = []

                    for i in range(critRevCount):
                        if not criticDates[i]:
                            revTemp = Review("Critic", criticScores[i], C_SCORE_MAX, publications[i], criticContents[i], None)
                        else:
                            revTemp = Review("Critic", criticScores[i], C_SCORE_MAX, publications[i], criticContents[i], stringToDate(criticDates[i], DATE_FORMAT))
                        criticReviews.append(revTemp)
                    album.addReviews(criticReviews)
                
                if usrRevCount > 0: # ensure user reviews exist

                    currentPg = 1

                    # get total page count
                    if usrRevCount > REV_PER_PG:
                        pgCount = int(U_REV_MAX / REV_PER_PG)
                        currentRevCount = REV_PER_PG
                    else:
                        pgCount = 1
                        currentRevCount = usrRevCount # get review count for current page

                    while currentPg <= pgCount:

                        random_sleep(LIGHT_SLEEP)
                        # Go to user review page and collect data
                        if currentPg == 1:
                            userUrl = HOME_URL + albumHref + "/user-reviews"
                        elif currentPg > 1:
                            userUrl = HOME_URL + albumHref + "/user-reviews" + "?page=" + str(currentPg - 1)
                            currentRevCount = usrRevCount - (REV_PER_PG * (pgCount -1))

                        result = sess.get(userUrl)
                        type(result)
                        soup = bs4.BeautifulSoup(result.text, "lxml") # get html result for this page
            
                        # extract UserReview data
                        
                        #score
                        userScores = []
                        elements = soup.select('div.review_grade div.metascore_w')
                        for a in elements:
                            userScores.append(a.getText().strip())

                        #content
                        userContents = []
                        elements = soup.select('div.review_body')
                        for a in elements:
                            userContents.append(a.getText().strip())

                        #date
                        userDates = []
                        elements = soup.select('div.review_critic div.date')
                        for a in elements:
                            userDates.append(a.getText().strip())

                        # initialize collection of UserReview objects
                        userReviews:Review = []

                        for i in range(currentRevCount):
                            revTemp = Review("User", userScores[i], U_SCORE_MAX, SERVICE_NAME, userContents[i], stringToDate(userDates[i], DATE_FORMAT))
                            userReviews.append(revTemp)
                    
                        album.addReviews(userReviews)

                        currentPg += 1
                    # end of user rev page loop
                # end of user rev block

                # debug :
                album.toString()
                print("---------")
                # -----------------

                albums.append(album)
                random_sleep(LIGHT_SLEEP)

            # end iteration for album
            print("Total Albums collected for " + letter + ": ", len(albums))

            # get schema result
            result = []
            for alb in albums:
                result.append(AlbumSchema().dump(alb))
            
            jsonResult = json.dumps(list(result), indent=4) # convert final results to json

            with open("json/" + letter + "_albums.json", "w") as outfile: # saving to json file
                outfile.write(jsonResult)

# --------        
main_ms2()
print("Good bye")


