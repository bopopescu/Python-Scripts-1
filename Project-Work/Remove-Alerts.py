#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pnagwekar
#
# Created:     29/10/2015
# Copyright:   (c) pnagwekar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------vcops = nagini.Nagini(host="vcopsqe-monitor-2.eng.vmware.com", user_pass=("admin", "Vmware60!") )

import json
import datetime

from nagini import Nagini


def create_client(host, user_name, password):
    client = Nagini(host=host, user_pass=[user_name, password], useInternalApis=True,
                    verify=False)
    return client


def get_alerts(client, stat, pageSize):
    alert_list = client.get_alerts(page=0, status=stat, pageSize=pageSize)
    if alert_list:
        return alert_list
    else:
        print 'Alert list is none'
        return None


def cancel_alert(client, data, page=0, pageSize=100):
    response = client.modify_alerts(data, page=page, action='cancel', pageSize=pageSize)
    return response


def query_active_alerts(client, data, page=0):
    alert_list = client.query_alert(data, page=page)
    return alert_list


if __name__ == '__main__':
    client = create_client('eso-monitor.eng.vmware.com', 'admin', 'Ca$hc0w1')
    alert_list = get_alerts(client, stat='ACTIVE', pageSize= 10)  # tune this pageSize number to query more alerts
    begin_time = datetime.datetime.now()
    print 'begin time ' + str(begin_time)
    alerts = alert_list['alerts']
    print alerts
    print 'alert size = ' + str(len(alerts))
    uuid = {'uuids': []}
    for alert in alerts:
        uuid['uuids'].append(alert['alertId'])
    data = json.dumps(uuid)
    print data
    response = cancel_alert(client, data, pageSize=200)
    end_time = datetime.datetime.now()
    print 'End time ' + str(end_time)
    print 'duration is ' + str(end_time - begin_time)