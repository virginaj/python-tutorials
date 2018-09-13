import boto3

def list_volumes():
    ec2_resource = boto3.resource('ec2')

    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.state)
        for item in instance.volumes.all():
            print item.id
            snapshot = ec2_resource.create_snapshot(VolumeId=item.id, Description="Taking backup")

list_volumes()
