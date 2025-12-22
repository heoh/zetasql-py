from zetasql.wasi._pb2.zetasql.compliance import known_error_pb2 as _known_error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComplianceTestsLabels(_message.Message):
    __slots__ = ("test_cases",)
    TEST_CASES_FIELD_NUMBER: _ClassVar[int]
    test_cases: _containers.RepeatedCompositeFieldContainer[ComplianceTestCaseLabels]
    def __init__(self, test_cases: _Optional[_Iterable[_Union[ComplianceTestCaseLabels, _Mapping]]] = ...) -> None: ...

class ComplianceTestCaseLabels(_message.Message):
    __slots__ = ("test_name", "test_query", "param", "test_error_mode", "compliance_labels", "test_shard", "test_location")
    class Param(_message.Message):
        __slots__ = ("param_name", "param_value_literal")
        PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
        PARAM_VALUE_LITERAL_FIELD_NUMBER: _ClassVar[int]
        param_name: str
        param_value_literal: str
        def __init__(self, param_name: _Optional[str] = ..., param_value_literal: _Optional[str] = ...) -> None: ...
    class Location(_message.Message):
        __slots__ = ("file", "line")
        FILE_FIELD_NUMBER: _ClassVar[int]
        LINE_FIELD_NUMBER: _ClassVar[int]
        file: str
        line: int
        def __init__(self, file: _Optional[str] = ..., line: _Optional[int] = ...) -> None: ...
    TEST_NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    TEST_ERROR_MODE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    TEST_SHARD_FIELD_NUMBER: _ClassVar[int]
    TEST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    test_name: str
    test_query: str
    param: _containers.RepeatedCompositeFieldContainer[ComplianceTestCaseLabels.Param]
    test_error_mode: _known_error_pb2.KnownErrorMode
    compliance_labels: _containers.RepeatedScalarFieldContainer[str]
    test_shard: int
    test_location: ComplianceTestCaseLabels.Location
    def __init__(self, test_name: _Optional[str] = ..., test_query: _Optional[str] = ..., param: _Optional[_Iterable[_Union[ComplianceTestCaseLabels.Param, _Mapping]]] = ..., test_error_mode: _Optional[_Union[_known_error_pb2.KnownErrorMode, str]] = ..., compliance_labels: _Optional[_Iterable[str]] = ..., test_shard: _Optional[int] = ..., test_location: _Optional[_Union[ComplianceTestCaseLabels.Location, _Mapping]] = ...) -> None: ...
