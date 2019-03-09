#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pnagwekar
#
# Created:     04/11/2015
# Copyright:   (c) pnagwekar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import json
import datetime

from nagini import Nagini


def create_client(host, user_name, password):
    client = Nagini(host=host, user_pass=[user_name, password], useInternalApis=True,
                    verify=False)
    return client

def create_email_template(client):
    emailtemplate = client.create_email_template({"name":"Paragname"},{"template":"Object Name : {{AffectedResourceName}}"})
    return emailtemplate

if __name__ == '__main__':
    client = create_client('eso-monitor.eng.vmware.com', 'admin', 'Ca$hc0w1')
    create_email_template=create_email_template(client, data)
    name = {'name':'ParagTemp'}
    template = {'template': '$$Subject=[vRealize Operations Manager] {{AlertStatus}} Type:{{AlertType}}, Sub-Type:{{AlertSubType}}, State:{{AlertCriticality}}, Object Type:{{AffectedResourceKind}}, Name:{{AffectedResourceName}} New alert was generated at: {{AlertGenerateTime}} Info: {{AffectedResourceName}} {{AffectedResourceKind}}&lt;br&gt; Alert Definition Name: {{AlertDefinitionName}} Alert Definition Description: {{AlertDefinitionDesc}} Object Name : {{AffectedResourceName}} Object Type : {{AffectedResourceKind}} Alert Impact: {{AlertImpact}} Alert State : {{AlertCriticality}} Alert Type : {{AlertType}} Alert Sub-Type : {{AlertSubType}} Object Health State: {{ResourceHealthState}} Object Risk State: {{ResourceRiskState}} Object Efficiency State: {{ResourceEfficiencyState}} Symptoms:&lt;br&gt;{{Anomalies}} Recommendations: {{AlertRecommendation}} Notification Rule Name: {{FilterRuleName}} Notification Rule Description: {{FilterRuleDesc}} Alert ID : {{AlertId}} VCOps Server - {{vcopsServerName}} &lt;a href=;{{AlertSumm