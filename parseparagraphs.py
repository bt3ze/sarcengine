import os
import sys
import re
import urllib2

def contentfromtags(line):
    return line[line.find(">")+1:]

paragraphs = re.findall('<p>.*</p>', sys.stdin.read())

body = " ".join(paragraphs)

cuts = re.split("<",body)

text = " ".join(map(contentfromtags,cuts))


#print paragraphs
print text
