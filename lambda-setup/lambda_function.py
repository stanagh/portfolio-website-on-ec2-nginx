import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    start_stop_tag = {'Key': 'Name', 'Value': 'app-nginx'}
    
    action = event.get('action', "stop")
    
    for region in regions:
        ec2_client = boto3.client('ec2', region)
        all_instances = ec2_client.describe_instances()
        if all_instances:
            print("List all instances:")
            for reservation in all_instances['Reservations']:
                for instance in reservation['Instances']:
                    print(instance['InstanceId'] + " - " + instance['State']['Name'])
                    
                    if action == "stop":
                        if start_stop_tag in instance['Tags']:
                            if instance['State']['Name'] == 'running':
                                print("Stopping ec2: " + instance['InstanceId'])
                                ec2_client.stop_instances(InstanceIds=[instance['InstanceId']])
                    
                    if action == "start":
                        if start_stop_tag in instance['Tags']:
                            if instance['State']['Name'] == 'stopped':
                                print("Starting ec2: " + instance['InstanceId'])
                                ec2_client.start_instances(InstanceIds=[instance['InstanceId']])