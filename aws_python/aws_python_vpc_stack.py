from aws_cdk import (core,aws_ec2)

class AwsPythonVpcStack(core.Stack):
    
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        print("Building VPC")
        # Create a Vpc with 3 groups in 2 AZs
        # This will create 6 subnets
        self.vpc = aws_ec2.Vpc(self, "Vpc",
            max_azs=2,
            cidr="10.10.0.0/16",
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                   subnet_type=aws_ec2.SubnetType.PUBLIC,
                   name="Public Subnets",
                   cidr_mask=24
                ),
                aws_ec2.SubnetConfiguration(
                   subnet_type=aws_ec2.SubnetType.PRIVATE,
                   name="Private Subnets",
                   cidr_mask=24
                ),
                aws_ec2.SubnetConfiguration(
                   subnet_type=aws_ec2.SubnetType.ISOLATED,
                   name="Isolated Subnets",
                   cidr_mask=24
                )
            ],
            nat_gateways=2,
            )
            
        core.Tags.of(self.vpc).add("Name", id)

        core.CfnOutput(self, "Output", value=self.vpc.vpc_id)
