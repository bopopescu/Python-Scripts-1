import boto3

ec2 = boto3.resource('ec2')

for ec2name in ec2.all():
    print(ec2name.name)

instance=ec2.create_instances(
    ImageId='ami-25615740',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

print(instance[0].id)