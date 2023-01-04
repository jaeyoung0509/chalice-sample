from datetime import datetime

from pydantic import BaseModel


class ProductSchemaOut(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime


class ProductSchemaIn(BaseModel):
    name: str
    description: str
