import sys
import urllib2

from xml.dom.minidom import parse, parseString

url = sys.argv[1]

response = urllib2.urlopen(url)

dom = parseString(response.read())

for item in dom.getElementsByTagName("item"):
    for i in item.getElementsByTagName("link"):
        print i.firstChild.nodeValue
