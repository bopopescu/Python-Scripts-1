__author__ = 'pnagwekar'
from fabric.api import *
env.hosts = ['172.16.78.155']
env.user = "pnagwekar"
env.password = "Pagroo557"

def hello(who="world"):
    print "Hello {who}!".format(who=who)

def listing():

    with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True
    ):
        print ("Running the command")
        print (run('ls -l'))