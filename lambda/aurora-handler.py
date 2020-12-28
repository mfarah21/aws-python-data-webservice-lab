import json
import sys
import logging
import pymysql

#rds settings
rds_host  = "tomc-aws-python-rds-anothercluster9d7c9369-11upxqxzst1zj.cluster-cxjbbr1ngwyo.us-east-2.rds.amazonaws.com"
name = "admin"
password = "password"
db_name = "Flowers"


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()


logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")



def handler(event, context):
    # print('request: {}'.format(json.dumps(event)))
    
    
    
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Response from Aurora Lambda. You have hit {}\n'.format(event['path'])
    }
