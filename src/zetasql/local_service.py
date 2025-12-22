from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from zetasql.client import WasmClient
from zetasql.grpc_utils import call_grpc_func, grpc_method
from zetasql.wasi import get_wasm_path
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2 as _local_service_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2 as _options_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2 as _simple_table_pb2
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

    @grpc_method(_local_service_pb2.PrepareRequest)
    def prepare(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_Prepare",
            _local_service_pb2.PrepareRequest(*args, **kwargs),
            _local_service_pb2.PrepareResponse,
        )

    @grpc_method(_local_service_pb2.EvaluateRequest)
    def evaluate(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_Evaluate",
            _local_service_pb2.EvaluateRequest(*args, **kwargs),
            _local_service_pb2.EvaluateResponse,
        )

    @grpc_method(_local_service_pb2.UnprepareRequest)
    def unprepare(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_Unprepare",
            _local_service_pb2.UnprepareRequest(*args, **kwargs),
            _empty_pb2.Empty,
        )

    @grpc_method(_local_service_pb2.PrepareQueryRequest)
    def prepare_query(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_PrepareQuery",
            _local_service_pb2.PrepareQueryRequest(*args, **kwargs),
            _local_service_pb2.PrepareQueryResponse,
        )

    @grpc_method(_local_service_pb2.EvaluateQueryRequest)
    def evaluate_query(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_EvaluateQuery",
            _local_service_pb2.EvaluateQueryRequest(*args, **kwargs),
            _local_service_pb2.EvaluateQueryResponse,
        )

    @grpc_method(_local_service_pb2.UnprepareQueryRequest)
    def unprepare_query(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_UnprepareQuery",
            _local_service_pb2.UnprepareQueryRequest(*args, **kwargs),
            _empty_pb2.Empty,
        )

    @grpc_method(_local_service_pb2.PrepareModifyRequest)
    def prepare_modify(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_PrepareModify",
            _local_service_pb2.PrepareModifyRequest(*args, **kwargs),
            _local_service_pb2.PrepareModifyResponse,
        )

    @grpc_method(_local_service_pb2.EvaluateModifyRequest)
    def evaluate_modify(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_EvaluateModify",
            _local_service_pb2.EvaluateModifyRequest(*args, **kwargs),
            _local_service_pb2.EvaluateModifyResponse,
        )

    @grpc_method(_local_service_pb2.UnprepareModifyRequest)
    def unprepare_modify(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_UnprepareModify",
            _local_service_pb2.UnprepareModifyRequest(*args, **kwargs),
            _empty_pb2.Empty,
        )

    @grpc_method(_local_service_pb2.AnalyzeRequest)
    def analyze(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_Analyze",
            _local_service_pb2.AnalyzeRequest(*args, **kwargs),
            _local_service_pb2.AnalyzeResponse,
        )

    @grpc_method(_local_service_pb2.BuildSqlRequest)
    def build_sql(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_BuildSql",
            _local_service_pb2.BuildSqlRequest(*args, **kwargs),
            _local_service_pb2.BuildSqlResponse,
        )

    @grpc_method(_local_service_pb2.ParseRequest)
    def parse(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_Parse",
            _local_service_pb2.ParseRequest(*args, **kwargs),
            _local_service_pb2.ParseResponse,
        )

    @grpc_method(_local_service_pb2.ExtractTableNamesFromStatementRequest)
    def extract_table_names_from_statement(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_ExtractTableNamesFromStatement",
            _local_service_pb2.ExtractTableNamesFromStatementRequest(*args, **kwargs),
            _local_service_pb2.ExtractTableNamesFromStatementResponse,
        )

    @grpc_method(_local_service_pb2.ExtractTableNamesFromNextStatementRequest)
    def extract_table_names_from_next_statement(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_ExtractTableNamesFromNextStatement",
            _local_service_pb2.ExtractTableNamesFromNextStatementRequest(*args, **kwargs),
            _local_service_pb2.ExtractTableNamesFromNextStatementResponse,
        )

    @grpc_method(_local_service_pb2.TableFromProtoRequest)
    def get_table_from_proto(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_GetTableFromProto",
            _local_service_pb2.TableFromProtoRequest(*args, **kwargs),
            _simple_table_pb2.SimpleTableProto,
        )

    @grpc_method(_local_service_pb2.FormatSqlRequest)
    def format_sql(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_FormatSql",
            _local_service_pb2.FormatSqlRequest(*args, **kwargs),
            _local_service_pb2.FormatSqlResponse,
        )

    @grpc_method(_local_service_pb2.FormatSqlRequest)
    def lenient_format_sql(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_LenientFormatSql",
            _local_service_pb2.FormatSqlRequest(*args, **kwargs),
            _local_service_pb2.FormatSqlResponse,
        )

    @grpc_method(_local_service_pb2.RegisterCatalogRequest)
    def register_catalog(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_RegisterCatalog",
            _local_service_pb2.RegisterCatalogRequest(*args, **kwargs),
            _local_service_pb2.RegisterResponse,
        )

    @grpc_method(_local_service_pb2.UnregisterRequest)
    def unregister_catalog(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_UnregisterCatalog",
            _local_service_pb2.UnregisterRequest(*args, **kwargs),
            _empty_pb2.Empty,
        )

    @grpc_method(_options_pb2.ZetaSQLBuiltinFunctionOptionsProto)
    def get_builtin_functions(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_GetBuiltinFunctions",
            _options_pb2.ZetaSQLBuiltinFunctionOptionsProto(*args, **kwargs),
            _local_service_pb2.GetBuiltinFunctionsResponse,
        )

    @grpc_method(_local_service_pb2.LanguageOptionsRequest)
    def get_language_options(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_GetLanguageOptions",
            _local_service_pb2.LanguageOptionsRequest(*args, **kwargs),
            _options_pb2.LanguageOptionsProto,
        )

    @grpc_method(_local_service_pb2.AnalyzerOptionsRequest)
    def get_analyzer_options(self, *args, **kwargs):
        return self._call_grpc_method(
            "ZetaSqlLocalService_GetAnalyzerOptions",
            _local_service_pb2.AnalyzerOptionsRequest(*args, **kwargs),
            _options_pb2.AnalyzerOptionsProto,
        )
