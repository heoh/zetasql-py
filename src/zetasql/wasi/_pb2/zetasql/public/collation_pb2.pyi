from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollationProto(_message.Message):
    __slots__ = ("collation_name", "child_list")
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CHILD_LIST_FIELD_NUMBER: _ClassVar[int]
    collation_name: str
    child_list: _containers.RepeatedCompositeFieldContainer[CollationProto]
    def __init__(self, collation_name: _Optional[str] = ..., child_list: _Optional[_Iterable[_Union[CollationProto, _Mapping]]] = ...) -> None: ...
