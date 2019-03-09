#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pnagwekar
#
# Created:     03/11/2015
# Copyright:   (c) pnagwekar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
import sys

search_text = 'alertId'
files = ['alerts.txt']
for arg in files :
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
        break
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

filename = files[0]
print ('alertIDs are dumped in alertsID file')
f = open(filename, 'r')
f2 = open ('alertsid.txt', 'w')
for line in f:
    if re.search(search_text, line):
       f2.write(line)
f2.close()
f.close()