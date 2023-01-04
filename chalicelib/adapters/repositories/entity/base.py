from pynamodb.models import Model
from chalicelib.common.config import  region, local_dynamodb
class Base(Model):
    class Meta:
        host = local_dynamodb
        region = region
