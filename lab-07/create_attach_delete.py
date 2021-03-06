import boto3
import sys
from botocore.exceptions import ClientError


# to create instances - maxcount =3
def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['sg-05198f9df4a5885af'],KeyName='fullstack')
    
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)
    print ("Instance is Running now!")
    return instance_ids
# end of function to create instances - maxcount =3

# to create snapshot
def create_snapshot(list):
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.state)
        for item in instance.volumes.all():
            snapshot = ec2_resource.create_snapshot(VolumeId=item, Description="Taking backup")
            print item.id
# end of function to create snapshot



# to delete instances
def prepare_instance_list():
    mylist = []
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id, instance.instance_type)
        mylist.append(instance.id)
    return mylist

def delete_instances(instance_list):
    ec2_client = boto3.client('ec2')
    try:
        ec2_client.terminate_instances(InstanceIds=instance_list,DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    ec2_client.terminate_instances(InstanceIds=instance_list,DryRun=False)
#end of function to delete instance

#-------------------------------
if __name__ == "__main__":
#call to create instance
    list = create_instance()
  
#call to create snapshot
    create_snapshot(list)

#call to terminate instance
    instance_list = prepare_instance_list()
    if len(instance_list) !=0:
        print ( "Deleting Instances", instance_list)
        delete_instances(instance_list)
    else:
        print ( "No Instances to delete ")

    