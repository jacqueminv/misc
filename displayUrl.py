from __future__ import with_statement
import sys

'''
author: Valentin Jacquemin <www.poxd.org>
year: 2009
version: 0.1

Summary: Some utility functions
'''

if __name__ == "__main__":
    file = sys.argv[1]
    url = ""
    try:
        with open(file) as f:
            for line in f:
                url += line
    except:
        print 'Error: the 1st argument must a filename'
    vars = url.split('&')
    sys.stdout.write('\n'.join(["%s" % (var) for var in vars]))
    