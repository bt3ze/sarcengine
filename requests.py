#/usr/bin/python

import urllib2
import sys
from contextlib import closing
import time

url = sys.argv[1]

try:
    handler = urllib2.build_opener(urllib2.HTTPCookieProcessor)
    urllib2.install_opener(handler)
    response = urllib2.urlopen(url)
    data = response.read()
except urllib2.URLError, err:
    print(err.reason)
finally:
    try:
        response.close()
    except NameError:
        pass

#print res
#print data

#dat = data
#print dat

#time.sleep(.05)

#data = data
#print data

try:
    print data
except IOError as e:
    print e
finally:
    pass


#pass
#print ""

#res = response.read()
#except urllib2.URLError, err:
#    print(err.reason)
#finally:
#    try:
#        response.close()
#    except NameError:
#        pass

#print res



'''
response = urllib2.urlopen(url)
print response.read()
response.close()

'''
