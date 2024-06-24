# AWS Python Lambda Function Hello World Example
import json

def lambda_handler(event, context):
    # Log the event argument for debugging and for in-depth troubleshooting
    print("Received event: " + json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
