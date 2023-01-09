from chalice import Blueprint
from chalicelib.adapters.repositories.products_repository import ProductRepository
from chalicelib.apis.dtos.products import ProductSchemaOut, ProductSchemaIn
from typing import Union, Any
router = Blueprint(__name__)
JSONType = Union[str, int, float, bool, None, dict[str, Any], list[Any]]

"""
python json typing 
https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
"""


@router.route("/products/{name}", methods=["GET"])
def get_product(name: str) -> JSONType:
    """
    :request: name:str
    :return: ProductSchemaOut
    """
    """
    TODO:
    - query pattern
    """
    return ProductRepository.get(name)


@router.route("/products", methods=["POST"])
def create_product() -> JSONType:
    """
    :request:ProductSchemaIn
    :return: ProductSchemaOut
    """
    """
    TODO:
    -   command pattern
        #return ProductRepository().create(request).json()
    """
    typed_request = ProductSchemaIn(**router.current_request.json_body)

    product = ProductRepository.create(typed_request)
    return ProductSchemaOut(**product).json()
