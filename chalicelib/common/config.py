from os import getenv
"""
reference: https://rogulski.it/dynamodb-with-fastapi/
"""


aws_key = getenv("aws_key")
environment = getenv("aws_secret_key")
aws_secret_key = getenv("aws_secret_key")
DB_HOST = getenv("DB_HOST") if environment in ["local", "test"] else None
region = "ap-northeast-2"
local_dynamodb = getenv("LOCAL_DYNAMO","http://localhost:4569")