import json
import sys
import logging
import pymysql
import os
import boto3
from botocore.exceptions import ClientError

#rds settings
rds_host  = os.environ['RDS_HOST'];
name = "admin"
password = ""
db_name = "Flowers"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name='us-east-2'
)
    
try:
    get_secret_value_response = client.get_secret_value(
        SecretId=os.environ['RDS_SECRET']
    )
except ClientError as e:
    logger.error(['Error']['Code'])
    if e.response['Error']['Code'] == 'DecryptionFailureException':
        # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
        # Deal with the exception here, and/or rethrow at your discretion.
        raise e
    elif e.response['Error']['Code'] == 'InternalServiceErrorException':
        # An error occurred on the server side.
        # Deal with the exception here, and/or rethrow at your discretion.
        raise e
    elif e.response['Error']['Code'] == 'InvalidParameterException':
        # You provided an invalid value for a parameter.
        # Deal with the exception here, and/or rethrow at your discretion.
        raise e
    elif e.response['Error']['Code'] == 'InvalidRequestException':
        # You provided a parameter value that is not valid for the current state of the resource.
        # Deal with the exception here, and/or rethrow at your discretion.
        raise e
    elif e.response['Error']['Code'] == 'ResourceNotFoundException':
        # We can't find the resource that you asked for.
        # Deal with the exception here, and/or rethrow at your discretion.
        raise e
else:
    # Decrypts secret using the associated KMS CMK.
    # Depending on whether the secret is a string or binary, one of these fields will be populated.
    if 'SecretString' in get_secret_value_response:
        password_response = json.loads(get_secret_value_response['SecretString'])
        password = password_response['password']
    # else:
    #     password = base64.b64decode(get_secret_value_response['SecretBinary'])
            
logger.info(password)


try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()


logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")



def handler(event, context):
    # print('request: {}'.format(json.dumps(event)))

    responseBody = "";

    with pymysql.cursors.DictCursor(conn) as cursor:
        # Read a single record
        sql = "SELECT * from Iris"
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info(f'Retrived {len(rows)} rows')

        first_row=True;
        responseBody = '['
        for row in rows:
            if (first_row):
                responseBody += '{'
                first_row=False;
            else:
                responseBody += ',{'
            first_item=True;                
            for key, value in row.items():
                if (first_item):
                    responseBody += f'"{key}":"{value}"'
                    first_item=False;
                else:
                    responseBody += f',"{key}":"{value}"'
            responseBody += '}'
        responseBody += ']'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': responseBody
    }
