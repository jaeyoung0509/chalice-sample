from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from chalicelib.adapters.repositories.entity.base import Base
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

class ProductTable(Base):
    class Meta:
        table_name = "product-table"
        read_capacity_units = 5
        host = "http://localhost:4569"
        region = "ap-northeast-2"
        write_capacity_units = 5

    id = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(hash_key=True, null=False)
    description = UnicodeAttribute(null=False)
    created_at = NumberAttribute(null=False)
    updated_at = NumberAttribute(null=False)
    product_name_index = ProductNameIndex()




