from collections.abc import Callable
from typing import TYPE_CHECKING, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def parameters(param_func: Callable[P, R]):
    """Decorator for parameter type hints without runtime overhead.

    Uses param_func signature for type checking while preserving original function at runtime.
    """
    S2 = TypeVar("S2")
    P2 = ParamSpec("P2")
    R2 = TypeVar("R2")
    P3 = ParamSpec("P3")
    R3 = TypeVar("R3")

    def decorator(func: Callable[Concatenate[S2, P2], R2], _: Callable[P3, R3] = param_func):
        def wrapper(self: S2, *args: P3.args, **kwargs: P3.kwargs) -> R2:
            return func(self, *args, **kwargs)

        return wrapper if TYPE_CHECKING else func

    return decorator
