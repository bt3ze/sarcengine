import sys
import os
import re
import pymongo
import sys
import json
from pymongo import MongoClient


client = MongoClient()


db = client.engine
wordcollection = db.words
relationcollection = db.relations
lst = ["china","money","yen"]

words = list(relationcollection.find({"word":lst}))

print words

matches = []
for w in words:
    intersects = list(wordcollection.find({"words": {"$in": words}}))
    print intersects


'''
for wlist in words:
#    print wlist
    print wlist['words']
    for w in wlist['words']:
        relations = list(relationcollection.find({"word":w}))
        for r in relations:
            print r
'''
client.close()
