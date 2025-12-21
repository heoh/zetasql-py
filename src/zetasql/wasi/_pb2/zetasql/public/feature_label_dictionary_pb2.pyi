from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureLabelDictionaryProto(_message.Message):
    __slots__ = ("label_mapping", "encoded_labels")
    class LabelMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelSet(_message.Message):
        __slots__ = ("label",)
        LABEL_FIELD_NUMBER: _ClassVar[int]
        label: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, label: _Optional[_Iterable[int]] = ...) -> None: ...
    class EncodedLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FeatureLabelDictionaryProto.LabelSet
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FeatureLabelDictionaryProto.LabelSet, _Mapping]] = ...) -> None: ...
    LABEL_MAPPING_FIELD_NUMBER: _ClassVar[int]
    ENCODED_LABELS_FIELD_NUMBER: _ClassVar[int]
    label_mapping: _containers.ScalarMap[int, str]
    encoded_labels: _containers.MessageMap[int, FeatureLabelDictionaryProto.LabelSet]
    def __init__(self, label_mapping: _Optional[_Mapping[int, str]] = ..., encoded_labels: _Optional[_Mapping[int, FeatureLabelDictionaryProto.LabelSet]] = ...) -> None: ...
