from aws_cdk import (core,aws_dynamodb,aws_lambda,aws_apigateway,aws_rds,aws_ec2,aws_secretsmanager)


class AwsPythonAppStack(core.Stack):

    # STEP 3 - add parameters

    def __init__(self, scope: core.Construct, construct_id: str, vpc, rds_endpoint, secret_arn, clientsecuritygroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # PART 1 - START

        # base API
        base_api = aws_apigateway.RestApi(self, 'ApiGatewayForGetData', rest_api_name='ApiGatewayForGetData')

        #
        #  Web Service responding to /hello.
        #   Resources: API resource, lambda
        #
        
        # Lambda function
        hello_lambda = aws_lambda.Function(self,'GetDataLambda',
        handler='hello-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        )

        # Add webservice /hello -> hello lambda
        hello_resource = base_api.root.add_resource('hello')
        hello_lambda_integration = aws_apigateway.LambdaIntegration(hello_lambda)
        hello_resource.add_method('GET', hello_lambda_integration)

        # PART 1 - END

        # PART 2 - START

        #
        #  Web Service responding to /dynamodb
        #   Resources: API resource, lambda, dynamodb
        #

        # DynamoDb table
        demo_table = aws_dynamodb.Table(
            self, "demo_table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )
        
        # Hello Lambda
        dynamodb_lambda = aws_lambda.Function(self,'GetDataFromDynamoDbLambda',
        handler='dynamodb-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        )
        dynamodb_lambda.add_environment("TABLE_NAME", demo_table.table_name)

        # Add webservice /dynamodb -> dynamodb lambda
        dynamodb_resource = base_api.root.add_resource('dynamodb')
        dynamodb_lambda_integration = aws_apigateway.LambdaIntegration(dynamodb_lambda)
        dynamodb_resource.add_method('GET', dynamodb_lambda_integration)

        demo_table.grant_read_data(dynamodb_lambda)
        
        # PART 2 - END
        
        # PART 3 - START

        #
        #  Web Service responding to /aurora
        #   Resources: API resource, lambda
        #   Stacks: vpc, rds
        #

        # PyMySql Layer
        pymysql_layer = aws_lambda.LayerVersion(self, 'PyMySql Layer', 
        layer_version_name = 'pymysql',
        code=aws_lambda.Code.asset('aws_python/layer-pymysql'),
        compatible_runtimes = [aws_lambda.Runtime.PYTHON_3_7],
        description='Layer for pymysql'
        )

        # Aurora Lambda
        aurora_lambda = aws_lambda.Function(self,'GetDataFromAuroraLambda',
        handler='aurora-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        vpc = vpc,
        security_group = clientsecuritygroup,
        timeout = core.Duration.minutes(1),
        layers=[pymysql_layer]
        )
        aurora_lambda.add_environment("RDS_HOST", rds_endpoint)
        aurora_lambda.add_environment("RDS_SECRET", secret_arn)

        # Add webservice /dynamodb -> dynamodb lambda
        aurora_resource = base_api.root.add_resource('aurora')
        aurora_lambda_integration = aws_apigateway.LambdaIntegration(aurora_lambda)
        aurora_resource.add_method('GET', aurora_lambda_integration)

        # grant lambda access to SSM
        secret = aws_secretsmanager.Secret.from_secret_complete_arn(self,'Rds Secret',secret_arn)
        secret.grant_read(aurora_lambda);
        
        # PART 3 - END
        
        