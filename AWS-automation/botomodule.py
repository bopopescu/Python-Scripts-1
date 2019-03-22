import boto3
import json

'''
# This creates EC2 instances
ec2 = boto3.resource('ec2')

instance=ec2.create_instances(
    ImageId='ami-0a313d6098716f372',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

print(instance[0].id)
'''

import boto3
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        # print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        # print(instance["InstanceId"],"\t", instance["LaunchTime"])
        ec2 = boto3.resource('ec2')
        if instance["ImageId"] == "ami-0a313d6098716f372":
            print(instance["InstanceId"])
            '''
            specificinstnace = ec2.Instance(instance["InstanceId"])
            response = specificinstnace.terminate()
            print(response)
            i-0f627d4919df1d1ea 	 2019-03-21 18:46:47+00:00
            i-09e3550a0c0112f56
            '''