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

words = list(articlecollection.find({}))

#print words

for wlist in words:
#    print wlist
    print wlist['words']
    for w in wlist['words']:
        relations = list(relationcollection.find({"word":w}))
        print relations

client.close()
