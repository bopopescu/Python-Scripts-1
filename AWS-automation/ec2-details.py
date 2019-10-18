import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
for t in response['Reservations']:
    for i in (t['Instances']):
        print (i['InstanceId'], i['PublicIpAddress'])

response=ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],
    DryRun=False,
    MaxResults=123
)