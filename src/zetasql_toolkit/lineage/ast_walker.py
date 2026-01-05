"""AST Walker - ResolvedAST 순회 유틸리티

Java의 Visitor 패턴을 대체하는 Python 구현입니다.
"""

from __future__ import annotations

from typing import Callable, List, Any

# ResolvedNode의 기본 타입 (실제로는 proto_models에서 가져옴)
ResolvedNode = Any


def walk_resolved_tree(node: ResolvedNode, visitor_fn: Callable[[ResolvedNode], None]) -> None:
    """ResolvedAST를 DFS로 순회하며 각 노드에 visitor_fn을 호출.

    Java의 accept(Visitor) 패턴을 대체합니다.

    Args:
        node: 순회를 시작할 노드
        visitor_fn: 각 노드에 호출할 함수
    """
    if node is None:
        return

    # 현재 노드 방문
    visitor_fn(node)

    # 자식 노드들 순회
    for child in get_child_nodes(node):
        walk_resolved_tree(child, visitor_fn)


def get_child_nodes(node: ResolvedNode) -> List[ResolvedNode]:
    """노드의 자식 ResolvedNode들을 반환.

    Args:
        node: 자식을 가져올 노드

    Returns:
        자식 노드 리스트
    """
    if node is None:
        return []

    children: List[ResolvedNode] = []

    # 노드의 모든 속성 순회
    for attr_name in dir(node):
        # private 속성 및 메서드 제외
        if attr_name.startswith("_"):
            continue

        try:
            attr_value = getattr(node, attr_name, None)
        except Exception:
            continue

        if attr_value is None:
            continue

        # callable은 제외 (메서드)
        if callable(attr_value):
            continue

        # ResolvedNode 타입 체크 (클래스 이름으로 판단)
        if _is_resolved_node(attr_value):
            children.append(attr_value)
        elif isinstance(attr_value, (list, tuple)):
            for item in attr_value:
                if _is_resolved_node(item):
                    children.append(item)

    return children


def _is_resolved_node(obj: Any) -> bool:
    """객체가 ResolvedNode 타입인지 확인.

    Args:
        obj: 확인할 객체

    Returns:
        ResolvedNode이면 True
    """
    if obj is None:
        return False

    type_name = type(obj).__name__

    # Resolved로 시작하는 클래스는 ResolvedNode로 간주
    if type_name.startswith("Resolved"):
        return True

    return False
