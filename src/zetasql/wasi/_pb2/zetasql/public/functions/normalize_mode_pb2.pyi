from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NormalizeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NFC: _ClassVar[NormalizeMode]
    NFKC: _ClassVar[NormalizeMode]
    NFD: _ClassVar[NormalizeMode]
    NFKD: _ClassVar[NormalizeMode]
NFC: NormalizeMode
NFKC: NormalizeMode
NFD: NormalizeMode
NFKD: NormalizeMode
