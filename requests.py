#!/usr/bin/python -u

import urllib2
import sys
import os
from contextlib import closing
import time

'''
class flushfile(object):
    def __init__(self, f):
        self.f = f
    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = flushfile(sys.stdout)
'''
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1) # no buffering


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

try:
    for d in data:
        sys.stdout.write( d )
        sys.stdout.flush()
except IOError as e:
    print e
finally:
    pass

'''
encoding = locale.getpreferredencoding()
Writer = getwriter(encoding)
sys.stdout = Writer(sys.stdout)
'''

sys.stdout.write("")


'''
response = urllib2.urlopen(url)
print response.read()
response.close()

'''
