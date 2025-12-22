"""
Understanding the 'parent' field in ZetaSQL AST

The 'parent' field is NOT a reference to the parent node in the tree.
It contains fields from the parent CLASS in the inheritance hierarchy.
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2


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
    
    return catalog


def main():
    service = ZetaSqlLocalService()
    analyzer_options = create_analyzer_options()
    catalog = create_catalog(analyzer_options)
    
    sql = "SELECT id, name FROM users"
    
    analyze_response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    # Resolved AST의 구조
    resolved_stmt = analyze_response.resolved_statement.resolved_query_stmt_node
    query_node = resolved_stmt.query
    
    print("="*70)
    print("Understanding the 'parent' field structure")
    print("="*70)
    
    print("\n1. query_node의 타입:")
    print(f"   {query_node.WhichOneof('node')}")
    
    # ProjectScan 노드 가져오기
    project_scan = query_node.resolved_project_scan_node
    
    print("\n2. ResolvedProjectScan의 구조:")
    print(f"   - 고유 필드: expr_list (projection expressions)")
    print(f"   - 고유 필드: input_scan (입력 스캔)")
    print(f"   - parent 필드에 있는 것들:")
    
    # parent는 ResolvedScan의 공통 필드들을 담고 있음
    parent_scan = project_scan.parent
    print(f"     * column_list: {len(parent_scan.column_list)}개 컬럼")
    for col in parent_scan.column_list:
        print(f"       - {col.table_name}.{col.name} ({col.type.type_kind})")
    print(f"     * is_ordered: {parent_scan.is_ordered}")
    
    print("\n3. 실제로 필드 접근 방법:")
    print(f"   project_scan.parent.column_list  ← 이렇게 접근")
    print(f"   = {[f'{c.name}' for c in project_scan.parent.column_list]}")
    
    print("\n4. InputScan (TableScan)의 구조:")
    input_scan = project_scan.input_scan
    print(f"   타입: {input_scan.WhichOneof('node')}")
    
    table_scan = input_scan.resolved_table_scan_node
    
    print(f"\n   ResolvedTableScan 고유 필드:")
    print(f"   - table.name: {table_scan.table.name}")
    print(f"   - column_index_list: {list(table_scan.column_index_list)}")
    
    print(f"\n   ResolvedTableScan.parent (ResolvedScan 공통 필드):")
    print(f"   - column_list: {len(table_scan.parent.column_list)}개")
    for col in table_scan.parent.column_list:
        print(f"     * {col.name}")
    
    print("\n" + "="*70)
    print("핵심 정리")
    print("="*70)
    print("""
1. 'parent' 필드의 의미:
   - 트리의 부모 노드 참조 ✗
   - 클래스 상속의 부모 클래스 필드들 ✓
   
2. 왜 이렇게 하나?
   - Protobuf는 클래스 상속을 지원하지 않음
   - C++ 클래스 계층을 protobuf로 표현하는 패턴
   
3. 클래스 계층 예시:
   ResolvedNode (최상위)
     └─ ResolvedScan (중간)
          ├─ column_list
          ├─ is_ordered
          └─ ResolvedTableScan (구체 클래스)
               ├─ parent { column_list, is_ordered }  ← ResolvedScan 필드
               ├─ table
               └─ column_index_list
   
4. 직접 부모에 두지 않는 이유:
   - 여러 노드 타입이 같은 기본 필드를 공유
   - parent 필드로 묶어서 구조를 명확히 함
   - C++ 코드와 protobuf 간의 매핑을 단순화
   
5. 실제 사용:
   - parent 필드는 보통 무시하고 직접 접근
   - 또는 필요한 공통 필드만 parent에서 추출
    """)


if __name__ == "__main__":
    main()
