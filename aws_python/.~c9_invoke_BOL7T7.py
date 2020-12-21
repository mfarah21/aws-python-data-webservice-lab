from aws_cdk import (core,aws_dynamodb,aws_lambda,aws_apigateway)


class AwsPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # base API
        base_api = aws_apigateway.RestApi(self, 'ApiGatewayForGetData', rest_api_name='ApiGatewayForGetData')



        # Hello Lambda
        hello_lambda = aws_lambda.Function(self,'GetDataLambda',
        handler='hello-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        )

        # Add webservice /hello -> hello lambda
        hello_resource = base_api.root.add_resource('hello')
        hello_lambda_integration = aws_apigateway.LambdaIntegration(hello_lambda)
        hello_resource.add_method('GET', hello_lambda_integration)

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
        