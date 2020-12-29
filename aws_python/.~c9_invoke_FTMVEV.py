from aws_cdk import (core,aws_ec2,aws_rds)

class AwsPythonRdsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Rds Security group
        self.rds_securitygroup = aws_ec2.SecurityGroup(self, "Rds Security Group",
        description= "Security group for database",
        security_group_name= "Aurora Rds Security Group",
        vpc = vpc,
        )

        # Rds Client security group
        self.rdsclient_securitygroup = aws_ec2.SecurityGroup(self, "Rds Client Security Group",
        description= "Allows lambda access to VPC",
        security_group_name= "Aurora Lambda Security Group",
        vpc = vpc
        )
        
        self.rds_securitygroup.add_ingress_rule(self.rdsclient_securitygroup,aws_ec2.Port.tcp(3306),"Allow RDS client security group members access to RDS on port 3306")

        self.rds = db_serverless_cluster = aws_rds.ServerlessCluster(self, "AuroraRds",
            engine=aws_rds.DatabaseClusterEngine.AURORA_MYSQL,
            # engine=aws_rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
            # parameterGroup=aws_rds.ParameterGroup.fromParameterGroupName(self, 'ParameterGroup', 'default.aurora-postgresql10'),
            default_database_name='Flowers',
            vpc=vpc,
            security_groups=[self.rds_securitygroup],
            enable_data_api=True,
            scaling=aws_rds.ServerlessScalingOptions(auto_pause=None)
        )
        
        
        
        self.cluster_arn = self.rds.cluster_arn
        self.secret_arn = self.rds.secret.secret_arn
        self.rds_endpoint = self.rds.cluster_endpoint
        






































