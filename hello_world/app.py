import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count')

def lambda_handler(event, context):
    # Get current count
    response = table.get_item(Key={'id': 'visitors'})
    
    if 'Item' in response:
        count = int(response['Item']['count']) + 1
    else:
        count = 1
    
    # Update count in DynamoDB
    table.put_item(Item={'id': 'visitors', 'count': count})
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps({'count': count})
    }