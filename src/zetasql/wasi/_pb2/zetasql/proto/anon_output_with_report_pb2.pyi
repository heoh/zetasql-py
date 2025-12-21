from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnonOutputWithReport(_message.Message):
    __slots__ = ("value", "values", "bounding_report")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_REPORT_FIELD_NUMBER: _ClassVar[int]
    value: AnonOutputValue
    values: AnonOutputValues
    bounding_report: BoundingReport
    def __init__(self, value: _Optional[_Union[AnonOutputValue, _Mapping]] = ..., values: _Optional[_Union[AnonOutputValues, _Mapping]] = ..., bounding_report: _Optional[_Union[BoundingReport, _Mapping]] = ...) -> None: ...

class BoundingReport(_message.Message):
    __slots__ = ("lower_bound", "upper_bound", "num_inputs", "num_outside")
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    NUM_OUTSIDE_FIELD_NUMBER: _ClassVar[int]
    lower_bound: AnonOutputValue
    upper_bound: AnonOutputValue
    num_inputs: float
    num_outside: float
    def __init__(self, lower_bound: _Optional[_Union[AnonOutputValue, _Mapping]] = ..., upper_bound: _Optional[_Union[AnonOutputValue, _Mapping]] = ..., num_inputs: _Optional[float] = ..., num_outside: _Optional[float] = ...) -> None: ...

class NoiseConfidenceInterval(_message.Message):
    __slots__ = ("lower_bound", "upper_bound", "confidence_level")
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    lower_bound: float
    upper_bound: float
    confidence_level: float
    def __init__(self, lower_bound: _Optional[float] = ..., upper_bound: _Optional[float] = ..., confidence_level: _Optional[float] = ...) -> None: ...

class AnonOutputValues(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[AnonOutputValue]
    def __init__(self, values: _Optional[_Iterable[_Union[AnonOutputValue, _Mapping]]] = ...) -> None: ...

class AnonOutputValue(_message.Message):
    __slots__ = ("int_value", "float_value", "string_value", "noise_confidence_interval")
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    NOISE_CONFIDENCE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    float_value: float
    string_value: str
    noise_confidence_interval: NoiseConfidenceInterval
    def __init__(self, int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., noise_confidence_interval: _Optional[_Union[NoiseConfidenceInterval, _Mapping]] = ...) -> None: ...
