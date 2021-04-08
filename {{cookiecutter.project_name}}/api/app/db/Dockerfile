#
# Dockerfile for DynamoDB Local
#
# https://aws.amazon.com/blogs/aws/dynamodb-local-for-desktop-development/
#
FROM amazon/dynamodb-local:latest

EXPOSE 8000

CMD  ["-jar DynamoDBLocal.jar", "-optimizeDbBeforeStartup", "-dbPath", "./data", "-port 8000"]