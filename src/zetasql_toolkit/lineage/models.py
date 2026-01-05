"""Column-Level Lineage 데이터 모델

Java 원본: ColumnEntity.java, ColumnLineage.java
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, FrozenSet

if TYPE_CHECKING:
    from zetasql.core.types.proto_models import ResolvedColumn


@dataclass(frozen=True)
class ColumnEntity:
    """테이블의 컬럼을 나타내는 불변 엔티티.

    Java 원본: com.google.zetasql.toolkit.tools.lineage.ColumnEntity

    Attributes:
        table: 테이블의 전체 이름 (예: "project.dataset.table")
        name: 컬럼 이름 (대소문자 무시 비교)
    """

    table: str
    name: str

    def __eq__(self, other: object) -> bool:
        """동등성 비교 (컬럼 이름은 대소문자 무시)."""
        if not isinstance(other, ColumnEntity):
            return NotImplemented
        return self.table == other.table and self.name.lower() == other.name.lower()

    def __hash__(self) -> int:
        """해시값 (Set/Dict에서 사용)."""
        return hash((self.table, self.name.lower()))

    def __repr__(self) -> str:
        """읽기 좋은 문자열 표현."""
        return f"ColumnEntity(table='{self.table}', name='{self.name}')"

    def __str__(self) -> str:
        """정규화된 이름 (table.column)."""
        if self.table:
            return f"{self.table}.{self.name}"
        return self.name

    @staticmethod
    def from_resolved_column(column: ResolvedColumn) -> ColumnEntity:
        """ResolvedColumn에서 ColumnEntity 생성.

        Args:
            column: ZetaSQL의 ResolvedColumn 객체

        Returns:
            생성된 ColumnEntity
        """
        return ColumnEntity(
            table=column.table_name or "",
            name=column.name,
        )


@dataclass(frozen=True)
class ColumnLineage:
    """컬럼 간의 계보 관계를 나타냄.

    Java 원본: com.google.zetasql.toolkit.tools.lineage.ColumnLineage

    Attributes:
        target: 대상(결과) 컬럼
        parents: 소스(부모) 컬럼들의 집합
    """

    target: ColumnEntity
    parents: FrozenSet[ColumnEntity]

    def __repr__(self) -> str:
        """읽기 좋은 문자열 표현."""
        parents_str = ", ".join(str(p) for p in self.parents)
        return f"ColumnLineage(target={self.target}, parents=[{parents_str}])"

    def __str__(self) -> str:
        """계보 관계를 문자열로 표현."""
        lines = [f"{self.target}"]
        for parent in sorted(self.parents, key=lambda p: (p.table, p.name)):
            lines.append(f"  <- {parent}")
        return "\n".join(lines)
