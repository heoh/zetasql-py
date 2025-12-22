from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_enums_pb2 as _resolved_ast_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StateMachineProto(_message.Message):
    __slots__ = ("nfa", "after_match_skip_mode", "longest_match_mode")
    class CompiledNFAProto(_message.Message):
        __slots__ = ("states", "start_state", "final_state", "num_pattern_variables")
        class EdgeProto(_message.Message):
            __slots__ = ("to_state", "pattern_variable", "is_head_anchored", "is_tail_anchored")
            TO_STATE_FIELD_NUMBER: _ClassVar[int]
            PATTERN_VARIABLE_FIELD_NUMBER: _ClassVar[int]
            IS_HEAD_ANCHORED_FIELD_NUMBER: _ClassVar[int]
            IS_TAIL_ANCHORED_FIELD_NUMBER: _ClassVar[int]
            to_state: int
            pattern_variable: int
            is_head_anchored: bool
            is_tail_anchored: bool
            def __init__(self, to_state: _Optional[int] = ..., pattern_variable: _Optional[int] = ..., is_head_anchored: bool = ..., is_tail_anchored: bool = ...) -> None: ...
        class StateProto(_message.Message):
            __slots__ = ("edges",)
            EDGES_FIELD_NUMBER: _ClassVar[int]
            edges: _containers.RepeatedCompositeFieldContainer[StateMachineProto.CompiledNFAProto.EdgeProto]
            def __init__(self, edges: _Optional[_Iterable[_Union[StateMachineProto.CompiledNFAProto.EdgeProto, _Mapping]]] = ...) -> None: ...
        STATES_FIELD_NUMBER: _ClassVar[int]
        START_STATE_FIELD_NUMBER: _ClassVar[int]
        FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
        NUM_PATTERN_VARIABLES_FIELD_NUMBER: _ClassVar[int]
        states: _containers.RepeatedCompositeFieldContainer[StateMachineProto.CompiledNFAProto.StateProto]
        start_state: int
        final_state: int
        num_pattern_variables: int
        def __init__(self, states: _Optional[_Iterable[_Union[StateMachineProto.CompiledNFAProto.StateProto, _Mapping]]] = ..., start_state: _Optional[int] = ..., final_state: _Optional[int] = ..., num_pattern_variables: _Optional[int] = ...) -> None: ...
    NFA_FIELD_NUMBER: _ClassVar[int]
    AFTER_MATCH_SKIP_MODE_FIELD_NUMBER: _ClassVar[int]
    LONGEST_MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    nfa: StateMachineProto.CompiledNFAProto
    after_match_skip_mode: _resolved_ast_enums_pb2.ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode
    longest_match_mode: bool
    def __init__(self, nfa: _Optional[_Union[StateMachineProto.CompiledNFAProto, _Mapping]] = ..., after_match_skip_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode, str]] = ..., longest_match_mode: bool = ...) -> None: ...

class CompiledPatternProto(_message.Message):
    __slots__ = ("state_machine",)
    STATE_MACHINE_FIELD_NUMBER: _ClassVar[int]
    state_machine: StateMachineProto
    def __init__(self, state_machine: _Optional[_Union[StateMachineProto, _Mapping]] = ...) -> None: ...
