class Album(object):
    def __int__(self, title, genre, releaseDate, mcScore):    
        self.title = title # album title
        self.genres.add(genre) # set of multiple genres
        self.releaseDate = releaseDate # album release date
        self.mcScore = mcScore # MetaCritic score

    def addGenre(self, genre):
        self.genres.add(genre)
