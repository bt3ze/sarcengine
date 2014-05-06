import sys
import os
import re
import pymongo
import sys
import json
from pymongo import MongoClient

#fname = sys.argv[1]

#file = open(fname,'r')
file = sys.stdin
lines = file.readlines()

client = MongoClient()

db = client.engine
wordcollection = db.words
relationcollection = db.relations

#lines = sys.stdin.readlines()

extract_list = ["and","the","is","are","were","be","being","been","has","have","had","do","does","did","can","may","might","must","shall","will","would","could","should","of","from","or","if","a","an","to","in","it","for","who","us","that","--","-","at","as","how","when","why","where","they","under","over","above","also","on","by","we","was","what","now","its","it\'s","","out","seem","/","like","this","that","therefore","however","she","he","i","him","her","his","hers","not","ive","with","but","which","that","said","says","say","more","less","about","up","ask","put","still","many","those","these","such","yet","new","old","before","after","so","no","than","then"]

source = ""
dictionary = {}
priority_list = {}
relations = {}

for line in lines:
    
    if line.strip() == "":
        print source,
        print priority_list
        print relations

        try:
            word_id = wordcollection.insert({"source":source,"words":priority_list})
            print word_id
        except Exception,err:
            print "error",err
        for w in relations:
            try:
                relation_id = relationcollection.insert({"word":w,"relations":relations[w]})
                print relation_id
            except Exception,err:
                print "error",err
        
    elif line[0:5] == "http:":
        source = line
    else:
        
        dictionary = {}
    
        line = line.lower()
        sentences = line.split(".")
        words = re.sub("\.|,|\'|:|\?|\"|\(|\)","",line)
        wordlist = words.split(" ")
        wordlist = [ w for w in wordlist if w not in extract_list]
        for w in wordlist:
            if w in dictionary:
                dictionary[w] = dictionary[w] + 1
            else:
                dictionary[w] = 1
                #  print sentences
                
                priority_list = sorted(dictionary,key=dictionary.get,reverse=True)[:40]
                
        relations = {}
                
        for sentence in sentences:
            sentence = re.sub("\.|,|\'|:|\?|\"|\(|\)","",sentence)
            sentence = [w for w in sentence.split(" ") if w not in extract_list]
            #print sentence
            for word in sentence:
                if word in priority_list:
                    #print word
                    for w2 in sentence:
                        if w2 in priority_list and w2 != word:
                            if word in relations:
                                if w2 in relations[word]:
                                    pass
                                else:
                                    relations[word].append(w2)
                            else:
                                relations[word] = []
                                relations[word].append(w2)
                                
        #for i in range(0, len(priority_list)):
            #print priority_list[i], dictionary[priority_list[i]]
            
        #for r in relations:
            #print r, relations[r]
        #print ""


#for d in sorted(dictionary, key=dictionary.get,reverse=True):
#    print d, dictionary[d]
