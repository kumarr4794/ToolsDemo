import boto3
import argparse

# Reference - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
# Simple py and boto3 script to check the bucket name exists in aws and create if not available,

# Creates a Normal S3 on AWS.
def create_bucket(bucketname):
    response = aws_resource.create_bucket(
        Bucket=bucketname,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2',
        },
    )
    print(response)

# To get the bucketname from user
def parse_args():
    parser = argparse.ArgumentParser(description='Create a S3')
    parser.add_argument('bucketname', required=True, help='aws region')
    args = parser.parse_args()
    return args

 # To check if the bucketexists in aws already
def checkIfExists(bucketname):
    try: 
        for Bucket in aws_resource.buckets.all():
            names = list(Bucket.name)
            if names == bucketname:
                print('Bucket Exists')
            else:
                create_bucket(bucketname)   
    except ValueError:
        print("Wrong Input!")

if __name__ == "__main__":
    args = parse_args() 
    aws_resource=boto3.resource("s3")
    bucketname=''
    checkIfExists(bucketname)