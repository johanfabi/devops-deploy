# AWS Python Lambda Function Hello World Example
import json
from dotenv import load_dotenv
import os

load_dotenv()

MESSAGE = os.getenv("MESSAGE")

def lambda_handler(event, context):
    # Log the event argument for debugging and for in-depth troubleshooting
    print("Received event: " + json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps(MESSAGE)
    }