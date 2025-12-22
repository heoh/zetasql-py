"""
Example: Wrapping ZetaSQL protobuf messages into Python classes

This shows how to create a more Pythonic API by wrapping the protobuf messages.
"""

from dataclasses import dataclass
from typing import List, Optional, Any
from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2


@dataclass
class Column:
    """Simplified column representation"""
    name: str
    table_name: str
    type_kind: str
    column_id: Optional[int] = None
    
    @classmethod
    def from_proto(cls, proto):
        """Create from protobuf ColumnProto"""
        type_kind_name = type_pb2.TypeKind.Name(proto.type.type_kind)
        return cls(
            name=proto.name,
            table_name=proto.table_name if proto.table_name else None,
            type_kind=type_kind_name,
            column_id=proto.column_id if proto.column_id else None
        )
    
    def __repr__(self):
        if self.table_name:
            return f"Column({self.table_name}.{self.name}: {self.type_kind})"
        return f"Column({self.name}: {self.type_kind})"


@dataclass
class Table:
    """Simplified table representation"""
    name: str
    full_name: str
    
    @classmethod
    def from_proto(cls, proto):
        """Create from protobuf SimpleTableProto"""
        return cls(
            name=proto.name,
            full_name=proto.full_name if proto.full_name else proto.name
        )
    
    def __repr__(self):
        return f"Table({self.name})"


class ResolvedNode:
    """Base class for all resolved nodes"""
    
    def __init__(self, proto):
        self._proto = proto
    
    @property
    def node_type(self) -> str:
        """Get the node type name"""
        return self._proto.WhichOneof('node')
    
    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.node_type})"


class ResolvedScan(ResolvedNode):
    """Wrapper for ResolvedScan nodes"""
    
    @property
    def columns(self) -> List[Column]:
        """Get column list (flattened from parent)"""
        # Access parent.column_list
        scan_node = self._get_scan_node()
        if scan_node and hasattr(scan_node, 'parent'):
            return [Column.from_proto(col) for col in scan_node.parent.column_list]
        return []
    
    @property
    def is_ordered(self) -> bool:
        """Check if scan is ordered (from parent)"""
        scan_node = self._get_scan_node()
        if scan_node and hasattr(scan_node, 'parent'):
            return scan_node.parent.is_ordered
        return False
    
    def _get_scan_node(self):
        """Get the actual scan node based on type"""
        node_type = self.node_type
        if node_type:
            return getattr(self._proto, node_type)
        return None


class ResolvedTableScan(ResolvedScan):
    """Wrapper for ResolvedTableScan"""
    
    @property
    def table(self) -> Table:
        """Get the table being scanned"""
        node = self._proto.resolved_table_scan_node
        return Table.from_proto(node.table)
    
    @property
    def column_indices(self) -> List[int]:
        """Get column index list"""
        node = self._proto.resolved_table_scan_node
        return list(node.column_index_list)
    
    def __repr__(self):
        return f"TableScan(table={self.table.name}, columns={len(self.columns)})"


class ResolvedFilterScan(ResolvedScan):
    """Wrapper for ResolvedFilterScan"""
    
    @property
    def input_scan(self) -> ResolvedScan:
        """Get input scan"""
        node = self._proto.resolved_filter_scan_node
        return wrap_scan(node.input_scan)
    
    @property
    def filter_expression(self):
        """Get filter expression (simplified representation)"""
        node = self._proto.resolved_filter_scan_node
        if node.HasField('filter_expr'):
            expr = node.filter_expr
            # Try to extract function name
            if expr.HasField('resolved_function_call_base_node'):
                func_node = expr.resolved_function_call_base_node
                if func_node.HasField('resolved_function_call_node'):
                    func_call = func_node.resolved_function_call_node
                    if func_call.parent.HasField('function'):
                        return func_call.parent.function.name
        return "unknown_filter"
    
    def __repr__(self):
        return f"FilterScan(filter={self.filter_expression}, columns={len(self.columns)})"


class ResolvedProjectScan(ResolvedScan):
    """Wrapper for ResolvedProjectScan"""
    
    @property
    def input_scan(self) -> ResolvedScan:
        """Get input scan"""
        node = self._proto.resolved_project_scan_node
        return wrap_scan(node.input_scan)
    
    @property
    def expressions_count(self) -> int:
        """Get number of projection expressions"""
        node = self._proto.resolved_project_scan_node
        return len(node.expr_list)
    
    def __repr__(self):
        return f"ProjectScan(expressions={self.expressions_count}, columns={len(self.columns)})"


class ResolvedAggregateScan(ResolvedScan):
    """Wrapper for ResolvedAggregateScan"""
    
    @property
    def input_scan(self) -> ResolvedScan:
        """Get input scan"""
        node = self._proto.resolved_aggregate_scan_node
        return wrap_scan(node.input_scan)
    
    @property
    def grouping_columns(self) -> List[Column]:
        """Get grouping columns"""
        node = self._proto.resolved_aggregate_scan_node
        return [Column.from_proto(col.column) for col in node.group_by_list]
    
    @property
    def aggregate_expressions_count(self) -> int:
        """Get number of aggregate expressions"""
        node = self._proto.resolved_aggregate_scan_node
        return len(node.aggregate_list)
    
    def __repr__(self):
        return f"AggregateScan(groups={len(self.grouping_columns)}, aggregates={self.aggregate_expressions_count})"


def wrap_scan(proto) -> ResolvedScan:
    """Wrap a scan proto into appropriate Python class"""
    node_type = proto.WhichOneof('node')
    
    if node_type == 'resolved_table_scan_node':
        return ResolvedTableScan(proto)
    elif node_type == 'resolved_filter_scan_node':
        return ResolvedFilterScan(proto)
    elif node_type == 'resolved_project_scan_node':
        return ResolvedProjectScan(proto)
    elif node_type == 'resolved_aggregate_scan_node':
        return ResolvedAggregateScan(proto)
    else:
        # Generic scan wrapper
        return ResolvedScan(proto)


class ResolvedQueryStatement:
    """Wrapper for ResolvedQueryStatement"""
    
    def __init__(self, proto):
        self._proto = proto
    
    @property
    def output_columns(self) -> List[Column]:
        """Get output columns"""
        return [Column.from_proto(col.column) for col in self._proto.output_column_list]
    
    @property
    def query(self) -> ResolvedScan:
        """Get the main query scan"""
        return wrap_scan(self._proto.query)
    
    def explain(self, indent=0) -> str:
        """Generate execution plan explanation"""
        lines = []
        lines.append("  " * indent + "OUTPUT:")
        for col in self.output_columns:
            lines.append("  " * (indent + 1) + f"- {col}")
        lines.append("  " * indent + "QUERY PLAN:")
        lines.extend(self._explain_scan(self.query, indent + 1))
        return "\n".join(lines)
    
    def _explain_scan(self, scan: ResolvedScan, indent: int) -> List[str]:
        """Recursively explain scan tree"""
        lines = []
        lines.append("  " * indent + f"→ {scan}")
        
        # Recursively explain input scans
        if hasattr(scan, 'input_scan'):
            lines.extend(self._explain_scan(scan.input_scan, indent + 1))
        
        return lines
    
    def __repr__(self):
        return f"QueryStatement(output_columns={len(self.output_columns)})"


def create_analyzer_options():
    opts = options_pb2.AnalyzerOptionsProto()
    language_options = opts.language_options
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    
    for feature in dir(public_options_pb2):
        if feature.startswith('FEATURE_'):
            if feature == 'FEATURE_SPANNER_LEGACY_DDL':
                continue
            try:
                feature_value = getattr(public_options_pb2, feature)
                if isinstance(feature_value, int) and feature_value > 0:
                    language_options.enabled_language_features.append(feature_value)
            except:
                pass
    
    return opts


def create_catalog(analyzer_options):
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
    table = catalog.table.add()
    table.name = "users"
    
    col = table.column.add()
    col.name = "id"
    col.type.type_kind = type_pb2.TYPE_INT64
    
    col = table.column.add()
    col.name = "name"
    col.type.type_kind = type_pb2.TYPE_STRING
    
    col = table.column.add()
    col.name = "age"
    col.type.type_kind = type_pb2.TYPE_INT64
    
    return catalog


def main():
    service = ZetaSqlLocalService()
    analyzer_options = create_analyzer_options()
    catalog = create_catalog(analyzer_options)
    
    print("="*70)
    print("Example 1: Simple SELECT with Python wrapper")
    print("="*70)
    
    sql = "SELECT id, name FROM users"
    print(f"\nSQL: {sql}\n")
    
    # Analyze
    response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    # Wrap in Python class
    query_stmt = ResolvedQueryStatement(response.resolved_statement.resolved_query_stmt_node)
    
    print("Wrapped representation:")
    print(f"  Statement: {query_stmt}")
    print(f"  Output columns: {query_stmt.output_columns}")
    print(f"  Query scan: {query_stmt.query}")
    
    print("\nExecution plan:")
    print(query_stmt.explain())
    
    print("\n" + "="*70)
    print("Example 2: SELECT with WHERE clause")
    print("="*70)
    
    sql = "SELECT id, name FROM users WHERE age > 18"
    print(f"\nSQL: {sql}\n")
    
    response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    query_stmt = ResolvedQueryStatement(response.resolved_statement.resolved_query_stmt_node)
    
    print("Wrapped representation:")
    print(f"  Output columns: {query_stmt.output_columns}")
    
    print("\nExecution plan:")
    print(query_stmt.explain())
    
    # Direct access to scan properties
    print("\nDirect property access:")
    scan = query_stmt.query
    print(f"  Top scan: {scan}")
    print(f"  Columns: {scan.columns}")
    print(f"  Is ordered: {scan.is_ordered}")
    
    if isinstance(scan, ResolvedFilterScan):
        print(f"  Filter: {scan.filter_expression}")
        print(f"  Input scan: {scan.input_scan}")
        
        if isinstance(scan.input_scan, ResolvedTableScan):
            print(f"  Table: {scan.input_scan.table}")
    
    print("\n" + "="*70)
    print("Example 3: Aggregation query")
    print("="*70)
    
    sql = "SELECT name, COUNT(*) as cnt FROM users GROUP BY name"
    print(f"\nSQL: {sql}\n")
    
    response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    query_stmt = ResolvedQueryStatement(response.resolved_statement.resolved_query_stmt_node)
    
    print("Execution plan:")
    print(query_stmt.explain())
    
    # Access aggregate info
    scan = query_stmt.query
    if isinstance(scan, ResolvedProjectScan):
        agg_scan = scan.input_scan
        if isinstance(agg_scan, ResolvedAggregateScan):
            print(f"\nAggregate details:")
            print(f"  Grouping columns: {agg_scan.grouping_columns}")
            print(f"  Number of aggregates: {agg_scan.aggregate_expressions_count}")
    
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    print("""
장점:
✓ parent 필드를 자동으로 플랫하게 접근
✓ 더 Pythonic한 API (properties, 메서드)
✓ 타입 안전성 (dataclass 사용)
✓ 쉬운 디버깅 (__repr__ 구현)
✓ 복잡한 protobuf 구조 숨김

단점:
✗ 초기 구현 비용
✗ protobuf 업데이트 시 유지보수 필요
✗ 모든 필드를 래핑하려면 많은 코드 필요

권장사항:
- 자주 사용하는 노드 타입만 래핑
- 필요한 필드만 노출
- 점진적으로 확장
    """)


if __name__ == "__main__":
    main()
