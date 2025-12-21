from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceholderDescriptorProto(_message.Message):
    __slots__ = ("is_placeholder",)
    PLACEHOLDER_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    placeholder_descriptor: _descriptor.FieldDescriptor
    IS_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    is_placeholder: bool
    def __init__(self, is_placeholder: bool = ...) -> None: ...
