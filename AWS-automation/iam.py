import boto3
iam = boto3.client('iam')

'''
# Create user
response = iam.create_user(UserName='Valaxy-Demo-User')
print(response)

'''
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)
