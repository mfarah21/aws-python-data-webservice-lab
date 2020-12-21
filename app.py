#!/usr/bin/env python3

from aws_cdk import core

from aws_python.aws_python_stack import AwsPythonStack
from aws_python.cdk_vpc_stack import CdkVpcStack
from aws_python.cdk_rds_stack import CdkRdsStack


app = core.App()

vpc_stack = CdkVpcStack(app, "cdk-vpc")
rds_stack = CdkRdsStack(app, "cdk-rds", vpc=vpc_stack.vpc)
AwsPythonStack(app, "tomc-aws-python", vpc=vpc_stack.vpc)

app.synth()
