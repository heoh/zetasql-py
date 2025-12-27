 
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from zetasql.wasm_client import WasmClient
from zetasql.func_utils import parameters
from zetasql.types import parse_proto, proto_models
from zetasql.wasi import get_wasm_path
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2
from typing import TypeVar

Message = TypeVar("Message", bound=_message.Message)

class ZetaSqlLocalService:
    """Client for ZetaSQL Local Service via WASM.
    
    Uses ProtoModel objects for all API interactions. ProtoModel objects
    provide type-safe dataclass interfaces with automatic protobuf conversion.
    """

    def __init__(self):
        """
        Initialize the ZetaSQL Local Service client.

        Args:
            wasm_path: Path to the ZetaSQL WASM binary.
        """
        self.wasm_client = WasmClient(wasm_path=get_wasm_path())

    @parameters(proto_models.PrepareRequest)
    def prepare(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_Prepare",
            proto_models.PrepareRequest(*args, **kwargs).to_proto(),
            local_service_pb2.PrepareResponse,
        )).as_type(proto_models.PrepareResponse)

    @parameters(proto_models.EvaluateRequest)
    def evaluate(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_Evaluate",
            proto_models.EvaluateRequest(*args, **kwargs).to_proto(),
            local_service_pb2.EvaluateResponse,
        )).as_type(proto_models.EvaluateResponse)

    @parameters(proto_models.UnprepareRequest)
    def unprepare(self, *args, **kwargs):
        parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_Unprepare",
            proto_models.UnprepareRequest(*args, **kwargs).to_proto(),
            _empty_pb2.Empty,
        ))

    @parameters(proto_models.PrepareQueryRequest)
    def prepare_query(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_PrepareQuery",
            proto_models.PrepareQueryRequest(*args, **kwargs).to_proto(),
            local_service_pb2.PrepareQueryResponse,
        )).as_type(proto_models.PrepareQueryResponse)

    @parameters(proto_models.EvaluateQueryRequest)
    def evaluate_query(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_EvaluateQuery",
            proto_models.EvaluateQueryRequest(*args, **kwargs).to_proto(),
            local_service_pb2.EvaluateQueryResponse,
        )).as_type(proto_models.EvaluateQueryResponse)

    @parameters(proto_models.UnprepareQueryRequest)
    def unprepare_query(self, *args, **kwargs):
        parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_UnprepareQuery",
            proto_models.UnprepareQueryRequest(*args, **kwargs).to_proto(),
            _empty_pb2.Empty,
        ))

    @parameters(proto_models.PrepareModifyRequest)
    def prepare_modify(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_PrepareModify",
            proto_models.PrepareModifyRequest(*args, **kwargs).to_proto(),
            local_service_pb2.PrepareModifyResponse,
        )).as_type(proto_models.PrepareModifyResponse)

    @parameters(proto_models.EvaluateModifyRequest)
    def evaluate_modify(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_EvaluateModify",
            proto_models.EvaluateModifyRequest(*args, **kwargs).to_proto(),
            local_service_pb2.EvaluateModifyResponse,
        )).as_type(proto_models.EvaluateModifyResponse)

    @parameters(proto_models.UnprepareModifyRequest)
    def unprepare_modify(self, *args, **kwargs):
        parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_UnprepareModify",
            proto_models.UnprepareModifyRequest(*args, **kwargs).to_proto(),
            _empty_pb2.Empty,
        ))

    @parameters(proto_models.AnalyzeRequest)
    def analyze(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_Analyze",
            proto_models.AnalyzeRequest(*args, **kwargs).to_proto(),
            local_service_pb2.AnalyzeResponse,
        )).as_type(proto_models.AnalyzeResponse)

    @parameters(proto_models.BuildSqlRequest)
    def build_sql(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_BuildSql",
            proto_models.BuildSqlRequest(*args, **kwargs).to_proto(),
            local_service_pb2.BuildSqlResponse,
        )).as_type(proto_models.BuildSqlResponse)

    @parameters(proto_models.ParseRequest)
    def parse(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_Parse",
            proto_models.ParseRequest(*args, **kwargs).to_proto(),
            local_service_pb2.ParseResponse,
        )).as_type(proto_models.ParseResponse)

    @parameters(proto_models.ExtractTableNamesFromStatementRequest)
    def extract_table_names_from_statement(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_ExtractTableNamesFromStatement",
            proto_models.ExtractTableNamesFromStatementRequest(*args, **kwargs).to_proto(),
            local_service_pb2.ExtractTableNamesFromStatementResponse,
        )).as_type(proto_models.ExtractTableNamesFromStatementResponse)

    @parameters(proto_models.ExtractTableNamesFromNextStatementRequest)
    def extract_table_names_from_next_statement(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_ExtractTableNamesFromNextStatement",
            proto_models.ExtractTableNamesFromNextStatementRequest(*args, **kwargs).to_proto(),
            local_service_pb2.ExtractTableNamesFromNextStatementResponse,
        )).as_type(proto_models.ExtractTableNamesFromNextStatementResponse)

    @parameters(proto_models.TableFromProtoRequest)
    def get_table_from_proto(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_GetTableFromProto",
            proto_models.TableFromProtoRequest(*args, **kwargs).to_proto(),
            simple_table_pb2.SimpleTableProto,
        )).as_type(proto_models.SimpleTable)

    @parameters(proto_models.FormatSqlRequest)
    def format_sql(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_FormatSql",
            proto_models.FormatSqlRequest(*args, **kwargs).to_proto(),
            local_service_pb2.FormatSqlResponse,
        )).as_type(proto_models.FormatSqlResponse)

    @parameters(proto_models.FormatSqlRequest)
    def lenient_format_sql(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_LenientFormatSql",
            proto_models.FormatSqlRequest(*args, **kwargs).to_proto(),
            local_service_pb2.FormatSqlResponse,
        )).as_type(proto_models.FormatSqlResponse)

    @parameters(proto_models.RegisterCatalogRequest)
    def register_catalog(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_RegisterCatalog",
            proto_models.RegisterCatalogRequest(*args, **kwargs).to_proto(),
            local_service_pb2.RegisterResponse,
        )).as_type(proto_models.RegisterResponse)

    @parameters(proto_models.UnregisterRequest)
    def unregister_catalog(self, *args, **kwargs):
        parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_UnregisterCatalog",
            proto_models.UnregisterRequest(*args, **kwargs).to_proto(),
            _empty_pb2.Empty,
        ))

    @parameters(proto_models.ZetaSQLBuiltinFunctionOptions)
    def get_builtin_functions(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_GetBuiltinFunctions",
            proto_models.ZetaSQLBuiltinFunctionOptions(*args, **kwargs).to_proto(),
            local_service_pb2.GetBuiltinFunctionsResponse,
        )).as_type(proto_models.GetBuiltinFunctionsResponse)

    @parameters(proto_models.LanguageOptionsRequest)
    def get_language_options(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_GetLanguageOptions",
            proto_models.LanguageOptionsRequest(*args, **kwargs).to_proto(),
            options_pb2.LanguageOptionsProto,
        )).as_type(proto_models.LanguageOptions)

    @parameters(proto_models.AnalyzerOptionsRequest)
    def get_analyzer_options(self, *args, **kwargs):
        return parse_proto(self.wasm_client.call_grpc_func(
            "ZetaSqlLocalService_GetAnalyzerOptions",
            proto_models.AnalyzerOptionsRequest(*args, **kwargs).to_proto(),
            options_pb2.AnalyzerOptionsProto,
        )).as_type(proto_models.AnalyzerOptions)

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance
