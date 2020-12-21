from aws_cdk import (core,aws_ec2,aws_rds)

class CdkRdsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Ceate Aurora Cluster with 2 instances with CDK High Level API
        # Secrets Manager auto generate and keep the password, don't put password in cdk code directly
        db_Aurora_cluster = aws_rds.DatabaseCluster(self, "MyAurora",
                                                default_database_name="MyAurora",
                                                engine=aws_rds.DatabaseClusterEngine.aurora(
                                                    version=aws_rds.AuroraEngineVersion.VER_1_22_2
                                                ),
                                                instance_props=aws_rds.InstanceProps(
                                                    vpc=vpc,
                                                    vpc_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.ISOLATED),
                                                    instance_type=aws_ec2.InstanceType(instance_type_identifier="t2.small")
                                                ),
                                                instances=2,
                                            )
