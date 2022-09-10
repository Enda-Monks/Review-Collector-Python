from datetime import datetime
from review.Review import Review, ReviewSchema
from marshmallow import Schema, fields

class AlbumSchema(Schema):
    title = fields.Str()
    artist = fields.Str()
    releaseDate = fields.DateTime()
    genres = fields.List(fields.Str())
    reviews = fields.List(fields.Nested(ReviewSchema))

class Album(object):
    def __init__(self:str, title:str, artist:str, releaseDate:datetime, genres:list):  
        self.title = title # album title
        self.artist = artist
        self.releaseDate = releaseDate.date()
        self.genres = genres # list
        self.reviews:Review = []

    def addReviews(self, reviews = []):
        self.reviews.extend(reviews)

    def getType(self) -> str:
        return self.type

    def getReviewCount(self) -> int:
        return len(self.reviews)
    
    def getReviewCountByType(self, type:str) -> int:
        result = 0
        for review in self.reviews:
            if review.authorType == type:
                result += 1
        return result

    def printSelf(self):
        print("Title: " + self.title)
        print("Artist: "+ self.artist)
        print("Release Date: " + str(self.releaseDate))
        for i in range(len(self.genres)):
            print("Genre[" + str(i+1) + "]: " + self.genres[i])
        print("Review Count: " + str(len(self.reviews)))