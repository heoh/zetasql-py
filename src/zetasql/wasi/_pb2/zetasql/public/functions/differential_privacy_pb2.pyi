from zetasql.wasi._pb2.zetasql.proto import anon_output_with_report_pb2 as _anon_output_with_report_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DifferentialPrivacyEnums(_message.Message):
    __slots__ = ()
    class ReportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIFFERENTIAL_PRIVACY_REPORT_FORMAT_INVALID: _ClassVar[DifferentialPrivacyEnums.ReportFormat]
        JSON: _ClassVar[DifferentialPrivacyEnums.ReportFormat]
        PROTO: _ClassVar[DifferentialPrivacyEnums.ReportFormat]
    DIFFERENTIAL_PRIVACY_REPORT_FORMAT_INVALID: DifferentialPrivacyEnums.ReportFormat
    JSON: DifferentialPrivacyEnums.ReportFormat
    PROTO: DifferentialPrivacyEnums.ReportFormat
    class GroupSelectionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIFFERENTIAL_PRIVACY_GROUP_SELECTION_STRATEGY_INVALID: _ClassVar[DifferentialPrivacyEnums.GroupSelectionStrategy]
        LAPLACE_THRESHOLD: _ClassVar[DifferentialPrivacyEnums.GroupSelectionStrategy]
        PUBLIC_GROUPS: _ClassVar[DifferentialPrivacyEnums.GroupSelectionStrategy]
    DIFFERENTIAL_PRIVACY_GROUP_SELECTION_STRATEGY_INVALID: DifferentialPrivacyEnums.GroupSelectionStrategy
    LAPLACE_THRESHOLD: DifferentialPrivacyEnums.GroupSelectionStrategy
    PUBLIC_GROUPS: DifferentialPrivacyEnums.GroupSelectionStrategy
    class CountDistinctContributionBoundingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIFFERENTIAL_PRIVACY_COUNT_DISTINCT_CONTRIBUTION_BOUNDING_STRATEGY_INVALID: _ClassVar[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy]
        AUTO: _ClassVar[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy]
        SAMPLING: _ClassVar[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy]
        GREEDY: _ClassVar[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy]
        MATCHING: _ClassVar[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy]
    DIFFERENTIAL_PRIVACY_COUNT_DISTINCT_CONTRIBUTION_BOUNDING_STRATEGY_INVALID: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    AUTO: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    SAMPLING: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    GREEDY: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    MATCHING: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    def __init__(self) -> None: ...

class DifferentialPrivacyOutputWithReport(_message.Message):
    __slots__ = ("value", "values", "bounding_report", "count_distinct_bounding_report")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_REPORT_FIELD_NUMBER: _ClassVar[int]
    COUNT_DISTINCT_BOUNDING_REPORT_FIELD_NUMBER: _ClassVar[int]
    value: DifferentialPrivacyOutputValue
    values: DifferentialPrivacyOutputValues
    bounding_report: DifferentialPrivacyBoundingReport
    count_distinct_bounding_report: DifferentiallyPrivateCountDistinctBoundingReport
    def __init__(self, value: _Optional[_Union[DifferentialPrivacyOutputValue, _Mapping]] = ..., values: _Optional[_Union[DifferentialPrivacyOutputValues, _Mapping]] = ..., bounding_report: _Optional[_Union[DifferentialPrivacyBoundingReport, _Mapping]] = ..., count_distinct_bounding_report: _Optional[_Union[DifferentiallyPrivateCountDistinctBoundingReport, _Mapping]] = ...) -> None: ...

class DifferentialPrivacyBoundingReport(_message.Message):
    __slots__ = ("lower_bound", "upper_bound", "num_inputs", "num_outside")
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    NUM_OUTSIDE_FIELD_NUMBER: _ClassVar[int]
    lower_bound: DifferentialPrivacyOutputValue
    upper_bound: DifferentialPrivacyOutputValue
    num_inputs: float
    num_outside: float
    def __init__(self, lower_bound: _Optional[_Union[DifferentialPrivacyOutputValue, _Mapping]] = ..., upper_bound: _Optional[_Union[DifferentialPrivacyOutputValue, _Mapping]] = ..., num_inputs: _Optional[float] = ..., num_outside: _Optional[float] = ...) -> None: ...

class DifferentiallyPrivateCountDistinctBoundingReport(_message.Message):
    __slots__ = ("contribution_bounding_strategy", "upper_bound", "num_inputs")
    CONTRIBUTION_BOUNDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    contribution_bounding_strategy: DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy
    upper_bound: int
    num_inputs: float
    def __init__(self, contribution_bounding_strategy: _Optional[_Union[DifferentialPrivacyEnums.CountDistinctContributionBoundingStrategy, str]] = ..., upper_bound: _Optional[int] = ..., num_inputs: _Optional[float] = ...) -> None: ...

class DifferentialPrivacyOutputValues(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[DifferentialPrivacyOutputValue]
    def __init__(self, values: _Optional[_Iterable[_Union[DifferentialPrivacyOutputValue, _Mapping]]] = ...) -> None: ...

class DifferentialPrivacyOutputValue(_message.Message):
    __slots__ = ("int_value", "float_value", "string_value", "noise_confidence_interval")
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    NOISE_CONFIDENCE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    float_value: float
    string_value: str
    noise_confidence_interval: _anon_output_with_report_pb2.NoiseConfidenceInterval
    def __init__(self, int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., noise_confidence_interval: _Optional[_Union[_anon_output_with_report_pb2.NoiseConfidenceInterval, _Mapping]] = ...) -> None: ...
