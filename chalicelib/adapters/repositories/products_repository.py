import abc
import time
import uuid
from typing import Any

from chalicelib.adapters.repositories.entity.products import ProductTable
from chalicelib.apis.dtos.products import ProductSchemaIn


class AbstractProductRepository(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def _process_create(values: dict[str, Any]) -> dict[str, Any]:
        ...

    @classmethod
    @abc.abstractmethod
    def create(cls, **kwargs) -> dict[str, Any]:
        ...

    @classmethod
    @abc.abstractmethod
    def get(cls, partition_key: str) -> dict[str, Any]:
        ...


class ProductRepository(AbstractProductRepository):
    table: ProductTable = ProductTable

    @staticmethod
    def _process_create(values: dict[str, Any]) -> dict[str, Any]:
        timestamp_now = time.time()
        values |= {"id": str(uuid.uuid4), "created_at": timestamp_now, "updated_at": timestamp_now}
        return values

    @classmethod
    def create(cls, product_in: ProductSchemaIn) -> dict[str, Any]:
        data = cls._process_create(product_in.dict())
        model = cls.table(**data)
        model.save()
        return model.attribute_values

    @classmethod
    def get(cls, partition_key:str) -> dict[str, Any]:
        model = cls.table.get(partition_key)
        return model.attribute_values
