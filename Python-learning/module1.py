#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     09/05/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import getopt, sys, os, errno
import getpass
import requests
import json
from requests.auth import HTTPBasicAuth


def exer3():
    """
    learn requests module
    task:
        get data from the server and print out response data like status_code, text, headers
    """
    server = "http://httpbin.org/get"

#r = requests.get('https://github.com', verify=True)
# <Response [200]>
# r = requests.get('https://github.com', auth=HTTPBasicAuth(user,passwd))
#

def main():
    number = "3"
    try:
        cmdlineOptions, args= getopt.getopt(sys.argv[1:],'he:',["help","exer="])
    except getopt.GetoptError, e:
        raise "Error in a command-line option:\n\t" + str(e)


    for (optName,optValue) in cmdlineOptions:
        if  optName in ("-h","--help"):
            print __doc__
            sys.exit()
        elif optName in ("-e","--exer"):
            number = optValue
        else:
            errorHandler('Option %s not recognized' % optName)

    # mostly you don't need to understand below, focus on exercise
    # Get it from globals and invoke `exerx()` method directly
    method_name = "exer" + number
    method_list = globals()
    if method_name in method_list:
        method_list[method_name]()
    else:
        print "the exericse %s is not ready, please create method `exer%s` directly" % (number, number )

if __name__ == '__main__':
    main()