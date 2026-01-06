from typing import TypeVar

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message

from zetasql import types
from zetasql.core.func_utils import parameters
from zetasql.core.wasm_client import WasmClient
from zetasql.types import parse_proto
from zetasql.wasi import get_wasm_path
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2

Message = TypeVar("Message", bound=_message.Message)


class ZetaSqlLocalService:
    """Client for ZetaSQL Local Service via WASM.

    Uses ProtoModel objects for all API interactions. ProtoModel objects
    provide type-safe dataclass interfaces with automatic protobuf conversion.
    """

    def __init__(self):
        """Initialize the ZetaSQL Local Service client."""
        self.wasm_client = WasmClient(wasm_path=get_wasm_path())

    @parameters(types.PrepareRequest)
    def prepare(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_Prepare",
                types.PrepareRequest(*args, **kwargs).to_proto(),
                local_service_pb2.PrepareResponse,
            ),
        ).as_type(types.PrepareResponse)

    @parameters(types.EvaluateRequest)
    def evaluate(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_Evaluate",
                types.EvaluateRequest(*args, **kwargs).to_proto(),
                local_service_pb2.EvaluateResponse,
            ),
        ).as_type(types.EvaluateResponse)

    @parameters(types.UnprepareRequest)
    def unprepare(self, *args, **kwargs):
        parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_Unprepare",
                types.UnprepareRequest(*args, **kwargs).to_proto(),
                _empty_pb2.Empty,
            ),
        )

    @parameters(types.PrepareQueryRequest)
    def prepare_query(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_PrepareQuery",
                types.PrepareQueryRequest(*args, **kwargs).to_proto(),
                local_service_pb2.PrepareQueryResponse,
            ),
        ).as_type(types.PrepareQueryResponse)

    @parameters(types.EvaluateQueryRequest)
    def evaluate_query(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_EvaluateQuery",
                types.EvaluateQueryRequest(*args, **kwargs).to_proto(),
                local_service_pb2.EvaluateQueryResponse,
            ),
        ).as_type(types.EvaluateQueryResponse)

    @parameters(types.UnprepareQueryRequest)
    def unprepare_query(self, *args, **kwargs):
        parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_UnprepareQuery",
                types.UnprepareQueryRequest(*args, **kwargs).to_proto(),
                _empty_pb2.Empty,
            ),
        )

    @parameters(types.PrepareModifyRequest)
    def prepare_modify(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_PrepareModify",
                types.PrepareModifyRequest(*args, **kwargs).to_proto(),
                local_service_pb2.PrepareModifyResponse,
            ),
        ).as_type(types.PrepareModifyResponse)

    @parameters(types.EvaluateModifyRequest)
    def evaluate_modify(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_EvaluateModify",
                types.EvaluateModifyRequest(*args, **kwargs).to_proto(),
                local_service_pb2.EvaluateModifyResponse,
            ),
        ).as_type(types.EvaluateModifyResponse)

    @parameters(types.UnprepareModifyRequest)
    def unprepare_modify(self, *args, **kwargs):
        parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_UnprepareModify",
                types.UnprepareModifyRequest(*args, **kwargs).to_proto(),
                _empty_pb2.Empty,
            ),
        )

    @parameters(types.AnalyzeRequest)
    def analyze(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_Analyze",
                types.AnalyzeRequest(*args, **kwargs).to_proto(),
                local_service_pb2.AnalyzeResponse,
            ),
        ).as_type(types.AnalyzeResponse)

    @parameters(types.BuildSqlRequest)
    def build_sql(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_BuildSql",
                types.BuildSqlRequest(*args, **kwargs).to_proto(),
                local_service_pb2.BuildSqlResponse,
            ),
        ).as_type(types.BuildSqlResponse)

    @parameters(types.ParseRequest)
    def parse(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_Parse",
                types.ParseRequest(*args, **kwargs).to_proto(),
                local_service_pb2.ParseResponse,
            ),
        ).as_type(types.ParseResponse)

    @parameters(types.ExtractTableNamesFromStatementRequest)
    def extract_table_names_from_statement(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_ExtractTableNamesFromStatement",
                types.ExtractTableNamesFromStatementRequest(*args, **kwargs).to_proto(),
                local_service_pb2.ExtractTableNamesFromStatementResponse,
            ),
        ).as_type(types.ExtractTableNamesFromStatementResponse)

    @parameters(types.ExtractTableNamesFromNextStatementRequest)
    def extract_table_names_from_next_statement(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_ExtractTableNamesFromNextStatement",
                types.ExtractTableNamesFromNextStatementRequest(*args, **kwargs).to_proto(),
                local_service_pb2.ExtractTableNamesFromNextStatementResponse,
            ),
        ).as_type(types.ExtractTableNamesFromNextStatementResponse)

    @parameters(types.TableFromProtoRequest)
    def get_table_from_proto(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_GetTableFromProto",
                types.TableFromProtoRequest(*args, **kwargs).to_proto(),
                simple_table_pb2.SimpleTableProto,
            ),
        ).as_type(types.SimpleTable)

    @parameters(types.FormatSqlRequest)
    def format_sql(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_FormatSql",
                types.FormatSqlRequest(*args, **kwargs).to_proto(),
                local_service_pb2.FormatSqlResponse,
            ),
        ).as_type(types.FormatSqlResponse)

    @parameters(types.FormatSqlRequest)
    def lenient_format_sql(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_LenientFormatSql",
                types.FormatSqlRequest(*args, **kwargs).to_proto(),
                local_service_pb2.FormatSqlResponse,
            ),
        ).as_type(types.FormatSqlResponse)

    @parameters(types.RegisterCatalogRequest)
    def register_catalog(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_RegisterCatalog",
                types.RegisterCatalogRequest(*args, **kwargs).to_proto(),
                local_service_pb2.RegisterResponse,
            ),
        ).as_type(types.RegisterResponse)

    @parameters(types.UnregisterRequest)
    def unregister_catalog(self, *args, **kwargs):
        parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_UnregisterCatalog",
                types.UnregisterRequest(*args, **kwargs).to_proto(),
                _empty_pb2.Empty,
            ),
        )

    @parameters(types.ZetaSQLBuiltinFunctionOptions)
    def get_builtin_functions(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_GetBuiltinFunctions",
                types.ZetaSQLBuiltinFunctionOptions(*args, **kwargs).to_proto(),
                local_service_pb2.GetBuiltinFunctionsResponse,
            ),
        ).as_type(types.GetBuiltinFunctionsResponse)

    @parameters(types.LanguageOptionsRequest)
    def get_language_options(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_GetLanguageOptions",
                types.LanguageOptionsRequest(*args, **kwargs).to_proto(),
                options_pb2.LanguageOptionsProto,
            ),
        ).as_type(types.LanguageOptions)

    @parameters(types.AnalyzerOptionsRequest)
    def get_analyzer_options(self, *args, **kwargs):
        return parse_proto(
            self.wasm_client.call_grpc_func(
                "ZetaSqlLocalService_GetAnalyzerOptions",
                types.AnalyzerOptionsRequest(*args, **kwargs).to_proto(),
                options_pb2.AnalyzerOptionsProto,
            ),
        ).as_type(types.AnalyzerOptions)

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance
