from google.protobuf import any_pb2 as _any_pb2
from zetasql.wasi._pb2.zetasql.proto import function_pb2 as _function_pb2
from zetasql.wasi._pb2.zetasql.proto import script_exception_pb2 as _script_exception_pb2
from zetasql.wasi._pb2.zetasql.scripting import procedure_extension_pb2 as _procedure_extension_pb2
from zetasql.wasi._pb2.zetasql.scripting import variable_pb2 as _variable_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptExecutorStateProto(_message.Message):
    __slots__ = ("callstack", "pending_exceptions", "triggered_features", "timezone", "case_stmt_true_branch_index", "case_stmt_current_branch_index", "sql_feature_usage")
    class ScriptFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[ScriptExecutorStateProto.ScriptFeature]
        EXCEPTION_CAUGHT: _ClassVar[ScriptExecutorStateProto.ScriptFeature]
        CALL_STATEMENT: _ClassVar[ScriptExecutorStateProto.ScriptFeature]
        EXECUTE_IMMEDIATE_STATEMENT: _ClassVar[ScriptExecutorStateProto.ScriptFeature]
    INVALID: ScriptExecutorStateProto.ScriptFeature
    EXCEPTION_CAUGHT: ScriptExecutorStateProto.ScriptFeature
    CALL_STATEMENT: ScriptExecutorStateProto.ScriptFeature
    EXECUTE_IMMEDIATE_STATEMENT: ScriptExecutorStateProto.ScriptFeature
    class ProcedureDefinition(_message.Message):
        __slots__ = ("name", "signature", "argument_name_list", "body", "is_dynamic_sql", "extension")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        ARGUMENT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        IS_DYNAMIC_SQL_FIELD_NUMBER: _ClassVar[int]
        EXTENSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        signature: _function_pb2.FunctionSignatureProto
        argument_name_list: _containers.RepeatedScalarFieldContainer[str]
        body: str
        is_dynamic_sql: bool
        extension: _procedure_extension_pb2.ProcedureExtension
        def __init__(self, name: _Optional[str] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., argument_name_list: _Optional[_Iterable[str]] = ..., body: _Optional[str] = ..., is_dynamic_sql: bool = ..., extension: _Optional[_Union[_procedure_extension_pb2.ProcedureExtension, _Mapping]] = ...) -> None: ...
    class StackFrame(_message.Message):
        __slots__ = ("procedure_definition", "variables", "current_location_byte_offset", "control_flow_node_kind", "parameters", "for_loop_stack")
        class Parameters(_message.Message):
            __slots__ = ("mode", "variables")
            class ParameterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NONE: _ClassVar[ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode]
                NAMED: _ClassVar[ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode]
                POSITIONAL: _ClassVar[ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode]
            NONE: ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode
            NAMED: ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode
            POSITIONAL: ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode
            MODE_FIELD_NUMBER: _ClassVar[int]
            VARIABLES_FIELD_NUMBER: _ClassVar[int]
            mode: ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode
            variables: _containers.RepeatedCompositeFieldContainer[_variable_pb2.Variable]
            def __init__(self, mode: _Optional[_Union[ScriptExecutorStateProto.StackFrame.Parameters.ParameterMode, str]] = ..., variables: _Optional[_Iterable[_Union[_variable_pb2.Variable, _Mapping]]] = ...) -> None: ...
        PROCEDURE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        VARIABLES_FIELD_NUMBER: _ClassVar[int]
        CURRENT_LOCATION_BYTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CONTROL_FLOW_NODE_KIND_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        FOR_LOOP_STACK_FIELD_NUMBER: _ClassVar[int]
        procedure_definition: ScriptExecutorStateProto.ProcedureDefinition
        variables: _containers.RepeatedCompositeFieldContainer[_variable_pb2.Variable]
        current_location_byte_offset: int
        control_flow_node_kind: int
        parameters: ScriptExecutorStateProto.StackFrame.Parameters
        for_loop_stack: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
        def __init__(self, procedure_definition: _Optional[_Union[ScriptExecutorStateProto.ProcedureDefinition, _Mapping]] = ..., variables: _Optional[_Iterable[_Union[_variable_pb2.Variable, _Mapping]]] = ..., current_location_byte_offset: _Optional[int] = ..., control_flow_node_kind: _Optional[int] = ..., parameters: _Optional[_Union[ScriptExecutorStateProto.StackFrame.Parameters, _Mapping]] = ..., for_loop_stack: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
    class ScriptFeatureUsage(_message.Message):
        __slots__ = ("exception", "call_stmt", "execute_immediate_stmt")
        EXCEPTION_FIELD_NUMBER: _ClassVar[int]
        CALL_STMT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_IMMEDIATE_STMT_FIELD_NUMBER: _ClassVar[int]
        exception: int
        call_stmt: int
        execute_immediate_stmt: int
        def __init__(self, exception: _Optional[int] = ..., call_stmt: _Optional[int] = ..., execute_immediate_stmt: _Optional[int] = ...) -> None: ...
    CALLSTACK_FIELD_NUMBER: _ClassVar[int]
    PENDING_EXCEPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    CASE_STMT_TRUE_BRANCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    CASE_STMT_CURRENT_BRANCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    SQL_FEATURE_USAGE_FIELD_NUMBER: _ClassVar[int]
    callstack: _containers.RepeatedCompositeFieldContainer[ScriptExecutorStateProto.StackFrame]
    pending_exceptions: _containers.RepeatedCompositeFieldContainer[_script_exception_pb2.ScriptException]
    triggered_features: _containers.RepeatedScalarFieldContainer[ScriptExecutorStateProto.ScriptFeature]
    timezone: str
    case_stmt_true_branch_index: int
    case_stmt_current_branch_index: int
    sql_feature_usage: ScriptExecutorStateProto.ScriptFeatureUsage
    def __init__(self, callstack: _Optional[_Iterable[_Union[ScriptExecutorStateProto.StackFrame, _Mapping]]] = ..., pending_exceptions: _Optional[_Iterable[_Union[_script_exception_pb2.ScriptException, _Mapping]]] = ..., triggered_features: _Optional[_Iterable[_Union[ScriptExecutorStateProto.ScriptFeature, str]]] = ..., timezone: _Optional[str] = ..., case_stmt_true_branch_index: _Optional[int] = ..., case_stmt_current_branch_index: _Optional[int] = ..., sql_feature_usage: _Optional[_Union[ScriptExecutorStateProto.ScriptFeatureUsage, _Mapping]] = ...) -> None: ...
