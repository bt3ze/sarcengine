import os
from flask import Flask, url_for, render_template, request,session
import jinja2
import re
import pymongo
import urllib2
from pymongo import MongoClient
from bs4 import BeautifulSoup
import unicodedata
from flask import request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def engine():
    return render_template('base.html',user='me')

@app.route('/hello')
def hello():
    return "hello"

@app.route('/queryurl/<path:url>')
def queryurl(url):
    # return url

    # go grab the external page, save it in "data"
    try:
        handler = urllib2.build_opener(urllib2.HTTPCookieProcessor)
        urllib2.install_opener(handler)
        response = urllib2.urlopen(url)
        data = response.read()
    except urllib2.URLError, err:
        print(err.reason)
#        data = ""
    finally:
        try:
            response.close()
        except NameError:
            pass
    
    #extract the good information from the page

    
    soup = BeautifulSoup(data)
    paragraphs = soup.find_all('p')

    paragraphs = map(lambda(x): x.get_text(),paragraphs)

    body = re.sub("\s+"," "," ".join(paragraphs))
    body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')


    ## now, process the content as if preparing to insert it into our db
    ## first, set up db connections

    
    client = MongoClient()

    db = client.engine
    wordcollection = db.words
    relationcollection = db.relations

    extract_list = ["and","the","is","are","were","be","being","been","has","have","had","do","does","did","can","may","might","must","shall","will","would","could","should","of","from","or","if","a","an","to","in","it","for","who","us","that","--","-","at","as","how","when","why","where","they","under","over","above","also","on","by","we","was","what","now","its","it\'s","","out","seem","/","like","this","that","therefore","however","she","he","i","him","her","his","hers","not","ive","with","but","which","that","said","says","say","more","less","about","up","ask","put","still","many","those","these","such","yet","new","old","before","after","so","no","than","then"]

    dictionary = {}
    priority_list = {}
    relations = {}
    
    # next, process the input    
    line = body.lower()
    
    sentences = line.split(".")
    
    words = re.sub("\.|,|\'|:|\?|\"|\(|\)","",line)
    wordlist = words.split(" ")
    
    wordlist = [ w for w in wordlist if w not in extract_list]
    
    
    for w in wordlist:
        if w in dictionary:
            dictionary[w] = dictionary[w] + 1
        else:
            dictionary[w] = 1

    
    priority_list = sorted(dictionary,key=dictionary.get,reverse=True)[:40]
        
    for sentence in sentences:
        sentence = re.sub("\.|,|\'|:|\?|\"|\(|\)","",sentence)
        sentence = [w for w in sentence.split(" ") if w not in extract_list]
        for word in sentence:
            if word in priority_list:
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

                        
    # now I have all the information I need, can go ahead and query the db


    words = list(relationcollection.find({"word": {"$in": list(dictionary)}}))
    # might come back to this later if I want to grab all the words from the relations and not just the important ones in the article. the difference is one degree of separation

    client.close()
    return json.dumps(words)
    '''
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
        
    client.close()
    return json.dumps(relations)
    '''
