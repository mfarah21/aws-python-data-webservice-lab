#!/usr/bin/env python3

from aws_cdk import core

from aws_python.aws_python_stack import AwsPythonStack


app = core.App()
AwsPythonStack(app, "aws-python")

app.synth()
