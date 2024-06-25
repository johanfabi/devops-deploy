#!/bin/bash

set -e

FUNCTION_NAME="hello-world-lambda"
ZIP_FILE="lambda_function.zip"
HANDLER="lambda_function.lambda_handler"
ROLE="arn:aws:iam::810237447559:role/lambda-ex"
RUNTIME="python3.8"
REGION="us-east-1"

# Empaquetar la función Lambda
zip -r $ZIP_FILE . -x "*.git*" "*tests*" "*trust-policy.json" "deploy.sh" "Jenkinsfile"

# Desplegar la función Lambda
aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://$ZIP_FILE --region $REGION || \
aws lambda create-function --function-name $FUNCTION_NAME --zip-file fileb://$ZIP_FILE --handler $HANDLER --runtime $RUNTIME --role $ROLE --region $REGION
