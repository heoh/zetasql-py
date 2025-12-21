from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleTokenListProto(_message.Message):
    __slots__ = ("text_token",)
    TEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    text_token: _containers.RepeatedCompositeFieldContainer[TextTokenProto]
    def __init__(self, text_token: _Optional[_Iterable[_Union[TextTokenProto, _Mapping]]] = ...) -> None: ...

class TextTokenProto(_message.Message):
    __slots__ = ("text", "attribute", "index_token")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    INDEX_TOKEN_FIELD_NUMBER: _ClassVar[int]
    text: str
    attribute: int
    index_token: _containers.RepeatedCompositeFieldContainer[TokenProto]
    def __init__(self, text: _Optional[str] = ..., attribute: _Optional[int] = ..., index_token: _Optional[_Iterable[_Union[TokenProto, _Mapping]]] = ...) -> None: ...

class TokenProto(_message.Message):
    __slots__ = ("text", "attribute")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    text: str
    attribute: int
    def __init__(self, text: _Optional[str] = ..., attribute: _Optional[int] = ...) -> None: ...
