
# AWS CDK Python Lab

## Before you start

This repository uses the AWS CDK to deploy infrastructure as code and Lambda functions.  To prevent conflicts. the root stack name needs to be changed in the app.py file, or copy the needed components into a new stack created via `cdk init`


## Setup

After cloning repository, to manually create a virtualenv on Cloud 9:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


## References

- https://aws.amazon.com/blogs/devops/deploying-a-serverless-application-using-aws-cdk/
- https://aws.amazon.com/blogs/mobile/building-real-time-serverless-apis-with-postgres-cdk-typescript-and-aws-appsync/
- https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html
- MySQL: https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html


## Lab details

- DataSource: https://gist.github.com/curran/a08a1080b88344b0c8a7
- https://www.pulumi.com/blog/aws-lambda-efs/