import boto3
import os

# Replace with your AWS credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = 'us-east-2'  # e.g., 'us-east-1'

# Create a DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Replace with the name of your DynamoDB table
table_name = 'HouseListings'

# Get the table
table = dynamodb.Table(table_name)

# Get the primary key structure
key_schema = table.key_schema

# Print the primary key information
print(f"Primary Key Structure for Table: {table_name}")
print("-------------------------------------------")

# Check if the table has a composite primary key
if len(key_schema) > 1:
    print("Composite Primary Key:")
    for key in key_schema:
        key_type = key['KeyType']
        attribute_name = key['AttributeName']
        print(f"{key_type}: {attribute_name}")
else:
    print("Partition Key:")
    partition_key = key_schema[0]
    partition_key_name = partition_key['AttributeName']
    print(f"Partition Key Name: {partition_key_name}")

print("-------------------------------------------")