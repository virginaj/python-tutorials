import boto3


def create_instance():

    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=1,InstanceType='t2.micro',
                SecurityGroupIds=['sg-05198f9df4a5885af'],KeyName='fullstack')
    
    instances =[1,2,3]
    for instance in instances.items():
        print instance.items

    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instances[instance].id])
    print ("Instance is Running now!")


create_instance()


# ec2_client.terminate_instances(InstanceIds=instance_list,DryRun=False)