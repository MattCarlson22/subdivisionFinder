import os
import boto3

# Load AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Connect to DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-2'  # Replace with your region
)

# Access the HouseListings table
table_name = 'HouseListings'
table = dynamodb.Table(table_name)

# Scan the table with a FilterExpression and limit the results to 100
response = table.scan(
    # FilterExpression=boto3.dynamodb.conditions.Attr('address').contains('Phoenix')
)

# Get the list of items
items = response.get('Items', [])
subdivisions = [item['subdivision'].upper() for item in items]

subdivisions = sorted(subdivisions)

# Print the listings
for index, item in enumerate(subdivisions):
    print(f"Listing {index + 1}: {item}")

# Print the total number of listings retrieved
print(f"Total listings retrieved: {len(items)}")