import os
import sys
import re
import urllib2
from bs4 import BeautifulSoup
import unicodedata

soup = BeautifulSoup(sys.stdin.read())
paragraphs = soup.find_all('p')

paragraphs = map(lambda(x): x.get_text(),paragraphs)

body = re.sub("\s+"," "," ".join(paragraphs))

body = unicodedata.normalize('NFKD', body).encode('ascii','ignore')

print body

