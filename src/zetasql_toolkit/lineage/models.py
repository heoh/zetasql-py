"""
Data models for column-level lineage.

This module defines the core data structures used in lineage extraction:
- ColumnEntity: Represents a table.column reference
- ColumnLineage: Maps a target column to its source columns
"""
from dataclasses import dataclass
from typing import Set

from zetasql.core.types.proto_models import ResolvedColumn


@dataclass(frozen=True)
class ColumnEntity:
    """
    Represents a reference to a column in a table.
    
    Attributes:
        table: Fully qualified table name (e.g., "project.dataset.table")
        name: Column name
        
    Note:
        Column name comparisons are case-insensitive (matching ZetaSQL behavior),
        but table names are case-sensitive.
    """
    
    table: str
    name: str
    
    @staticmethod
    def from_resolved_column(column: ResolvedColumn) -> "ColumnEntity":
        """
        Create a ColumnEntity from a ResolvedColumn.
        
        Args:
            column: The ResolvedColumn to convert
            
        Returns:
            A new ColumnEntity instance
        """
        return ColumnEntity(table=column.table_name, name=column.name)
    
    def __eq__(self, other: object) -> bool:
        """
        Check equality with case-insensitive column name comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if both table and column name match (column name case-insensitive)
        """
        if not isinstance(other, ColumnEntity):
            return NotImplemented
        return (
            self.table == other.table
            and self.name.lower() == other.name.lower()
        )
    
    def __hash__(self) -> int:
        """
        Compute hash with case-insensitive column name.
        
        Returns:
            Hash value
        """
        return hash((self.table, self.name.lower()))
    
    def __str__(self) -> str:
        """
        String representation.
        
        Returns:
            "table.column" format
        """
        return f"{self.table}.{self.name}"


@dataclass(frozen=True)
class ColumnLineage:
    """
    Represents lineage for a single column.
    
    Maps a target (output) column to the set of parent (source) columns
    that contribute to its value.
    
    Attributes:
        target: The output column
        parents: Set of source columns that contribute to the target
                 (empty set means the column is computed from literals only)
    """
    
    target: ColumnEntity
    parents: Set[ColumnEntity]
    
    def __str__(self) -> str:
        """
        String representation.
        
        Returns:
            Multi-line string showing target and parents
        """
        lines = [str(self.target)]
        for parent in sorted(self.parents, key=str):
            lines.append(f"  <- {parent}")
        return "\n".join(lines)
