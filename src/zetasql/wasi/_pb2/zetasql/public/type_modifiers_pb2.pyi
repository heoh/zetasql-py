from zetasql.wasi._pb2.zetasql.public import collation_pb2 as _collation_pb2
from zetasql.wasi._pb2.zetasql.public import type_parameters_pb2 as _type_parameters_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypeModifiersProto(_message.Message):
    __slots__ = ("type_parameters", "collation")
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    type_parameters: _type_parameters_pb2.TypeParametersProto
    collation: _collation_pb2.CollationProto
    def __init__(self, type_parameters: _Optional[_Union[_type_parameters_pb2.TypeParametersProto, _Mapping]] = ..., collation: _Optional[_Union[_collation_pb2.CollationProto, _Mapping]] = ...) -> None: ...
