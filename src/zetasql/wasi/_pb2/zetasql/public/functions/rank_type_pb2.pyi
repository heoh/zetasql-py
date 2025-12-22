from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RankTypeEnums(_message.Message):
    __slots__ = ()
    class RankType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANK_TYPE_UNKNOWN: _ClassVar[RankTypeEnums.RankType]
        FRACTION_LESS_THAN_OR_EQUAL: _ClassVar[RankTypeEnums.RankType]
        MIDPOINT: _ClassVar[RankTypeEnums.RankType]
        FRACTION_LESS_THAN: _ClassVar[RankTypeEnums.RankType]
    RANK_TYPE_UNKNOWN: RankTypeEnums.RankType
    FRACTION_LESS_THAN_OR_EQUAL: RankTypeEnums.RankType
    MIDPOINT: RankTypeEnums.RankType
    FRACTION_LESS_THAN: RankTypeEnums.RankType
    def __init__(self) -> None: ...
