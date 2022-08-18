from datetime import datetime
from sqlite3 import Date ## ?? neccesary??
from marshmallow import Schema, fields

class ReviewSchema(Schema):
    authorType = fields.Str()
    score = fields.Float()
    scoreMax = fields.Float()
    publication = fields.Str()
    content = fields.Str()
    date = fields.DateTime()

class Review(object):
    def __init__(self:str, authorType:str, score:float, scoreMax:float, publication:str, content:str, date:datetime):
        self.authorType = authorType
        self.score = score
        self.scoreMax = scoreMax
        self.publication = publication
        self.content = content
        if date == None: # some reviews do not include dates
            self.date = None
        else:
            self.date = date.date()
    
    def toString(self):
        print("Author Type: " + self.authorType)
        print("Score:", self.score, "/", self.scoreMax)
        print("Publication: " + self.publication) 
        print("Content: " + self.content)
        print("Date: " + str(self.date))


    
