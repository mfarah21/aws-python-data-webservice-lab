# Lab Agenda

## Overview
This is a interactive lab for a small group of developers.  The goal is to understand:

- How Principal manages AWS accounts
- How to connect to an AWS account using browser
- Introduction to Cloud 9 IDE
- Creation of a basic solutions using core services: S3, Lambda, DynamoDB, API Gateway, SQS, SSM
- Building solutions using the AWS Console, CloudFormation and AWS CDK
- Use of GitHub repositories and workflow with AWS platform

## Prerequisites
- Request an AWS Sandbox - [Requesting a New PFG AWS Account](https://docs.principal.com/display/AWS/Requesting+a+New+PFG+AWS+Account)
- GitHub licenses for all developers attending - [Github Cloud User Guide](https://docs.principal.com/display/ECH/Github+Cloud+User+Guide)
- Cloud enabled ER accounts for all developers attending - [Creating an Alternate Account to Administer Cloud Resources](https://docs.principal.com/display/AWS/Creating+an+Alternate+Account+to+Administer+Cloud+Resources)
- Custom role "Developer" within the AWS Sandbox - [Creating a Custom AWS Role with SSO Access](https://docs.principal.com/display/AWS/Creating+a+Custom+AWS+Role+with+SSO+Access)
- Proctor access to AWS Sandbox, share name of entitlement with Proctor, or add Proctor's Alternate Account to entitlement
- Submit sample data for the team's service to be used in lab
- Completion of the Node.js tutorial, to get basic understanding of JavaScript
- Firefox installed

## Lab Steps

### Part 1 - Getting connected

- Get credentials from password vault for cloud enabled ER account
- Launch Firefox as cloud enabled ER account
- Select from available AWS account roles
- Overview of AWS console

### Part 2 - Lambda Editor
- Create Hello World lambda
- [Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- Print environment variables
```
import os

...

print(os.environ)
```
- Review logs
- Understand "testing" tools
- Update timeouts for Lambda

### Part 3 - DynamoDB
- Create DynamoDB table
- IAM permissions
- Read/write to table from Lambda

### Part 4 - API Gateway
- Connect API Gateway to Lambda
- Create GET web service that can retrieve data from DynamoDB using Browser

### Part 5 - Cloud 9 IDE
- Create Cloud 9 IDE
- Discuss sharing capabilities
- Curl
- AWS CLI
- Debugging Lambda

### Part 6 - CloudFormation
- Re-create above solution using CloudFormation
- Lambda first, then DynamoDB, then API Gateway
- Create Stack + Delete Stack
- Create Stack Change Sets
- Set environment variables

### Part 7 - AWS CDK
- PreAssignment: [CDK Workshop](https://cdkworkshop.com/)
- Change your stack name - Multiple Students, One Account of [CDK Intro Workshop](https://docs.principal.com/display/AWS/CDK+Intro+Workshop)
- Convert CloudFormation to using AWS CDK
- [https://github.com/cdk-patterns](https://github.com/cdk-patterns)

### Part 8 - More services
- S3 buckets
- SQS messaging
- SSM property stores
- Scheduled Lambda using CloudWatch events
- Triggering Lambda on S3 / SQS events

### Part 9 - GitHub
- Creating repositories
- Creating groups
- Connecting to GitHub repository using Cloud 9
- Working with branches

### Part 10 - GitHub Advanced
- Create GitHub Actions to deploy AWS CDK to AWS account
- [Two Lambda and AWS CDK](https://docs.principal.com/display/ECH/Two+Lambda+and+AWS+CDK)
- Principal AWS CDK

### Part 11 - RDS
- Introduction to VPC
- Introduction to RDS
- Creating VPC and RDS via AWS CDK

### Part 12 - API Key Authentication
- API Key authentication
- What are Usage Plans?  What are API Keys?  How to compare this technology to Developer Apps accessing Apigee Products
- Alternatives?  Cognito User Pools?  ForgeRock?

## Additional Resources
- Team Channel: [Amazon Community Teams channel](https://teams.microsoft.com/l/team/19%3a59013c925026486ebe40c115d34b6493%40thread.tacv2/conversations?groupId=e534b89f-cad9-4262-8c7b-e1147d3bf852&tenantId=3bea478c-1684-4a8c-8e85-045ec54ba430)
- [https://github.com/PrincipalFinancialGroup/aws-cdk-library](https://github.com/PrincipalFinancialGroup/aws-cdk-library)
- [https://github.com/PrincipalFinancialGroup/pfg-awesome-cloud](https://github.com/PrincipalFinancialGroup/pfg-awesome-cloud)
- [TypeScript](https://docs.principal.com/display/WEB/TypeScript), especially Async TypeScript course
- [Tips for using Cloud9](https://docs.principal.com/display/AWS/Tips+for+using+Cloud9)
