from aws_cdk import (core,aws_ec2,aws_rds)

class AwsPythonRdsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Ceate Aurora Cluster with 2 instances with CDK High Level API
        # Secrets Manager auto generate and keep the password, don't put password in cdk code directly
        # db_Aurora_cluster = aws_rds.DatabaseCluster(self, "MyAurora",
        #                                         default_database_name="MyAurora",
        #                                         engine=aws_rds.DatabaseClusterEngine.aurora(
        #                                             version=aws_rds.AuroraEngineVersion.VER_1_22_2
        #                                         ),
        #                                         instance_props=aws_rds.InstanceProps(
        #                                             vpc=vpc,
        #                                             vpc_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.ISOLATED),
        #                                             instance_type=aws_ec2.InstanceType(instance_type_identifier="t2.small")
        #                                         ),
        #                                         instances=2,

        #                                     )

        print(f'VPC = {vpc}')

        self.rds_securitygroup = aws_ec2.SecurityGroup(self, "Rds Security Group",
        description= "Security group for database",
        security_group_name= "Aurora Rds Security Group",
        vpc = vpc,
        )

        # Aurora Lamnda security group
        self.rdsclient_securitygroup = aws_ec2.SecurityGroup(self, "Rds Client Security Group",
        description= "Allows lambda access to VPC",
        security_group_name= "Aurora Lambda Security Group",
        vpc = vpc
        )
        
        self.rds_securitygroup.add_ingress_rule(self.rdsclient_securitygroup,aws_ec2.Port.tcp(3306),"Allow RDS client security group members access to RDS on port 3306")

        # subnet_ids = []
        # for subnet in vpc.isolated_subnets:
        #     print(f'Appending subnet {subnet.subnet_id}')
        #     subnet_ids.append(subnet.subnet_id)

        # subnet_group = aws_rds.CfnDBSubnetGroup(
        #     self,
        #     id="AuroraServerlessSubnetGroup",
        #     db_subnet_group_description='Aurora Postgres Serverless Subnet Group',
        #     subnet_ids=subnet_ids,
        #     db_subnet_group_name='auroraserverlesssubnetgroup' # needs to be all lowercase
        # )
        
        # print(f'Subnet Group = {subnet_group}')
        
        self.rds = db_serverless_cluster = aws_rds.ServerlessCluster(self, "AnotherCluster",
            engine=aws_rds.DatabaseClusterEngine.AURORA_MYSQL,
            # engine=aws_rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
            # parameterGroup=aws_rds.ParameterGroup.fromParameterGroupName(self, 'ParameterGroup', 'default.aurora-postgresql10'),
            default_database_name='Flowers',
            vpc=vpc,
            # subnet_group=subnet_group,
            security_groups=[self.rds_securitygroup],
            enable_data_api=True,
            scaling=aws_rds.ServerlessScalingOptions(auto_pause=None)
            # scaling: { autoPause: cdk.Duration.seconds(0) } // Optional. If not set, then instance will pause after 5 minutes 
        )
        
        self.cluster_arn = self.rds.cluster_arn
        self.secret_arn = self.rds.secret.secret_arn

