# AWS Lambda & Serverless API

## Project Overview

A serverless REST-style API built using AWS Lambda, Amazon API Gateway, and Python.

This project demonstrates event-driven computing, Lambda function execution, API Gateway integration, and HTTP API responses without managing servers.

## Objectives

- Understand serverless computing.
- Learn AWS Lambda fundamentals.
- Create and test a Lambda function.
- Understand Amazon API Gateway.
- Integrate API Gateway with Lambda.
- Build and deploy a simple serverless API.

## Technologies Used

- AWS Lambda
- Amazon API Gateway (HTTP API)
- Python
- AWS IAM
- Amazon CloudWatch
- GitHub

## Architecture

Client → API Gateway → AWS Lambda → JSON Response

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Returns project information |
| GET | `/health` | Returns API health status |

## Deployment Steps

1. Created a Python AWS Lambda function.
2. Implemented the Lambda handler.
3. Tested the function using Lambda test events.
4. Created an Amazon API Gateway HTTP API.
5. Connected API Gateway routes to Lambda.
6. Enabled automatic deployment.
7. Tested the public API endpoints.

## Security

- Used a Lambda IAM execution role.
- Granted API Gateway permission to invoke Lambda.
- Did not expose AWS access keys or credentials.
- Kept the demonstration API limited to read-only responses.

## Live API

**Base URL:** https://uehqswi3g4.execute-api.ap-southeast-2.amazonaws.com/

**Health Endpoint:** https://uehqswi3g4.execute-api.ap-southeast-2.amazonaws.com/health

## Project Screenshots

Add screenshots showing:

- Lambda function configuration
- Lambda test execution
- API Gateway routes
- Lambda integration
- Successful browser API response

## Key Learnings

- Serverless computing eliminates the need to manage application servers.
- Lambda executes code in response to events.
- API Gateway provides HTTPS endpoints for backend services.
- IAM controls access to AWS resources.
- CloudWatch helps monitor Lambda execution.

## Conclusion

Successfully developed and deployed a simple serverless API using AWS Lambda and Amazon API Gateway.

**Learning Program:** Codomax Digital Solutions
