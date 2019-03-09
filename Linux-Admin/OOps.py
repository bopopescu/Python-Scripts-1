#! /usr/bin/env python
from bashing import diskspace_func


class Server(object):
    def __init__(self, ip, hostname):
        self.ip=ip
        self.hostname=hostname

    def set_hostname(self, hostname):
        self.hostname=hostname

    def set_ip(self,ip):
        self.ip=ip

    def ping(self,ipaddress):
        print("Pinging %s from %s of (%s)" %(ipaddress, self.ip, self.hostname))

if __name__ == '__main__':
    server=Server('192.168.1.12', 'Win')
    server.ping('192.168.1.15')

    diskspace_func()























#! /usr/bin/env python
class Server(object):
    def __init__(self, ipaddress, hostname):
        self.ip = ipaddress
        self.hostname = hostname

    def setip (self, ipaddress):
        self.ip=ipaddress

    def sethostname(self, hostname):
        self.hostname=hostname

    def ping (self, ip_addr):
        print ("Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname))

if __name__==  '__main__':
    server=Server("192.168.1.1", "tumbly")
    server.ping ("192.168.1.2")