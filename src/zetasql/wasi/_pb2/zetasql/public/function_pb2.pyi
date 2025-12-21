from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SignatureArgumentKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARG_TYPE_FIXED: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ANY_1: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ANY_2: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ANY_3: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ANY_4: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ANY_5: _ClassVar[SignatureArgumentKind]
    ARG_ARRAY_TYPE_ANY_1: _ClassVar[SignatureArgumentKind]
    ARG_ARRAY_TYPE_ANY_2: _ClassVar[SignatureArgumentKind]
    ARG_ARRAY_TYPE_ANY_3: _ClassVar[SignatureArgumentKind]
    ARG_ARRAY_TYPE_ANY_4: _ClassVar[SignatureArgumentKind]
    ARG_ARRAY_TYPE_ANY_5: _ClassVar[SignatureArgumentKind]
    ARG_PROTO_MAP_ANY: _ClassVar[SignatureArgumentKind]
    ARG_PROTO_MAP_KEY_ANY: _ClassVar[SignatureArgumentKind]
    ARG_PROTO_MAP_VALUE_ANY: _ClassVar[SignatureArgumentKind]
    ARG_PROTO_ANY: _ClassVar[SignatureArgumentKind]
    ARG_STRUCT_ANY: _ClassVar[SignatureArgumentKind]
    ARG_ENUM_ANY: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_ARBITRARY: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_RELATION: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_VOID: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_MODEL: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_CONNECTION: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_DESCRIPTOR: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_LAMBDA: _ClassVar[SignatureArgumentKind]
    ARG_RANGE_TYPE_ANY_1: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_GRAPH_NODE: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_GRAPH_EDGE: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_GRAPH_ELEMENT: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_GRAPH_PATH: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_GRAPH: _ClassVar[SignatureArgumentKind]
    ARG_TYPE_SEQUENCE: _ClassVar[SignatureArgumentKind]
    ARG_MEASURE_TYPE_ANY_1: _ClassVar[SignatureArgumentKind]
    ARG_MAP_TYPE_ANY_1_2: _ClassVar[SignatureArgumentKind]
    __SignatureArgumentKind__switch_must_have_a_default__: _ClassVar[SignatureArgumentKind]
ARG_TYPE_FIXED: SignatureArgumentKind
ARG_TYPE_ANY_1: SignatureArgumentKind
ARG_TYPE_ANY_2: SignatureArgumentKind
ARG_TYPE_ANY_3: SignatureArgumentKind
ARG_TYPE_ANY_4: SignatureArgumentKind
ARG_TYPE_ANY_5: SignatureArgumentKind
ARG_ARRAY_TYPE_ANY_1: SignatureArgumentKind
ARG_ARRAY_TYPE_ANY_2: SignatureArgumentKind
ARG_ARRAY_TYPE_ANY_3: SignatureArgumentKind
ARG_ARRAY_TYPE_ANY_4: SignatureArgumentKind
ARG_ARRAY_TYPE_ANY_5: SignatureArgumentKind
ARG_PROTO_MAP_ANY: SignatureArgumentKind
ARG_PROTO_MAP_KEY_ANY: SignatureArgumentKind
ARG_PROTO_MAP_VALUE_ANY: SignatureArgumentKind
ARG_PROTO_ANY: SignatureArgumentKind
ARG_STRUCT_ANY: SignatureArgumentKind
ARG_ENUM_ANY: SignatureArgumentKind
ARG_TYPE_ARBITRARY: SignatureArgumentKind
ARG_TYPE_RELATION: SignatureArgumentKind
ARG_TYPE_VOID: SignatureArgumentKind
ARG_TYPE_MODEL: SignatureArgumentKind
ARG_TYPE_CONNECTION: SignatureArgumentKind
ARG_TYPE_DESCRIPTOR: SignatureArgumentKind
ARG_TYPE_LAMBDA: SignatureArgumentKind
ARG_RANGE_TYPE_ANY_1: SignatureArgumentKind
ARG_TYPE_GRAPH_NODE: SignatureArgumentKind
ARG_TYPE_GRAPH_EDGE: SignatureArgumentKind
ARG_TYPE_GRAPH_ELEMENT: SignatureArgumentKind
ARG_TYPE_GRAPH_PATH: SignatureArgumentKind
ARG_TYPE_GRAPH: SignatureArgumentKind
ARG_TYPE_SEQUENCE: SignatureArgumentKind
ARG_MEASURE_TYPE_ANY_1: SignatureArgumentKind
ARG_MAP_TYPE_ANY_1_2: SignatureArgumentKind
__SignatureArgumentKind__switch_must_have_a_default__: SignatureArgumentKind

class FunctionEnums(_message.Message):
    __slots__ = ()
    class ArgumentCardinality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUIRED: _ClassVar[FunctionEnums.ArgumentCardinality]
        REPEATED: _ClassVar[FunctionEnums.ArgumentCardinality]
        OPTIONAL: _ClassVar[FunctionEnums.ArgumentCardinality]
    REQUIRED: FunctionEnums.ArgumentCardinality
    REPEATED: FunctionEnums.ArgumentCardinality
    OPTIONAL: FunctionEnums.ArgumentCardinality
    class ProcedureArgumentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[FunctionEnums.ProcedureArgumentMode]
        IN: _ClassVar[FunctionEnums.ProcedureArgumentMode]
        OUT: _ClassVar[FunctionEnums.ProcedureArgumentMode]
        INOUT: _ClassVar[FunctionEnums.ProcedureArgumentMode]
    NOT_SET: FunctionEnums.ProcedureArgumentMode
    IN: FunctionEnums.ProcedureArgumentMode
    OUT: FunctionEnums.ProcedureArgumentMode
    INOUT: FunctionEnums.ProcedureArgumentMode
    class WindowOrderSupport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_UNSUPPORTED: _ClassVar[FunctionEnums.WindowOrderSupport]
        ORDER_OPTIONAL: _ClassVar[FunctionEnums.WindowOrderSupport]
        ORDER_REQUIRED: _ClassVar[FunctionEnums.WindowOrderSupport]
    ORDER_UNSUPPORTED: FunctionEnums.WindowOrderSupport
    ORDER_OPTIONAL: FunctionEnums.WindowOrderSupport
    ORDER_REQUIRED: FunctionEnums.WindowOrderSupport
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCALAR: _ClassVar[FunctionEnums.Mode]
        AGGREGATE: _ClassVar[FunctionEnums.Mode]
        ANALYTIC: _ClassVar[FunctionEnums.Mode]
    SCALAR: FunctionEnums.Mode
    AGGREGATE: FunctionEnums.Mode
    ANALYTIC: FunctionEnums.Mode
    class Volatility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMMUTABLE: _ClassVar[FunctionEnums.Volatility]
        STABLE: _ClassVar[FunctionEnums.Volatility]
        VOLATILE: _ClassVar[FunctionEnums.Volatility]
    IMMUTABLE: FunctionEnums.Volatility
    STABLE: FunctionEnums.Volatility
    VOLATILE: FunctionEnums.Volatility
    class TableValuedFunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[FunctionEnums.TableValuedFunctionType]
        FIXED_OUTPUT_SCHEMA_TVF: _ClassVar[FunctionEnums.TableValuedFunctionType]
        FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF: _ClassVar[FunctionEnums.TableValuedFunctionType]
        TEMPLATED_SQL_TVF: _ClassVar[FunctionEnums.TableValuedFunctionType]
        FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS: _ClassVar[FunctionEnums.TableValuedFunctionType]
        BASIS_TVF: _ClassVar[FunctionEnums.TableValuedFunctionType]
    INVALID: FunctionEnums.TableValuedFunctionType
    FIXED_OUTPUT_SCHEMA_TVF: FunctionEnums.TableValuedFunctionType
    FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF: FunctionEnums.TableValuedFunctionType
    TEMPLATED_SQL_TVF: FunctionEnums.TableValuedFunctionType
    FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS: FunctionEnums.TableValuedFunctionType
    BASIS_TVF: FunctionEnums.TableValuedFunctionType
    class ArgumentCollationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AFFECTS_NONE: _ClassVar[FunctionEnums.ArgumentCollationMode]
        AFFECTS_OPERATION: _ClassVar[FunctionEnums.ArgumentCollationMode]
        AFFECTS_PROPAGATION: _ClassVar[FunctionEnums.ArgumentCollationMode]
        AFFECTS_OPERATION_AND_PROPAGATION: _ClassVar[FunctionEnums.ArgumentCollationMode]
    AFFECTS_NONE: FunctionEnums.ArgumentCollationMode
    AFFECTS_OPERATION: FunctionEnums.ArgumentCollationMode
    AFFECTS_PROPAGATION: FunctionEnums.ArgumentCollationMode
    AFFECTS_OPERATION_AND_PROPAGATION: FunctionEnums.ArgumentCollationMode
    class NamedArgumentKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAMED_ARGUMENT_KIND_UNSPECIFIED: _ClassVar[FunctionEnums.NamedArgumentKind]
        POSITIONAL_ONLY: _ClassVar[FunctionEnums.NamedArgumentKind]
        POSITIONAL_OR_NAMED: _ClassVar[FunctionEnums.NamedArgumentKind]
        NAMED_ONLY: _ClassVar[FunctionEnums.NamedArgumentKind]
    NAMED_ARGUMENT_KIND_UNSPECIFIED: FunctionEnums.NamedArgumentKind
    POSITIONAL_ONLY: FunctionEnums.NamedArgumentKind
    POSITIONAL_OR_NAMED: FunctionEnums.NamedArgumentKind
    NAMED_ONLY: FunctionEnums.NamedArgumentKind
    class ArgumentAliasKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARGUMENT_ALIAS_KIND_UNSPECIFIED: _ClassVar[FunctionEnums.ArgumentAliasKind]
        ARGUMENT_NON_ALIASED: _ClassVar[FunctionEnums.ArgumentAliasKind]
        ARGUMENT_ALIASED: _ClassVar[FunctionEnums.ArgumentAliasKind]
    ARGUMENT_ALIAS_KIND_UNSPECIFIED: FunctionEnums.ArgumentAliasKind
    ARGUMENT_NON_ALIASED: FunctionEnums.ArgumentAliasKind
    ARGUMENT_ALIASED: FunctionEnums.ArgumentAliasKind
    class DefaultNullHandling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_NULL_HANDLING_UNSPECIFIED: _ClassVar[FunctionEnums.DefaultNullHandling]
        DEFAULT_NULL_HANDLING_IGNORE_NULLS: _ClassVar[FunctionEnums.DefaultNullHandling]
        DEFAULT_NULL_HANDLING_RESPECT_NULLS: _ClassVar[FunctionEnums.DefaultNullHandling]
    DEFAULT_NULL_HANDLING_UNSPECIFIED: FunctionEnums.DefaultNullHandling
    DEFAULT_NULL_HANDLING_IGNORE_NULLS: FunctionEnums.DefaultNullHandling
    DEFAULT_NULL_HANDLING_RESPECT_NULLS: FunctionEnums.DefaultNullHandling
    def __init__(self) -> None: ...
