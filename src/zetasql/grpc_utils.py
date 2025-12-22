from google.protobuf import message as _message
from typing import TypeVar, ParamSpec, Callable, Concatenate
from zetasql.client import WasmClient

Message = TypeVar("Message", bound=_message.Message)

P = ParamSpec("P")
R = TypeVar("R")
def grpc_method(request_type: Callable[P, R]):
    S2 = TypeVar("S2")
    P2 = ParamSpec("P2")
    R2 = TypeVar("R2")
    P3 = ParamSpec("P3")
    R3 = TypeVar("R3")
    def decorator(func: Callable[Concatenate[S2, P2], R2], _: Callable[P3, R3] = request_type):
        def wrapper(self: S2, *args: P3.args, **kwargs: P3.kwargs) -> R2:
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def call_grpc_func(client: WasmClient, func_name: str, request: _message.Message, response_type: type[Message]) -> Message:
    request_data = request.SerializeToString()
    response_data = client.call_rpc_method(func_name, request_data)
    response = response_type.FromString(response_data)
    return response
