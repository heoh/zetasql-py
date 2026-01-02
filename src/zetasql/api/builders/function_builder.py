"""
FunctionBuilder - Fluent API for building Function ProtoModel objects

This module provides a Java-style builder pattern for constructing functions,
making custom function creation much cleaner than manual protobuf manipulation.

Examples:
    >>> from zetasql.api.builders import FunctionBuilder, SignatureBuilder
    >>> from zetasql.types import TypeKind
    >>> from zetasql.core.types.proto_models import FunctionEnums
    >>> 
    >>> # Simple scalar UDF with single signature
    >>> my_udf = (FunctionBuilder("MY_UDF")
    ...     .add_signature(
    ...         SignatureBuilder()
    ...             .add_argument(TypeKind.TYPE_STRING)
    ...             .set_return_type(TypeKind.TYPE_INT64)
    ...             .build()
    ...     )
    ...     .build())
    >>> 
    >>> # Function with overloaded signatures
    >>> concat_func = (FunctionBuilder("CONCAT")
    ...     .set_group("STRING_OPS")
    ...     .add_signature(
    ...         SignatureBuilder()
    ...             .add_argument(TypeKind.TYPE_STRING)
    ...             .add_argument(TypeKind.TYPE_STRING)
    ...             .set_return_type(TypeKind.TYPE_STRING)
    ...             .build()
    ...     )
    ...     .add_signature(
    ...         SignatureBuilder()
    ...             .add_argument(TypeKind.TYPE_BYTES)
    ...             .add_argument(TypeKind.TYPE_BYTES)
    ...             .set_return_type(TypeKind.TYPE_BYTES)
    ...             .build()
    ...     )
    ...     .build())
    >>> 
    >>> # Function with optional/repeated arguments
    >>> variadic_func = (FunctionBuilder("GREATEST")
    ...     .add_signature(
    ...         SignatureBuilder()
    ...             .add_argument(TypeKind.TYPE_INT64, FunctionEnums.ArgumentCardinality.REQUIRED)
    ...             .add_argument(TypeKind.TYPE_INT64, FunctionEnums.ArgumentCardinality.REPEATED)
    ...             .set_return_type(TypeKind.TYPE_INT64)
    ...             .build()
    ...     )
    ...     .build())
"""

from typing import Union, List
from typing_extensions import Self
from zetasql.types import (
    Function, 
    FunctionSignature, 
    FunctionArgumentType,
    FunctionArgumentTypeOptions,
    Type, 
    TypeKind, 
    TypeFactory
)
from zetasql.core.types.proto_models import (
    FunctionEnums,
    SignatureArgumentKind,
)

# Function Mode enum values (from public.function_pb2.FunctionEnums)
# These are used directly as integers since FunctionEnums.Mode is not properly exposed in proto_models
class Mode:
    """Function mode enum values."""
    SCALAR = 1
    AGGREGATE = 2
    ANALYTIC = 3


class FunctionBuilder:
    """Builder for Function ProtoModel objects.
    
    Provides method chaining for fluent function construction. The builder
    creates ProtoModel objects that can be used directly with SimpleCatalog.
    
    Args:
        name: Function name (can be multi-part like "pkg.MY_UDF")
        group: Function group (default: "UDF")
        mode: Function mode (default: SCALAR)
    
    Examples:
        >>> # Basic scalar UDF
        >>> func = (FunctionBuilder("MY_UDF")
        ...     .add_signature(...)
        ...     .build())
        >>> 
        >>> # With custom group
        >>> func = (FunctionBuilder("CUSTOM_FUNC")
        ...     .set_group("MyFunctions")
        ...     .add_signature(...)
        ...     .build())
        >>> 
        >>> # Aggregate function
        >>> agg = (FunctionBuilder("MY_AGG")
        ...     .set_mode(FunctionEnums.Mode.AGGREGATE)
        ...     .add_signature(...)
        ...     .build())
    """
    
    def __init__(
        self, 
        name: str, 
        group: str = "UDF",
        mode: int = Mode.SCALAR
    ):
        """Initialize FunctionBuilder.
        
        Args:
            name: Function name. Can be simple ("MY_UDF") or qualified ("pkg.MY_UDF")
            group: Function group (default: "UDF"). Java uses non-null group.
            mode: Function mode - Mode.SCALAR (default), Mode.AGGREGATE, or Mode.ANALYTIC
        """
        # Split name into name_path (Java uses List<String> for namePath)
        name_path = name.split('.') if '.' in name else [name]
        
        self._function = Function(
            name_path=name_path,
            group=group,
            mode=mode,
            signature=[]
        )
    
    def set_group(self, group: str) -> Self:
        """Set function group.
        
        Args:
            group: Function group name (e.g., "UDF", "STRING_OPS", "zetasql")
        
        Returns:
            Self for method chaining
        """
        self._function.group = group
        return self
    
    def set_mode(self, mode: int) -> Self:
        """Set function mode.
        
        Args:
            mode: Mode.SCALAR (default), Mode.AGGREGATE, or Mode.ANALYTIC
        
        Returns:
            Self for method chaining
        """
        self._function.mode = mode
        return self
    
    def add_signature(self, signature: FunctionSignature) -> Self:
        """Add a function signature (allows overloading).
        
        Args:
            signature: FunctionSignature built by SignatureBuilder
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> builder.add_signature(
            ...     SignatureBuilder()
            ...         .add_argument(TypeKind.TYPE_STRING)
            ...         .set_return_type(TypeKind.TYPE_INT64)
            ...         .build()
            ... )
        """
        self._function.signature.append(signature)
        return self
    
    def build(self) -> Function:
        """Build and return the Function ProtoModel.
        
        Returns:
            Function ProtoModel ready for use with SimpleCatalog
        """
        return self._function


class SignatureBuilder:
    """Builder for FunctionSignature ProtoModel objects.
    
    Provides method chaining for constructing function signatures with
    typed arguments and return types.
    
    Examples:
        >>> # Simple signature: (STRING) -> INT64
        >>> sig = (SignatureBuilder()
        ...     .add_argument(TypeKind.TYPE_STRING)
        ...     .set_return_type(TypeKind.TYPE_INT64)
        ...     .build())
        >>> 
        >>> # Multiple arguments: (INT64, DOUBLE) -> DOUBLE
        >>> sig = (SignatureBuilder()
        ...     .add_argument(TypeKind.TYPE_INT64)
        ...     .add_argument(TypeKind.TYPE_DOUBLE)
        ...     .set_return_type(TypeKind.TYPE_DOUBLE)
        ...     .build())
        >>> 
        >>> # Optional argument: (STRING, STRING?) -> STRING
        >>> sig = (SignatureBuilder()
        ...     .add_argument(TypeKind.TYPE_STRING, FunctionEnums.ArgumentCardinality.REQUIRED)
        ...     .add_argument(TypeKind.TYPE_STRING, FunctionEnums.ArgumentCardinality.OPTIONAL)
        ...     .set_return_type(TypeKind.TYPE_STRING)
        ...     .build())
        >>> 
        >>> # Variadic: (INT64, INT64...) -> INT64
        >>> sig = (SignatureBuilder()
        ...     .add_argument(TypeKind.TYPE_INT64)
        ...     .add_argument(TypeKind.TYPE_INT64, FunctionEnums.ArgumentCardinality.REPEATED)
        ...     .set_return_type(TypeKind.TYPE_INT64)
        ...     .build())
    """
    
    def __init__(self):
        """Initialize SignatureBuilder."""
        self._signature = FunctionSignature(
            argument=[],
            return_type=None
        )
    
    def add_argument(
        self, 
        type_or_kind: Union[Type, TypeKind, int],
        cardinality: FunctionEnums.ArgumentCardinality = FunctionEnums.ArgumentCardinality.REQUIRED
    ) -> Self:
        """Add an argument to the signature.
        
        Args:
            type_or_kind: Type object or TypeKind enum value
            cardinality: REQUIRED (default), OPTIONAL, or REPEATED
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> # Required argument
            >>> builder.add_argument(TypeKind.TYPE_STRING)
            >>> 
            >>> # Optional argument
            >>> builder.add_argument(
            ...     TypeKind.TYPE_INT64, 
            ...     FunctionEnums.ArgumentCardinality.OPTIONAL
            ... )
            >>> 
            >>> # Repeated (variadic) argument
            >>> builder.add_argument(
            ...     TypeKind.TYPE_DOUBLE,
            ...     FunctionEnums.ArgumentCardinality.REPEATED
            ... )
        """
        # Convert TypeKind to Type if needed (following TableBuilder pattern)
        if isinstance(type_or_kind, (TypeKind, int)):
            arg_type = TypeFactory.create_simple_type(type_or_kind)
        else:
            arg_type = type_or_kind
        
        # Create FunctionArgumentType with options
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_FIXED,
            type=arg_type,
            options=FunctionArgumentTypeOptions(
                cardinality=cardinality
            )
        )
        
        self._signature.argument.append(arg)
        return self
    
    def set_return_type(self, type_or_kind: Union[Type, TypeKind, int]) -> Self:
        """Set the return type of the signature.
        
        Args:
            type_or_kind: Type object or TypeKind enum value
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> builder.set_return_type(TypeKind.TYPE_STRING)
            >>> # or
            >>> builder.set_return_type(TypeFactory.create_array_type(...))
        """
        # Convert TypeKind to Type if needed
        if isinstance(type_or_kind, (TypeKind, int)):
            ret_type = TypeFactory.create_simple_type(type_or_kind)
        else:
            ret_type = type_or_kind
        
        self._signature.return_type = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_FIXED,
            type=ret_type
        )
        return self
    
    def build(self) -> FunctionSignature:
        """Build and return the FunctionSignature ProtoModel.
        
        Returns:
            FunctionSignature ready to be added to Function
        """
        return self._signature
