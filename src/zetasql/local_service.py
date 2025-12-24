from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from zetasql.client import WasmClient
from zetasql.grpc_utils import call_grpc_func, grpc_method
from zetasql.types import parse_proto, proto_models
from zetasql.wasi import get_wasm_path
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2
from typing import TypeVar

Message = TypeVar("Message", bound=_message.Message)

class ZetaSqlLocalService:
    """Client for ZetaSQL Local Service via WASM."""

    def __init__(self):
        """
        Initialize the ZetaSQL Local Service client.

        Args:
            wasm_path: Path to the ZetaSQL WASM binary.
        """
        self.wasm_client = WasmClient(wasm_path=get_wasm_path())

    def _call_grpc_method(self, method_name: str, request: _message.Message, response_type: type[Message]) -> Message:
        return call_grpc_func(self.wasm_client, method_name, request, response_type)

    @grpc_method(local_service_pb2.PrepareRequest)
    def prepare(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_Prepare",
            local_service_pb2.PrepareRequest(*args, **kwargs),
            local_service_pb2.PrepareResponse,
        )).as_type(proto_models.PrepareResponse)

    @grpc_method(local_service_pb2.EvaluateRequest)
    def evaluate(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_Evaluate",
            local_service_pb2.EvaluateRequest(*args, **kwargs),
            local_service_pb2.EvaluateResponse,
        )).as_type(proto_models.EvaluateResponse)

    @grpc_method(local_service_pb2.UnprepareRequest)
    def unprepare(self, *args, **kwargs):
        parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_Unprepare",
            local_service_pb2.UnprepareRequest(*args, **kwargs),
            _empty_pb2.Empty,
        ))

    @grpc_method(local_service_pb2.PrepareQueryRequest)
    def prepare_query(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_PrepareQuery",
            local_service_pb2.PrepareQueryRequest(*args, **kwargs),
            local_service_pb2.PrepareQueryResponse,
        )).as_type(proto_models.PrepareQueryResponse)

    @grpc_method(local_service_pb2.EvaluateQueryRequest)
    def evaluate_query(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_EvaluateQuery",
            local_service_pb2.EvaluateQueryRequest(*args, **kwargs),
            local_service_pb2.EvaluateQueryResponse,
        )).as_type(proto_models.EvaluateQueryResponse)

    @grpc_method(local_service_pb2.UnprepareQueryRequest)
    def unprepare_query(self, *args, **kwargs):
        parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_UnprepareQuery",
            local_service_pb2.UnprepareQueryRequest(*args, **kwargs),
            _empty_pb2.Empty,
        ))

    @grpc_method(local_service_pb2.PrepareModifyRequest)
    def prepare_modify(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_PrepareModify",
            local_service_pb2.PrepareModifyRequest(*args, **kwargs),
            local_service_pb2.PrepareModifyResponse,
        )).as_type(proto_models.PrepareModifyResponse)

    @grpc_method(local_service_pb2.EvaluateModifyRequest)
    def evaluate_modify(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_EvaluateModify",
            local_service_pb2.EvaluateModifyRequest(*args, **kwargs),
            local_service_pb2.EvaluateModifyResponse,
        )).as_type(proto_models.EvaluateModifyResponse)

    @grpc_method(local_service_pb2.UnprepareModifyRequest)
    def unprepare_modify(self, *args, **kwargs):
        parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_UnprepareModify",
            local_service_pb2.UnprepareModifyRequest(*args, **kwargs),
            _empty_pb2.Empty,
        ))

    @grpc_method(local_service_pb2.AnalyzeRequest)
    def analyze(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_Analyze",
            local_service_pb2.AnalyzeRequest(*args, **kwargs),
            local_service_pb2.AnalyzeResponse,
        )).as_type(proto_models.AnalyzeResponse)

    @grpc_method(local_service_pb2.BuildSqlRequest)
    def build_sql(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_BuildSql",
            local_service_pb2.BuildSqlRequest(*args, **kwargs),
            local_service_pb2.BuildSqlResponse,
        )).as_type(proto_models.BuildSqlResponse)

    @grpc_method(local_service_pb2.ParseRequest)
    def parse(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_Parse",
            local_service_pb2.ParseRequest(*args, **kwargs),
            local_service_pb2.ParseResponse,
        )).as_type(proto_models.ParseResponse)

    @grpc_method(local_service_pb2.ExtractTableNamesFromStatementRequest)
    def extract_table_names_from_statement(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_ExtractTableNamesFromStatement",
            local_service_pb2.ExtractTableNamesFromStatementRequest(*args, **kwargs),
            local_service_pb2.ExtractTableNamesFromStatementResponse,
        )).as_type(proto_models.ExtractTableNamesFromStatementResponse)

    @grpc_method(local_service_pb2.ExtractTableNamesFromNextStatementRequest)
    def extract_table_names_from_next_statement(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_ExtractTableNamesFromNextStatement",
            local_service_pb2.ExtractTableNamesFromNextStatementRequest(*args, **kwargs),
            local_service_pb2.ExtractTableNamesFromNextStatementResponse,
        )).as_type(proto_models.ExtractTableNamesFromNextStatementResponse)

    @grpc_method(local_service_pb2.TableFromProtoRequest)
    def get_table_from_proto(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_GetTableFromProto",
            local_service_pb2.TableFromProtoRequest(*args, **kwargs),
            simple_table_pb2.SimpleTableProto,
        )).as_type(proto_models.SimpleTable)

    @grpc_method(local_service_pb2.FormatSqlRequest)
    def format_sql(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_FormatSql",
            local_service_pb2.FormatSqlRequest(*args, **kwargs),
            local_service_pb2.FormatSqlResponse,
        )).as_type(proto_models.FormatSqlResponse)

    @grpc_method(local_service_pb2.FormatSqlRequest)
    def lenient_format_sql(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_LenientFormatSql",
            local_service_pb2.FormatSqlRequest(*args, **kwargs),
            local_service_pb2.FormatSqlResponse,
        )).as_type(proto_models.FormatSqlResponse)

    @grpc_method(local_service_pb2.RegisterCatalogRequest)
    def register_catalog(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_RegisterCatalog",
            local_service_pb2.RegisterCatalogRequest(*args, **kwargs),
            local_service_pb2.RegisterResponse,
        )).as_type(proto_models.RegisterResponse)

    @grpc_method(local_service_pb2.UnregisterRequest)
    def unregister_catalog(self, *args, **kwargs):
        parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_UnregisterCatalog",
            local_service_pb2.UnregisterRequest(*args, **kwargs),
            _empty_pb2.Empty,
        ))

    @grpc_method(options_pb2.ZetaSQLBuiltinFunctionOptionsProto)
    def get_builtin_functions(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_GetBuiltinFunctions",
            options_pb2.ZetaSQLBuiltinFunctionOptionsProto(*args, **kwargs),
            local_service_pb2.GetBuiltinFunctionsResponse,
        )).as_type(proto_models.GetBuiltinFunctionsResponse)

    @grpc_method(local_service_pb2.LanguageOptionsRequest)
    def get_language_options(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_GetLanguageOptions",
            local_service_pb2.LanguageOptionsRequest(*args, **kwargs),
            options_pb2.LanguageOptionsProto,
        )).as_type(proto_models.LanguageOptions)

    @grpc_method(local_service_pb2.AnalyzerOptionsRequest)
    def get_analyzer_options(self, *args, **kwargs):
        return parse_proto(self._call_grpc_method(
            "ZetaSqlLocalService_GetAnalyzerOptions",
            local_service_pb2.AnalyzerOptionsRequest(*args, **kwargs),
            options_pb2.AnalyzerOptionsProto,
        )).as_type(proto_models.AnalyzerOptions)
