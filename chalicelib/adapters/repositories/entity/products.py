import os

from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model
class ProductNameIndex(GlobalSecondaryIndex["ProductTable"]):
    """
    Represents a global secondary index for ProductTable
    """
    class Meta:
        index_name = "product_name_index"
        read_capacity_units = 10
        write_capacity_units = 10
        projection = AllProjection()

    name = UnicodeAttribute(hash_key=True)
    updated_at = NumberAttribute(range_key=True)


class ProductTable(Model):
    class Meta:
        region = "ap-northeast-2"
        table_name = "product-table"
        host = os.getenv("LOCAL_DYNAMO")
        read_capacity_units = 5
        write_capacity_units = 5

    id = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(hash_key=True, null=False)
    description = UnicodeAttribute(null=False)
    created_at = NumberAttribute(null=False)
    updated_at = NumberAttribute(null=False)
    product_name_index = ProductNameIndex()




