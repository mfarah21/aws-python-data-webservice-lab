import json
import decimal
import os
import boto3
from botocore.exceptions import ClientError


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# set environment variable
TABLE_NAME = os.environ['TABLE_NAME']

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    table = dynamodb.Table(TABLE_NAME)
    # Scan items in table
    try:
        response = table.scan()
        print("Response Start")
        print(response)
        print("Response End")
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        # print item of the table - see CloudWatch logs
        for i in response['Items']:
            print(i)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response['Items'])

    }