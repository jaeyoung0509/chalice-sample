# chalice-sample

## requirements
- chalice: serverless micro framework
- pydantic: validation
- pynamodb: A Pythonic interface for Amazon's DynamoDB.
- local stack

### local stack usage
```shell
aws --endpoint-url=http://localhost:4569 dynamodb describe-table --table-name product-table | grep TableStatus
```