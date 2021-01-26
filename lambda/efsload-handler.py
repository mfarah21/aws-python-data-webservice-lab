import json


def handler(event, context):
    print("Loading EFS")
    
    f = open('/mnt/flyway/flyway.conf','w')
    f.write("Hello World")
    f.close()
    
    