from aws_cdk import (core,aws_dynamodb,aws_lambda,aws_efs,aws_rds,aws_ec2,aws_secretsmanager)


class AwsPythonFlywayStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc, rds_endpoint, secret_arn, clientsecuritygroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # Create EFS
        self.flyway_efs = aws_efs.FileSystem(self,'Flyway EFS',vpc=vpc,file_system_name='flyway')
        self.flyway_efs_access_point = aws_efs.AccessPoint(self,'Flyway EFS AccessPoint',
        file_system=self.flyway_efs,
        posix_user=aws_efs.PosixUser(gid='1000',uid='1000')
        )

        # Create the efsload Lamnda
        efsload_lambda = aws_lambda.Function(self,'EfsLoadLambda',
        handler='efsload-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        vpc = vpc,
        timeout = core.Duration.minutes(1),
        filesystem=aws_lambda.FileSystem.from_efs_access_point(ap=self.flyway_efs_access_point,mount_path='/mnt/flyway')
        )

        # Create the efsdump Lamnda
        efsdump_lambda = aws_lambda.Function(self,'EfsDumpLambda',
        handler='efsdump-handler.handler',
        runtime=aws_lambda.Runtime.PYTHON_3_7,
        code=aws_lambda.Code.asset('lambda'),
        vpc = vpc,
        timeout = core.Duration.minutes(1),
        filesystem=aws_lambda.FileSystem.from_efs_access_point(ap=self.flyway_efs_access_point,mount_path='/mnt/flyway')
        )

        # Copy SQL files into EFS
        
        # Launch flyway container with EFS mount point