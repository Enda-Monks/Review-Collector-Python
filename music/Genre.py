GENRE_TUPLE = ( "Alt-Country" #0
                "Alternative" #1
                "Blues" #2
                "Comedy", #3
                "Country", #4
                "Dance", #5
                "Electronic",#6
                "Experimental", #7
                "Folk", #8
                "House", #9
                "Indie",
                "Jazz",
                "Latin",
                "Metal",
                "Pop",
                "Psychedelic",
                "Punk",
                "Rap",
                "R&B"
                "Singer-Songwriter"
                "Soul",
                "Soundtrack",
                "Techno",
                "Vocal",
                "World")

def Genre(object):
    def __init__(self, genreName):
        if genreName in GENRE_TUPLE: # ensure valid
            self.name = genreName # genre name
            urlFormat = self.name.toLowerCase()
            self.urlFormat = urlFormat.replace('&', '') # url format genre name