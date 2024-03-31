import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('AIResearchFields')

    # Scan operation to retrieve all items from the table
    response = table.scan()

    titles = [item['Title'] for item in response['Items']]

    return {
        'statusCode': 200,
        'body': json.dumps(titles)
    }
