from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConstnessLevelProto(_message.Message):
    __slots__ = ()
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSTNESS_UNSPECIFIED: _ClassVar[ConstnessLevelProto.Level]
        FOREVER_CONST: _ClassVar[ConstnessLevelProto.Level]
        ANALYSIS_CONST: _ClassVar[ConstnessLevelProto.Level]
        LEGACY_LITERAL_OR_PARAMETER: _ClassVar[ConstnessLevelProto.Level]
        LEGACY_CONSTANT_EXPRESSION: _ClassVar[ConstnessLevelProto.Level]
    CONSTNESS_UNSPECIFIED: ConstnessLevelProto.Level
    FOREVER_CONST: ConstnessLevelProto.Level
    ANALYSIS_CONST: ConstnessLevelProto.Level
    LEGACY_LITERAL_OR_PARAMETER: ConstnessLevelProto.Level
    LEGACY_CONSTANT_EXPRESSION: ConstnessLevelProto.Level
    def __init__(self) -> None: ...
