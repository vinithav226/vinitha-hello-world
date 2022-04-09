import json

import logging
import boto3

BUCKET_NAME ='dev-days-test'
KEY = 'hello.txt'
# Get the service client
s3 = boto3.resource('s3')

# Download object at bucket-name with key-name to tmp.txt
#s3.download_file("bucket-name", "key-name", "tmp.txt")
logging.getLogger().setLevel(logging.INFO)

def lambda_handler(event, context):
    logging.info(event)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/hello_local.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] =="404":
            logging.error('Object not found')
        else:
            raise e
            
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
