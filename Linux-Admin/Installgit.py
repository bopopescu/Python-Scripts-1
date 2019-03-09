import os
import sys
import platform
import time
import re
import urllib
from subprocess import *

def welcome():
    print("******************************************************")
    print("This Script will find the existing version of GIT")
    print("******************************************************")
    time.sleep(4)

def Thank_you():
    print( "\n\n Thank you for using this script\n Have a great day")
    return None

def run_cmd_status(cmd):
    sp=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
    rt=sp.wait()
    out,err=sp.communicate()
    return(out)

def is_root():
    if os.getuid() == 0:
        return True
    else:
        return False


os.system('clear')
print("Please wait checking the pre-requisite.....")
time.sleep(2)

try:
    if is_root() == True:
            print("You are the root user. You can run this scriptr")
    else:
        print("Please run this script as a root user")
        Thank_you()
        sys.exit(1)
except Exception as e:
    print (e)
    print ("Plese rectify the error as try it")
    sys.exit(2)

try:
    wget_status=run_cmd_status("wget --version")
    if wget_status =='':
        print("Please wait installing wget command")
        run_cmd_status("yum install wget -y")
    else:
        print("Satisfied with wget command")
except Exception as e:
    print(e)
    print ("Rectify the error and try it")
    Thank_you()
    sys.exit(3)

try:
    pip_status=run_cmd_status("pip --version")
    if pip_status =='':
        print("Please wait installing pip command")
        run_cmd_status("easy_install pip")
    else:
        print("Satisfied with wget command")
except Exception as e:
    print(e)
    print ("Rectify the error and try it")
    Thank_you()
    sys.exit(4)

try:
    from bs4 import BeautifulSoup
    pip_status=run_cmd_status("pip --version")
    if pip_status =='':
        print("Please wait installing pip command")
        run_cmd_status("easy_install pip")
    else:
        print("Satisfied with wget command")
except Exception as e:
    print(e)
    print ("Rectify the error and try it")
    Thank_you()
    sys.exit(4)
