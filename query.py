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

words = list(relationcollection.find({"word":"yen"}))

item = words[0]
#print item

rels = item[u'relations']
#print rels

intersects = list(wordcollection.find({"words": {"$in":rels}}))
#print intersects
intersects = map(lambda(x): {"source":x['source'],'words':x['words'],"intersections":len(set(rels)&set(x['words']))},intersects)

#print intersects

bestmatches = sorted(intersects, key=lambda x: x['intersections'], reverse=True)

for i in range(0,10):
    print bestmatches[i]

'''
for w in words['relations']:
    intersects = list(wordcollection.find({"words": {"$in": words}}))
    print intersects
'''

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
