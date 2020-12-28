from aws_cdk import core
from aws_cdk import (aws_ec2)

class AwsPythonVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        self.vpc = aws_ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.10.0.0/16",
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[aws_ec2.SubnetConfiguration(
                               subnet_type=aws_ec2.SubnetType.PUBLIC,
                               name="Public Subnets",
                               cidr_mask=24
                           ), aws_ec2.SubnetConfiguration(
                               subnet_type=aws_ec2.SubnetType.PRIVATE,
                               name="Private Subnets",
                               cidr_mask=24
                           ), aws_ec2.SubnetConfiguration(
                               subnet_type=aws_ec2.SubnetType.ISOLATED,
                               name="Isolated Subnets",
                               cidr_mask=24
                           )
                           ],
                           # nat_gateway_provider=ec2.NatProvider.gateway(),
                           nat_gateways=2,
                           )

        core.CfnOutput(self, "Output", value=self.vpc.vpc_id)
