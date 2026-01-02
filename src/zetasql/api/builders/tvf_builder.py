"""
TVFBuilder - Fluent API for building TableValuedFunction ProtoModel objects

This module provides a Java-style builder pattern for constructing table-valued functions (TVFs),
making custom TVF creation much cleaner than manual protobuf manipulation.

Examples:
    >>> from zetasql.api.builders import TVFBuilder
    >>> from zetasql.types import TypeKind
    >>> 
    >>> # Simple TVF with scalar arguments and fixed output schema
    >>> my_tvf = (TVFBuilder("generate_series")
    ...     .add_argument("start", TypeKind.TYPE_INT64)
    ...     .add_argument("end", TypeKind.TYPE_INT64)
    ...     .set_output_schema([
    ...         ("value", TypeKind.TYPE_INT64),
    ...     ])
    ...     .build())
    >>> 
    >>> # TVF that accepts a TABLE argument
    >>> filter_tvf = (TVFBuilder("filter_table")
    ...     .add_table_argument("input_table")
    ...     .add_argument("filter_value", TypeKind.TYPE_INT64)
    ...     .set_forward_input_schema()  # Output matches input schema
    ...     .build())
    >>> 
    >>> # TVF with TABLE input plus additional columns
    >>> enriched_tvf = (TVFBuilder("enrich_table")
    ...     .add_table_argument("input_table")
    ...     .set_forward_input_schema_with_appended_columns([
    ...         ("enriched_col", TypeKind.TYPE_STRING),
    ...     ])
    ...     .build())
"""

from typing import Union, List, Tuple
from typing_extensions import Self
from zetasql.types import (
    TableValuedFunction,
    FunctionSignature,
    FunctionArgumentType,
    FunctionArgumentTypeOptions,
    TVFRelation,
    TVFRelationColumn,
    Type,
    TypeKind,
    TypeFactory
)
from zetasql.core.types.proto_models import (
    FunctionEnums,
    SignatureArgumentKind,
)


class TVFBuilder:
    """Builder for TableValuedFunction ProtoModel objects.
    
    Provides method chaining for fluent TVF construction. The builder
    creates ProtoModel objects that can be used directly with SimpleCatalog.
    
    Args:
        name: TVF name
    
    Examples:
        >>> # Fixed output schema TVF
        >>> tvf = (TVFBuilder("my_tvf")
        ...     .add_argument("param1", TypeKind.TYPE_INT64)
        ...     .set_output_schema([
        ...         ("col1", TypeKind.TYPE_STRING),
        ...         ("col2", TypeKind.TYPE_INT64),
        ...     ])
        ...     .build())
        >>> 
        >>> # Pass-through TVF (output matches input)
        >>> tvf = (TVFBuilder("pass_through")
        ...     .add_table_argument("input_table")
        ...     .set_forward_input_schema()
        ...     .build())
    """
    
    def __init__(self, name: str):
        """Initialize TVFBuilder.
        
        Args:
            name: TVF name. Can be simple ("my_tvf") or qualified ("pkg.my_tvf")
        """
        # Split name into name_path (following Function pattern)
        name_path = name.split('.') if '.' in name else [name]
        
        self._tvf = TableValuedFunction(
            name_path=name_path,
            signature=FunctionSignature(
                argument=[],
                return_type=None
            )
        )
        
        # Track TVF type for proper construction
        self._tvf_type = None
        self._output_columns = []
    
    def add_argument(
        self, 
        name: str,
        type_or_kind: Union[Type, TypeKind, int],
        cardinality: FunctionEnums.ArgumentCardinality = FunctionEnums.ArgumentCardinality.REQUIRED
    ) -> Self:
        """Add a scalar argument to the TVF.
        
        Args:
            name: Argument name
            type_or_kind: Type object or TypeKind enum value
            cardinality: REQUIRED (default), OPTIONAL, or REPEATED
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> builder.add_argument("filter_value", TypeKind.TYPE_INT64)
            >>> builder.add_argument("optional_param", TypeKind.TYPE_STRING, 
            ...     FunctionEnums.ArgumentCardinality.OPTIONAL)
        """
        # Convert TypeKind to Type if needed
        if isinstance(type_or_kind, (TypeKind, int)):
            arg_type = TypeFactory.create_simple_type(type_or_kind)
        else:
            arg_type = type_or_kind
        
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_FIXED,
            type=arg_type,
            options=FunctionArgumentTypeOptions(
                cardinality=cardinality,
                argument_name=name  # Store argument name
            )
        )
        
        self._tvf.signature.argument.append(arg)
        return self
    
    def add_table_argument(self, name: str) -> Self:
        """Add a TABLE argument to the TVF.
        
        This creates an argument that accepts a table as input.
        
        Args:
            name: Argument name (e.g., "input_table")
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> builder.add_table_argument("input_table")
        """
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_RELATION,  # Indicates TABLE argument
            options=FunctionArgumentTypeOptions(
                argument_name=name
            )
        )
        
        self._tvf.signature.argument.append(arg)
        return self
    
    def set_output_schema(
        self, 
        columns: List[Tuple[str, Union[Type, TypeKind, int]]]
    ) -> Self:
        """Set fixed output schema for the TVF.
        
        This creates a FIXED_OUTPUT_SCHEMA_TVF type.
        
        Args:
            columns: List of (column_name, type_or_kind) tuples
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> builder.set_output_schema([
            ...     ("col1", TypeKind.TYPE_STRING),
            ...     ("col2", TypeKind.TYPE_INT64),
            ...     ("col3", TypeKind.TYPE_DOUBLE),
            ... ])
        """
        self._tvf_type = FunctionEnums.TableValuedFunctionType.FIXED_OUTPUT_SCHEMA_TVF
        self._output_columns = []
        
        for col_name, type_or_kind in columns:
            # Convert TypeKind to Type if needed
            if isinstance(type_or_kind, (TypeKind, int)):
                col_type = TypeFactory.create_simple_type(type_or_kind)
            else:
                col_type = type_or_kind
            
            self._output_columns.append(
                TVFRelationColumn(
                    name=col_name,
                    type=col_type
                )
            )
        
        return self
    
    def set_forward_input_schema(self) -> Self:
        """Set TVF to forward input schema to output (pass-through).
        
        This creates a FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF type.
        The output schema will match the input table's schema.
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> # TVF that passes through input table unchanged
            >>> builder.add_table_argument("input_table")
            >>> builder.set_forward_input_schema()
        """
        self._tvf_type = FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF
        return self
    
    def set_forward_input_schema_with_appended_columns(
        self,
        appended_columns: List[Tuple[str, Union[Type, TypeKind, int]]]
    ) -> Self:
        """Set TVF to forward input schema plus additional columns.
        
        This creates a FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS type.
        The output schema will be input columns + appended columns.
        
        Args:
            appended_columns: List of (column_name, type_or_kind) tuples to append
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> # TVF that adds enrichment columns to input table
            >>> builder.add_table_argument("input_table")
            >>> builder.set_forward_input_schema_with_appended_columns([
            ...     ("enriched_data", TypeKind.TYPE_STRING),
            ...     ("score", TypeKind.TYPE_DOUBLE),
            ... ])
        """
        self._tvf_type = FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS
        self._output_columns = []
        
        for col_name, type_or_kind in appended_columns:
            # Convert TypeKind to Type if needed
            if isinstance(type_or_kind, (TypeKind, int)):
                col_type = TypeFactory.create_simple_type(type_or_kind)
            else:
                col_type = type_or_kind
            
            self._output_columns.append(
                TVFRelationColumn(
                    name=col_name,
                    type=col_type
                )
            )
        
        return self
    
    def build(self) -> TableValuedFunction:
        """Build and return the TableValuedFunction ProtoModel.
        
        Returns:
            TableValuedFunction ProtoModel ready for use with SimpleCatalog
        """
        # Set TVF type
        if self._tvf_type is not None:
            self._tvf.type = self._tvf_type
        
        # Set output schema if columns were specified
        if self._output_columns:
            # Create TVFRelation for output schema
            output_relation = TVFRelation(
                column=self._output_columns,
                is_value_table=False
            )
            
            # Store in signature's return_type using ARG_TYPE_RELATION
            self._tvf.signature.return_type = FunctionArgumentType(
                kind=SignatureArgumentKind.ARG_TYPE_RELATION,
                options=FunctionArgumentTypeOptions(
                    relation_input_schema=output_relation
                )
            )
        
        return self._tvf
