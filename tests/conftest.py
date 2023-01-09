import os
import uuid

from chalice.test import Client
import app as chalice_app
from typing import Generator, Any
import pytest
import docker as libdocker
from chalice import Chalice
import warnings
from chalicelib.adapters.repositories.entity.products import ProductTable
from tests.test_helpers import ping_dynamo
@pytest.fixture(scope="session", autouse=True)
def app() -> Chalice:
    return chalice_app


@pytest.fixture(scope="session", autouse=True)
def chalice_client(app):
    with Client(app) as client:
        yield client


@pytest.fixture(scope="session")
def docker() -> Generator[libdocker.APIClient, None, None]:
    with libdocker.APIClient(version="auto") as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def dynamo_server(docker: libdocker.APIClient) -> Generator[Any, None, None]:
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    container = docker.create_container(
        image="localstack/localstack:0.11.3",
        name=f"test-localstack-{uuid.uuid4()}",
        detach=True,
        ports=[
            "5555",
            "4569"
        ],
        environment=[
            "DATA_DIR=/tmp/localstack/data",
            "DEBUG=1",
            "DEFAULT_REGION=ap-northeast-2",
            "LAMBDA_EXECUTOR=docker-reuse",
            "HOSTNAME=localstack"

        ],
        volumes=["/var/run/docker.sock:/var/run/docker.sock",
                 "localstack:/tmp/localstack/data"],
        host_config=docker.create_host_config(port_bindings={  "4566": "4566"}),
    )
    docker.start(container=container["Id"])
    try:
        ping_dynamo(str(os.getenv("LOCAL_DYNAMO")))
        yield container
    finally:
        docker.kill(container["Id"])
        docker.remove_container(container["Id"])

@pytest.fixture(scope="session", autouse=True)
def apply_migrations(dynamo_server: None) -> None:
    try:
        ProductTable.create_table(wait=True)
    except Exception as e:
        raise e
    finally:
        ProductTable.delete_table()
