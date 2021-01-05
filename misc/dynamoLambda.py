import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLENAMEHERE')

def lambda_handler(event, context):
    result = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }
