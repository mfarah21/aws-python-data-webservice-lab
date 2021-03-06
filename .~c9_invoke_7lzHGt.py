#!/usr/bin/env python3

from aws_cdk import core

from aws_python.aws_python_app_stack import AwsPythonAppStack
from aws_python.aws_python_vpc_stack import AwsPythonVpcStack
from aws_python.aws_python_mysql_rds_stack import AwsPythonMysqlRdsStack
from aws_python.aws_python_postgres_rds_stack import AwsPythonPostgresRdsStack

rootstackname = "tomc-aws-python-v2-"

app = core.App()

vpc_stack = AwsPythonVpcStack(app, rootstackname+"vpc")
rds_stack = AwsPythonPostgresRdsStack(app, rootstackname+"rds", vpc=vpc_stack.vpc)
rds_stack = AwsPythonPostgresRdsStack(app, rootstackname+"rds", vpc=vpc_stack.vpc)
# AwsPythonAppStack(app, rootstackname+"app", vpc=vpc_stack.vpc, rds_endpoint=rds_stack.rds_endpoint, secret_arn = rds_stack.secret_arn, clientsecuritygroup = rds_stack.rdsclient_securitygroup)

app.synth()
