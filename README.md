
# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

https://aws.amazon.com/blogs/devops/deploying-a-serverless-application-using-aws-cdk/
https://aws.amazon.com/blogs/mobile/building-real-time-serverless-apis-with-postgres-cdk-typescript-and-aws-appsync/
https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html


============

DataSource: https://gist.github.com/curran/a08a1080b88344b0c8a7
MySQL: https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html


CREATE DATABASE Flowers;


sepal_length	sepal_width	petal_length	petal_width	species

CREATE TABLE Iris (
sepal_length float, 
sepal_width float, 
petal_length float, 
petal_width float, 
species VARCHAR(20));


INSERT INTO Iris VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);

https://github.com/martinbpeters/cdk-vpc-postgres/blob/master/stacks/rds_aurora_serverless.py

SHOW DATABASES;
SHOW TABLES from Flowers;
SHOW COLUMNS from Iris from Flowers;
USE Flowers; SELECT * FROM Iris;
