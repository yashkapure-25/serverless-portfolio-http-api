
import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    path = event.get("rawPath", "/")

    if path == "/health":
        data = {
            "status": "healthy",
            "service": "serverless-portfolio-api"
        }
    else:
        data = {
            "message": "Welcome to my AWS Serverless API!",
            "project": "AWS Lambda & API Gateway",
            "developer": "Yash",
            "status": "success",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data)
    }
