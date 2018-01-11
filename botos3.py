from boto.s3.connection import S3Connection

# Connecting to S3
conn = S3Connection()

# Creating a S3 bucket
bucket = conn.create_bucket('sobisw-mybucket')

# verifying if the bucket exists
nonexistent = conn.get_bucket('sobisw-mybucket')

# delete bucket if exists
if nonexistent is None:
    print "No such bucket!"
else:
    conn.delete_bucket('sobisw-mybucket')
