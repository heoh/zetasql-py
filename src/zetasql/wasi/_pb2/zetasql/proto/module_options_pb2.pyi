from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerModuleOptions(_message.Message):
    __slots__ = ("udf_server_address", "udf_namespace", "udf_server_import_mode", "udf_scaling_factor")
    class UdfServerImportMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[PerModuleOptions.UdfServerImportMode]
        SERVER_ADDRESS_FROM_MODULE: _ClassVar[PerModuleOptions.UdfServerImportMode]
        CALLER_PROVIDED: _ClassVar[PerModuleOptions.UdfServerImportMode]
        MANUAL: _ClassVar[PerModuleOptions.UdfServerImportMode]
    UNKNOWN: PerModuleOptions.UdfServerImportMode
    SERVER_ADDRESS_FROM_MODULE: PerModuleOptions.UdfServerImportMode
    CALLER_PROVIDED: PerModuleOptions.UdfServerImportMode
    MANUAL: PerModuleOptions.UdfServerImportMode
    UDF_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UDF_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    UDF_SERVER_IMPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    UDF_SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    udf_server_address: str
    udf_namespace: str
    udf_server_import_mode: PerModuleOptions.UdfServerImportMode
    udf_scaling_factor: float
    def __init__(self, udf_server_address: _Optional[str] = ..., udf_namespace: _Optional[str] = ..., udf_server_import_mode: _Optional[_Union[PerModuleOptions.UdfServerImportMode, str]] = ..., udf_scaling_factor: _Optional[float] = ...) -> None: ...

class ModuleOptions(_message.Message):
    __slots__ = ("global_options", "per_module_options")
    class PerModuleOptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PerModuleOptions
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PerModuleOptions, _Mapping]] = ...) -> None: ...
    GLOBAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PER_MODULE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    global_options: PerModuleOptions
    per_module_options: _containers.MessageMap[str, PerModuleOptions]
    def __init__(self, global_options: _Optional[_Union[PerModuleOptions, _Mapping]] = ..., per_module_options: _Optional[_Mapping[str, PerModuleOptions]] = ...) -> None: ...
