# STEPS FOR EXECUTION:

1. Create an user in AWS with poweruser role (based on requirment, you can change the role)
2. Get the access key id and secret access key
3. In you system, create a file named .boto and add the following lines:
  [Credentials]
  aws_access_key_id = [your access key id]
  aws_secret_access_key = [ your secret access key ]
  and changed the file permission to 600 (chmod 600 .boto)
4. export this environment variable => export BOTO_CONFIG='your/path/to/.boto/file'
5. Execute the script

NOTE: This script is very basic and it will be modified later
