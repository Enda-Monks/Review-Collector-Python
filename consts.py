# Utils
# =====
DEEP_SLEEP = 2.5 # scrape tools
LIGHT_SLEEP = 0.5 

# MetaCritic
# ==========
SERVICE_NAME = "MetaCritic"
HOME_URL = "https://www.metacritic.com"
DATE_FORMAT = "%b %d, %Y" # all dates on website
C_SCORE_MAX = 100 # critic scores are int/100
U_SCORE_MAX = 10 # user scores are int/10
REV_PER_PG = 100 # limit to reviews per page
U_REV_MAX = 200 # Project requires <= 200 user reviews per album
MC_GENRES = (   "alt-country", # website's genre selection for albums directory
                "alternative", 
                "blues", 
                "comedy", 
                "country", 
                "dance", 
                "electronic",
                "experimental", 
                "folk", 
                "house", 
                "indie",
                "jazz",
                "latin",
                "metal",
                "pop",
                "psychedelic",
                "punk",
                "rap",
                "rb",
                "reggae",
                "rock",
                "singer-songwriter",
                "soul",
                "soundtrack",
                "techno",
                "vocal",
                "world")
