import boto.ec2
import time

# Cretae connection to the region
print "Connecting to region ..."
time.sleep(5)
conn = boto.ec2.connect_to_region('ap-south-1')

# Creating EC2 instance
print "Creating EC2 instance ..."
conn.run_instances('ami-fedb8f91', instance_type='t2.micro')
time.sleep(120)
reservations=conn.get_all_instances();

# Stop/Start/Terminate the created instances (if more than one will stop all)
for reservation in reservations:
    for instances in reservation.instances:
        i_id =  instances.id
        if instances.state != 'terminated':
            print "Stopping the instance ..."
            conn.stop_instances(instance_ids=[i_id])
            time.sleep(120)
            print "Starting the instance ..."
            conn.start_instances(instance_ids=[i_id])
            time.sleep(120)
            print "Terminating the instance ..."
            conn.terminate_instances(instance_ids=[i_id])
