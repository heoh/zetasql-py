#!/usr/bin/env python3
"""
Runtime wrapper generator using protobuf reflection

이미 생성된 _pb2.py 파일의 descriptor를 사용해서
런타임에 wrapper를 생성합니다. 가장 정확합니다!
"""

import sys
import importlib
from pathlib import Path
from typing import Dict, List, Set
from google.protobuf.descriptor import Descriptor, FieldDescriptor


def analyze_message(descriptor: Descriptor) -> Dict:
    """메시지 descriptor 분석"""
    
    info = {
        'name': descriptor.name,
        'full_name': descriptor.full_name,
        'fields': [],
        'parent_field': None,
        'parent_type': None,
    }
    
    for field in descriptor.fields:
        # type_name 안전하게 가져오기
        type_name = None
        if field.type == FieldDescriptor.TYPE_MESSAGE:
            try:
                type_name = field.message_type.name if hasattr(field, 'message_type') else None
            except:
                pass
        
        field_info = {
            'name': field.name,
            'number': field.number,
            'type': field.type,
            'type_name': type_name,
            'label': field.label,
            'is_repeated': field.label == FieldDescriptor.LABEL_REPEATED,
            'is_message': field.type == FieldDescriptor.TYPE_MESSAGE,
        }
        
        info['fields'].append(field_info)
        
        # parent 필드 찾기
        if field.name == 'parent' and field.type == FieldDescriptor.TYPE_MESSAGE:
            info['parent_field'] = field_info
            if type_name:
                info['parent_type'] = type_name  # 이미 짧은 이름
    
    return info


def generate_wrapper_code(msg_info: Dict, all_messages: Dict[str, Dict]) -> str:
    """메시지 정보에서 wrapper 코드 생성"""
    
    class_name = msg_info['name'].replace('Proto', '')
    lines = []
    
    # 클래스 정의
    base_class = 'BaseNode'
    if msg_info['parent_type']:
        base_class = msg_info['parent_type'].replace('Proto', '')
    
    lines.append(f"class {class_name}({base_class}):")
    lines.append(f'    """Wrapper for {msg_info["name"]}"""')
    lines.append("")
    
    # oneof 필드 이름 (소문자 + _node)
    proto_field = to_snake_case(class_name) + "_node"
    
    # 자신의 필드들 (parent 제외)
    own_fields = [f for f in msg_info['fields'] if f['name'] != 'parent']
    
    for field in own_fields:
        field_name = field['name']
        
        lines.append(f"    @property")
        lines.append(f"    def {field_name}(self):")
        lines.append(f'        """Access {field_name}"""')
        
        # 필드 접근 경로
        access_path = f"self._proto.{proto_field}.{field_name}"
        
        if field['is_repeated']:
            lines.append(f"        return list({access_path})")
        elif field['is_message']:
            # 메시지 타입이면 래핑
            msg_type = field['type_name'].split('.')[-1].replace('Proto', '')
            lines.append(f"        try:")
            lines.append(f"            if self._proto.{proto_field}.HasField('{field_name}'):")
            lines.append(f"                return {msg_type}.from_proto({access_path})")
            lines.append(f"        except ValueError:")
            lines.append(f"            pass")
            lines.append(f"        return {access_path}")
        else:
            lines.append(f"        return {access_path}")
        
        lines.append("")
    
    # parent로부터 상속받은 필드들
    if msg_info['parent_type'] and msg_info['parent_type'] in all_messages:
        parent_msg = all_messages[msg_info['parent_type']]
        parent_fields = [f for f in parent_msg['fields'] if f['name'] != 'parent']
        
        if parent_fields:
            lines.append("    # Inherited from parent")
            lines.append("")
        
        for field in parent_fields:
            field_name = field['name']
            
            lines.append(f"    @property")
            lines.append(f"    def {field_name}(self):")
            lines.append(f'        """Access {field_name} (inherited)"""')
            
            access_path = f"self._proto.{proto_field}.parent.{field_name}"
            
            if field['is_repeated']:
                lines.append(f"        return list({access_path})")
            elif field['is_message']:
                msg_type = field['type_name'].split('.')[-1].replace('Proto', '')
                lines.append(f"        try:")
                lines.append(f"            if self._proto.{proto_field}.parent.HasField('{field_name}'):")
                lines.append(f"                return {msg_type}.from_proto({access_path})")
                lines.append(f"        except ValueError:")
                lines.append(f"            pass")
                lines.append(f"        return {access_path}")
            else:
                lines.append(f"        return {access_path}")
            
            lines.append("")
    
    lines.append(f"    def __repr__(self):")
    lines.append(f"        return f'{class_name}()'")
    lines.append("")
    
    return "\n".join(lines)


def to_snake_case(name: str) -> str:
    """CamelCase를 snake_case로"""
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def generate_from_module(module_name: str, message_names: List[str], output_path: Path):
    """Python 모듈에서 메시지를 로드하고 wrapper 생성"""
    
    print(f"Importing module: {module_name}")
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error importing module: {e}")
        sys.exit(1)
    
    # 메시지 정보 수집
    messages = {}
    
    for msg_name in message_names:
        if not hasattr(module, msg_name):
            print(f"Warning: {msg_name} not found in {module_name}")
            continue
        
        msg_class = getattr(module, msg_name)
        descriptor = msg_class.DESCRIPTOR
        
        info = analyze_message(descriptor)
        messages[info['name']] = info
        
        print(f"  Found: {info['name']} ({len(info['fields'])} fields)")
    
    # wrapper 코드 생성
    lines = []
    
    # 헤더
    lines.append('"""')
    lines.append(f"Auto-generated wrappers from {module_name}")
    lines.append('"""')
    lines.append("")
    lines.append("from typing import List, Optional")
    lines.append(f"from {module_name} import *")
    lines.append("")
    
    # 베이스 클래스
    lines.append('''
class BaseNode:
    """Base node wrapper"""
    
    def __init__(self, proto):
        self._proto = proto
    
    @classmethod
    def from_proto(cls, proto):
        return cls(proto)
    
    @property
    def proto(self):
        return self._proto
''')
    lines.append("")
    
    # 각 메시지 wrapper
    for msg_info in messages.values():
        lines.append(generate_wrapper_code(msg_info, messages))
        lines.append("")
    
    # 파일 작성
    output_path.write_text("\n".join(lines))
    print(f"\nGenerated: {output_path}")
    print(f"Total classes: {len(messages)}")


def main():
    """메인 함수"""
    
    print("="*70)
    print("Protobuf Wrapper Generator (Reflection-based)")
    print("="*70)
    print()
    
    # ZetaSQL resolved_ast 메시지들
    module_name = "zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2"
    
    message_names = [
        "ResolvedScanProto",
        "ResolvedTableScanProto",
        "ResolvedFilterScanProto", 
        "ResolvedProjectScanProto",
        "ResolvedAggregateScanProto",
        "ResolvedJoinScanProto",
        "ResolvedOrderByScanProto",
        "ResolvedLimitOffsetScanProto",
    ]
    
    output_path = Path("generated_wrappers_reflection.py")
    
    generate_from_module(module_name, message_names, output_path)
    
    print("\n" + "="*70)
    print("Done!")
    print("="*70)
    print(f"\nUsage:")
    print(f"  from generated_wrappers_reflection import *")
    print(f"  ")
    print(f"  scan = ResolvedTableScan.from_proto(proto_message)")
    print(f"  print(scan.columns)  # Direct access!")


if __name__ == "__main__":
    main()
