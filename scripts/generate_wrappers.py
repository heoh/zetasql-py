#!/usr/bin/env python3
"""
Protobuf wrapper generator

.proto 파일에서 메시지 정의를 읽고 Python wrapper 클래스를 자동 생성합니다.
parent 필드 패턴을 인식하고 플랫한 속성 접근을 제공합니다.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Optional, Set
from dataclasses import dataclass


@dataclass
class Field:
    """Protobuf field 정보"""
    name: str
    type: str
    label: str  # optional, repeated, required
    number: int
    
    @property
    def is_repeated(self) -> bool:
        return self.label == "repeated"
    
    @property
    def is_parent(self) -> bool:
        return self.name == "parent"


@dataclass
class Message:
    """Protobuf message 정보"""
    name: str
    fields: List[Field]
    parent_message: Optional[str] = None  # parent 필드의 타입
    
    @property
    def python_class_name(self) -> str:
        """Proto 이름에서 Python 클래스 이름 생성"""
        # ResolvedTableScanProto -> ResolvedTableScan
        return self.name.replace("Proto", "")
    
    @property
    def base_class_name(self) -> str:
        """부모 클래스 이름"""
        if self.parent_message:
            return self.parent_message.replace("Proto", "")
        return "BaseNode"
    
    @property
    def own_fields(self) -> List[Field]:
        """parent 제외한 자신의 필드들"""
        return [f for f in self.fields if not f.is_parent]
    
    @property
    def parent_field(self) -> Optional[Field]:
        """parent 필드"""
        for f in self.fields:
            if f.is_parent:
                return f
        return None


def parse_proto_file(proto_path: Path) -> List[Message]:
    """
    .proto 파일을 파싱해서 메시지 정의 추출
    
    간단한 정규식 기반 파서입니다. 복잡한 proto는 처리 못할 수 있습니다.
    """
    content = proto_path.read_text()
    messages = []
    
    # message 블록 찾기
    message_pattern = r'message\s+(\w+)\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}'
    
    for match in re.finditer(message_pattern, content, re.MULTILINE | re.DOTALL):
        msg_name = match.group(1)
        msg_body = match.group(2)
        
        # 필드 파싱
        fields = []
        field_pattern = r'(optional|repeated|required)?\s*(\w+)\s+(\w+)\s*=\s*(\d+)'
        
        parent_msg = None
        
        for field_match in re.finditer(field_pattern, msg_body):
            label = field_match.group(1) or "optional"
            field_type = field_match.group(2)
            field_name = field_match.group(3)
            field_num = int(field_match.group(4))
            
            field = Field(
                name=field_name,
                type=field_type,
                label=label,
                number=field_num
            )
            fields.append(field)
            
            # parent 필드면 타입 저장
            if field_name == "parent":
                parent_msg = field_type
        
        if fields:  # 필드가 있는 메시지만
            messages.append(Message(
                name=msg_name,
                fields=fields,
                parent_message=parent_msg
            ))
    
    return messages


def generate_wrapper_class(msg: Message, all_messages: Dict[str, Message]) -> str:
    """메시지에 대한 wrapper 클래스 생성"""
    
    lines = []
    
    # 클래스 정의
    class_name = msg.python_class_name
    base_name = msg.base_class_name if msg.parent_message else "BaseNode"
    
    lines.append(f"class {class_name}({base_name}):")
    lines.append(f'    """Wrapper for {msg.name}"""')
    lines.append("")
    
    # proto 필드 이름 (oneof 처리를 위해)
    proto_field = to_snake_case(msg.python_class_name) + "_node"
    lines.append(f"    _proto_field = '{proto_field}'")
    lines.append("")
    
    # 자신의 필드들에 대한 property 생성
    for field in msg.own_fields:
        prop_name = field.name
        field_access = f"self._proto.{proto_field}.{field.name}"
        
        lines.append(f"    @property")
        lines.append(f"    def {prop_name}(self):")
        lines.append(f'        """Get {field.name}"""')
        
        if field.is_repeated:
            lines.append(f"        return list({field_access})")
        else:
            # 타입에 따라 래핑
            if field.type.endswith("Proto"):
                wrapper_class = field.type.replace("Proto", "")
                lines.append(f"        if self._proto.{proto_field}.HasField('{field.name}'):")
                lines.append(f"            return {wrapper_class}.from_proto({field_access})")
                lines.append(f"        return None")
            else:
                lines.append(f"        return {field_access}")
        
        lines.append("")
    
    # parent 필드가 있으면 상속받은 필드들도 노출
    if msg.parent_message and msg.parent_message in all_messages:
        parent_msg = all_messages[msg.parent_message]
        
        lines.append("    # Inherited fields from parent")
        
        for field in parent_msg.own_fields:
            prop_name = field.name
            field_access = f"self._proto.{proto_field}.parent.{field.name}"
            
            lines.append(f"    @property")
            lines.append(f"    def {prop_name}(self):")
            lines.append(f'        """Get {field.name} (inherited)"""')
            
            if field.is_repeated:
                lines.append(f"        return list({field_access})")
            else:
                if field.type.endswith("Proto"):
                    wrapper_class = field.type.replace("Proto", "")
                    lines.append(f"        if self._proto.{proto_field}.parent.HasField('{field.name}'):")
                    lines.append(f"            return {wrapper_class}.from_proto({field_access})")
                    lines.append(f"        return None")
                else:
                    lines.append(f"        return {field_access}")
            
            lines.append("")
    
    lines.append(f"    def __repr__(self):")
    lines.append(f"        return f'{class_name}(...)'")
    lines.append("")
    
    return "\n".join(lines)


def to_snake_case(name: str) -> str:
    """CamelCase를 snake_case로 변환"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def generate_base_class() -> str:
    """기본 베이스 클래스 생성"""
    return '''
class BaseNode:
    """Base class for all wrapper nodes"""
    
    def __init__(self, proto):
        self._proto = proto
    
    @classmethod
    def from_proto(cls, proto):
        """Create wrapper from protobuf message"""
        return cls(proto)
    
    @property
    def proto(self):
        """Get underlying protobuf message"""
        return self._proto
'''


def generate_wrapper_file(messages: List[Message], output_path: Path):
    """전체 wrapper 파일 생성"""
    
    # 메시지를 딕셔너리로
    msg_dict = {msg.name: msg for msg in messages}
    
    lines = []
    
    # 헤더
    lines.append('"""')
    lines.append("Auto-generated wrapper classes for ZetaSQL protobuf messages")
    lines.append('"""')
    lines.append("")
    lines.append("from typing import List, Optional")
    lines.append("")
    
    # 베이스 클래스
    lines.append(generate_base_class())
    lines.append("")
    
    # 각 메시지에 대한 wrapper
    for msg in messages:
        lines.append(generate_wrapper_class(msg, msg_dict))
        lines.append("")
    
    # 파일 작성
    output_path.write_text("\n".join(lines))
    print(f"Generated: {output_path}")


def main():
    """메인 함수"""
    
    if len(sys.argv) < 2:
        print("Usage: python generate_wrappers.py <proto_file> [output_file]")
        print("\nExample:")
        print("  python generate_wrappers.py src/zetasql/wasi/proto/zetasql/resolved_ast/resolved_ast.proto")
        sys.exit(1)
    
    proto_path = Path(sys.argv[1])
    
    if not proto_path.exists():
        print(f"Error: {proto_path} not found")
        sys.exit(1)
    
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("generated_wrappers.py")
    
    print(f"Parsing: {proto_path}")
    messages = parse_proto_file(proto_path)
    
    print(f"Found {len(messages)} messages")
    
    # parent가 있는 메시지만 필터링 (필요시)
    # messages = [m for m in messages if m.parent_message]
    
    # 일부만 생성하려면 필터링
    interesting_messages = [
        "ResolvedScanProto",
        "ResolvedTableScanProto", 
        "ResolvedFilterScanProto",
        "ResolvedProjectScanProto",
        "ResolvedAggregateScanProto",
        "ResolvedJoinScanProto",
    ]
    
    messages = [m for m in messages if m.name in interesting_messages]
    
    print(f"Generating wrappers for {len(messages)} messages")
    
    generate_wrapper_file(messages, output_path)
    
    print("\nDone! You can now import and use the generated wrappers.")
    print(f"\nNext steps:")
    print(f"1. Review {output_path}")
    print(f"2. Add proper imports for protobuf types")
    print(f"3. Customize the wrappers as needed")


if __name__ == "__main__":
    main()
