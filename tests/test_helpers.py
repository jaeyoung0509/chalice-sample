import logging
import time
from functools import wraps
from typing import Any, Callable, Type
from pynamodb.connection import  Connection
from pynamodb.exceptions import PynamoDBConnectionError

def do_with_retry(
    catching_exc: Type[Exception], reraised_exc: Type[Exception], error_msg: str
) -> Callable:  # pragma: no cover
    def outer_wrapper(call: Callable) -> Callable:
        @wraps(call)
        def inner_wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 0.001
            for _ in range(13):
                try:
                    return call(*args, **kwargs)
                except catching_exc:
                    time.sleep(delay)
                    delay *= 2
            else:  # pragma: no cover
                raise reraised_exc(error_msg)

        return inner_wrapper

    return outer_wrapper

@do_with_retry(PynamoDBConnectionError, RuntimeError, "can't connect' to DynamoDB")
def ping_dynamo(dsn: str) -> None:
    logging.getLogger().debug("ping_dynamo")
    conn = Connection(host=dsn)
    print(conn.session)