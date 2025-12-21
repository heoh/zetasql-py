from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResolvedSubqueryExprEnums(_message.Message):
    __slots__ = ()
    class SubqueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCALAR: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        ARRAY: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        EXISTS: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        IN: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        LIKE_ANY: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        LIKE_ALL: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        NOT_LIKE_ANY: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
        NOT_LIKE_ALL: _ClassVar[ResolvedSubqueryExprEnums.SubqueryType]
    SCALAR: ResolvedSubqueryExprEnums.SubqueryType
    ARRAY: ResolvedSubqueryExprEnums.SubqueryType
    EXISTS: ResolvedSubqueryExprEnums.SubqueryType
    IN: ResolvedSubqueryExprEnums.SubqueryType
    LIKE_ANY: ResolvedSubqueryExprEnums.SubqueryType
    LIKE_ALL: ResolvedSubqueryExprEnums.SubqueryType
    NOT_LIKE_ANY: ResolvedSubqueryExprEnums.SubqueryType
    NOT_LIKE_ALL: ResolvedSubqueryExprEnums.SubqueryType
    def __init__(self) -> None: ...

class ResolvedJoinScanEnums(_message.Message):
    __slots__ = ()
    class JoinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INNER: _ClassVar[ResolvedJoinScanEnums.JoinType]
        LEFT: _ClassVar[ResolvedJoinScanEnums.JoinType]
        RIGHT: _ClassVar[ResolvedJoinScanEnums.JoinType]
        FULL: _ClassVar[ResolvedJoinScanEnums.JoinType]
    INNER: ResolvedJoinScanEnums.JoinType
    LEFT: ResolvedJoinScanEnums.JoinType
    RIGHT: ResolvedJoinScanEnums.JoinType
    FULL: ResolvedJoinScanEnums.JoinType
    def __init__(self) -> None: ...

class ResolvedSetOperationScanEnums(_message.Message):
    __slots__ = ()
    class SetOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNION_ALL: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
        UNION_DISTINCT: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
        INTERSECT_ALL: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
        INTERSECT_DISTINCT: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
        EXCEPT_ALL: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
        EXCEPT_DISTINCT: _ClassVar[ResolvedSetOperationScanEnums.SetOperationType]
    UNION_ALL: ResolvedSetOperationScanEnums.SetOperationType
    UNION_DISTINCT: ResolvedSetOperationScanEnums.SetOperationType
    INTERSECT_ALL: ResolvedSetOperationScanEnums.SetOperationType
    INTERSECT_DISTINCT: ResolvedSetOperationScanEnums.SetOperationType
    EXCEPT_ALL: ResolvedSetOperationScanEnums.SetOperationType
    EXCEPT_DISTINCT: ResolvedSetOperationScanEnums.SetOperationType
    class SetOperationColumnMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BY_POSITION: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnMatchMode]
        CORRESPONDING: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnMatchMode]
        CORRESPONDING_BY: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnMatchMode]
    BY_POSITION: ResolvedSetOperationScanEnums.SetOperationColumnMatchMode
    CORRESPONDING: ResolvedSetOperationScanEnums.SetOperationColumnMatchMode
    CORRESPONDING_BY: ResolvedSetOperationScanEnums.SetOperationColumnMatchMode
    class SetOperationColumnPropagationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRICT: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode]
        INNER: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode]
        LEFT: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode]
        FULL: _ClassVar[ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode]
    STRICT: ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode
    INNER: ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode
    LEFT: ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode
    FULL: ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode
    def __init__(self) -> None: ...

class ResolvedRecursiveScanEnums(_message.Message):
    __slots__ = ()
    class RecursiveSetOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNION_ALL: _ClassVar[ResolvedRecursiveScanEnums.RecursiveSetOperationType]
        UNION_DISTINCT: _ClassVar[ResolvedRecursiveScanEnums.RecursiveSetOperationType]
    UNION_ALL: ResolvedRecursiveScanEnums.RecursiveSetOperationType
    UNION_DISTINCT: ResolvedRecursiveScanEnums.RecursiveSetOperationType
    def __init__(self) -> None: ...

class ResolvedSampleScanEnums(_message.Message):
    __slots__ = ()
    class SampleUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROWS: _ClassVar[ResolvedSampleScanEnums.SampleUnit]
        PERCENT: _ClassVar[ResolvedSampleScanEnums.SampleUnit]
    ROWS: ResolvedSampleScanEnums.SampleUnit
    PERCENT: ResolvedSampleScanEnums.SampleUnit
    def __init__(self) -> None: ...

class ResolvedOrderByItemEnums(_message.Message):
    __slots__ = ()
    class NullOrderMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_UNSPECIFIED: _ClassVar[ResolvedOrderByItemEnums.NullOrderMode]
        NULLS_FIRST: _ClassVar[ResolvedOrderByItemEnums.NullOrderMode]
        NULLS_LAST: _ClassVar[ResolvedOrderByItemEnums.NullOrderMode]
    ORDER_UNSPECIFIED: ResolvedOrderByItemEnums.NullOrderMode
    NULLS_FIRST: ResolvedOrderByItemEnums.NullOrderMode
    NULLS_LAST: ResolvedOrderByItemEnums.NullOrderMode
    def __init__(self) -> None: ...

class ResolvedCreateStatementEnums(_message.Message):
    __slots__ = ()
    class CreateScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATE_DEFAULT_SCOPE: _ClassVar[ResolvedCreateStatementEnums.CreateScope]
        CREATE_PRIVATE: _ClassVar[ResolvedCreateStatementEnums.CreateScope]
        CREATE_PUBLIC: _ClassVar[ResolvedCreateStatementEnums.CreateScope]
        CREATE_TEMP: _ClassVar[ResolvedCreateStatementEnums.CreateScope]
    CREATE_DEFAULT_SCOPE: ResolvedCreateStatementEnums.CreateScope
    CREATE_PRIVATE: ResolvedCreateStatementEnums.CreateScope
    CREATE_PUBLIC: ResolvedCreateStatementEnums.CreateScope
    CREATE_TEMP: ResolvedCreateStatementEnums.CreateScope
    class CreateMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATE_DEFAULT: _ClassVar[ResolvedCreateStatementEnums.CreateMode]
        CREATE_OR_REPLACE: _ClassVar[ResolvedCreateStatementEnums.CreateMode]
        CREATE_IF_NOT_EXISTS: _ClassVar[ResolvedCreateStatementEnums.CreateMode]
    CREATE_DEFAULT: ResolvedCreateStatementEnums.CreateMode
    CREATE_OR_REPLACE: ResolvedCreateStatementEnums.CreateMode
    CREATE_IF_NOT_EXISTS: ResolvedCreateStatementEnums.CreateMode
    class SqlSecurity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_SECURITY_UNSPECIFIED: _ClassVar[ResolvedCreateStatementEnums.SqlSecurity]
        SQL_SECURITY_DEFINER: _ClassVar[ResolvedCreateStatementEnums.SqlSecurity]
        SQL_SECURITY_INVOKER: _ClassVar[ResolvedCreateStatementEnums.SqlSecurity]
    SQL_SECURITY_UNSPECIFIED: ResolvedCreateStatementEnums.SqlSecurity
    SQL_SECURITY_DEFINER: ResolvedCreateStatementEnums.SqlSecurity
    SQL_SECURITY_INVOKER: ResolvedCreateStatementEnums.SqlSecurity
    class DeterminismLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETERMINISM_UNSPECIFIED: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
        DETERMINISM_DETERMINISTIC: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
        DETERMINISM_NOT_DETERMINISTIC: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
        DETERMINISM_IMMUTABLE: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
        DETERMINISM_STABLE: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
        DETERMINISM_VOLATILE: _ClassVar[ResolvedCreateStatementEnums.DeterminismLevel]
    DETERMINISM_UNSPECIFIED: ResolvedCreateStatementEnums.DeterminismLevel
    DETERMINISM_DETERMINISTIC: ResolvedCreateStatementEnums.DeterminismLevel
    DETERMINISM_NOT_DETERMINISTIC: ResolvedCreateStatementEnums.DeterminismLevel
    DETERMINISM_IMMUTABLE: ResolvedCreateStatementEnums.DeterminismLevel
    DETERMINISM_STABLE: ResolvedCreateStatementEnums.DeterminismLevel
    DETERMINISM_VOLATILE: ResolvedCreateStatementEnums.DeterminismLevel
    def __init__(self) -> None: ...

class ResolvedGeneratedColumnInfoEnums(_message.Message):
    __slots__ = ()
    class StoredMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NON_STORED: _ClassVar[ResolvedGeneratedColumnInfoEnums.StoredMode]
        STORED: _ClassVar[ResolvedGeneratedColumnInfoEnums.StoredMode]
        STORED_VOLATILE: _ClassVar[ResolvedGeneratedColumnInfoEnums.StoredMode]
    NON_STORED: ResolvedGeneratedColumnInfoEnums.StoredMode
    STORED: ResolvedGeneratedColumnInfoEnums.StoredMode
    STORED_VOLATILE: ResolvedGeneratedColumnInfoEnums.StoredMode
    class GeneratedMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALWAYS: _ClassVar[ResolvedGeneratedColumnInfoEnums.GeneratedMode]
        BY_DEFAULT: _ClassVar[ResolvedGeneratedColumnInfoEnums.GeneratedMode]
    ALWAYS: ResolvedGeneratedColumnInfoEnums.GeneratedMode
    BY_DEFAULT: ResolvedGeneratedColumnInfoEnums.GeneratedMode
    def __init__(self) -> None: ...

class ResolvedDropStmtEnums(_message.Message):
    __slots__ = ()
    class DropMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DROP_MODE_UNSPECIFIED: _ClassVar[ResolvedDropStmtEnums.DropMode]
        RESTRICT: _ClassVar[ResolvedDropStmtEnums.DropMode]
        CASCADE: _ClassVar[ResolvedDropStmtEnums.DropMode]
    DROP_MODE_UNSPECIFIED: ResolvedDropStmtEnums.DropMode
    RESTRICT: ResolvedDropStmtEnums.DropMode
    CASCADE: ResolvedDropStmtEnums.DropMode
    def __init__(self) -> None: ...

class ResolvedBeginStmtEnums(_message.Message):
    __slots__ = ()
    class ReadWriteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[ResolvedBeginStmtEnums.ReadWriteMode]
        MODE_READ_ONLY: _ClassVar[ResolvedBeginStmtEnums.ReadWriteMode]
        MODE_READ_WRITE: _ClassVar[ResolvedBeginStmtEnums.ReadWriteMode]
    MODE_UNSPECIFIED: ResolvedBeginStmtEnums.ReadWriteMode
    MODE_READ_ONLY: ResolvedBeginStmtEnums.ReadWriteMode
    MODE_READ_WRITE: ResolvedBeginStmtEnums.ReadWriteMode
    def __init__(self) -> None: ...

class ResolvedWindowFrameEnums(_message.Message):
    __slots__ = ()
    class FrameUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROWS: _ClassVar[ResolvedWindowFrameEnums.FrameUnit]
        RANGE: _ClassVar[ResolvedWindowFrameEnums.FrameUnit]
    ROWS: ResolvedWindowFrameEnums.FrameUnit
    RANGE: ResolvedWindowFrameEnums.FrameUnit
    def __init__(self) -> None: ...

class ResolvedWindowFrameExprEnums(_message.Message):
    __slots__ = ()
    class BoundaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNBOUNDED_PRECEDING: _ClassVar[ResolvedWindowFrameExprEnums.BoundaryType]
        OFFSET_PRECEDING: _ClassVar[ResolvedWindowFrameExprEnums.BoundaryType]
        CURRENT_ROW: _ClassVar[ResolvedWindowFrameExprEnums.BoundaryType]
        OFFSET_FOLLOWING: _ClassVar[ResolvedWindowFrameExprEnums.BoundaryType]
        UNBOUNDED_FOLLOWING: _ClassVar[ResolvedWindowFrameExprEnums.BoundaryType]
    UNBOUNDED_PRECEDING: ResolvedWindowFrameExprEnums.BoundaryType
    OFFSET_PRECEDING: ResolvedWindowFrameExprEnums.BoundaryType
    CURRENT_ROW: ResolvedWindowFrameExprEnums.BoundaryType
    OFFSET_FOLLOWING: ResolvedWindowFrameExprEnums.BoundaryType
    UNBOUNDED_FOLLOWING: ResolvedWindowFrameExprEnums.BoundaryType
    def __init__(self) -> None: ...

class ResolvedInsertStmtEnums(_message.Message):
    __slots__ = ()
    class InsertMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OR_ERROR: _ClassVar[ResolvedInsertStmtEnums.InsertMode]
        OR_IGNORE: _ClassVar[ResolvedInsertStmtEnums.InsertMode]
        OR_REPLACE: _ClassVar[ResolvedInsertStmtEnums.InsertMode]
        OR_UPDATE: _ClassVar[ResolvedInsertStmtEnums.InsertMode]
    OR_ERROR: ResolvedInsertStmtEnums.InsertMode
    OR_IGNORE: ResolvedInsertStmtEnums.InsertMode
    OR_REPLACE: ResolvedInsertStmtEnums.InsertMode
    OR_UPDATE: ResolvedInsertStmtEnums.InsertMode
    def __init__(self) -> None: ...

class ResolvedMergeWhenEnums(_message.Message):
    __slots__ = ()
    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCHED: _ClassVar[ResolvedMergeWhenEnums.MatchType]
        NOT_MATCHED_BY_SOURCE: _ClassVar[ResolvedMergeWhenEnums.MatchType]
        NOT_MATCHED_BY_TARGET: _ClassVar[ResolvedMergeWhenEnums.MatchType]
    MATCHED: ResolvedMergeWhenEnums.MatchType
    NOT_MATCHED_BY_SOURCE: ResolvedMergeWhenEnums.MatchType
    NOT_MATCHED_BY_TARGET: ResolvedMergeWhenEnums.MatchType
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSERT: _ClassVar[ResolvedMergeWhenEnums.ActionType]
        UPDATE: _ClassVar[ResolvedMergeWhenEnums.ActionType]
        DELETE: _ClassVar[ResolvedMergeWhenEnums.ActionType]
    INSERT: ResolvedMergeWhenEnums.ActionType
    UPDATE: ResolvedMergeWhenEnums.ActionType
    DELETE: ResolvedMergeWhenEnums.ActionType
    def __init__(self) -> None: ...

class ResolvedOnConflictClauseEnums(_message.Message):
    __slots__ = ()
    class ConflictAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTHING: _ClassVar[ResolvedOnConflictClauseEnums.ConflictAction]
        UPDATE: _ClassVar[ResolvedOnConflictClauseEnums.ConflictAction]
    NOTHING: ResolvedOnConflictClauseEnums.ConflictAction
    UPDATE: ResolvedOnConflictClauseEnums.ConflictAction
    def __init__(self) -> None: ...

class ResolvedArgumentDefEnums(_message.Message):
    __slots__ = ()
    class ArgumentKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCALAR: _ClassVar[ResolvedArgumentDefEnums.ArgumentKind]
        AGGREGATE: _ClassVar[ResolvedArgumentDefEnums.ArgumentKind]
        NOT_AGGREGATE: _ClassVar[ResolvedArgumentDefEnums.ArgumentKind]
    SCALAR: ResolvedArgumentDefEnums.ArgumentKind
    AGGREGATE: ResolvedArgumentDefEnums.ArgumentKind
    NOT_AGGREGATE: ResolvedArgumentDefEnums.ArgumentKind
    def __init__(self) -> None: ...

class ResolvedFunctionCallBaseEnums(_message.Message):
    __slots__ = ()
    class ErrorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_ERROR_MODE: _ClassVar[ResolvedFunctionCallBaseEnums.ErrorMode]
        SAFE_ERROR_MODE: _ClassVar[ResolvedFunctionCallBaseEnums.ErrorMode]
    DEFAULT_ERROR_MODE: ResolvedFunctionCallBaseEnums.ErrorMode
    SAFE_ERROR_MODE: ResolvedFunctionCallBaseEnums.ErrorMode
    def __init__(self) -> None: ...

class ResolvedNonScalarFunctionCallBaseEnums(_message.Message):
    __slots__ = ()
    class NullHandlingModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_NULL_HANDLING: _ClassVar[ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier]
        IGNORE_NULLS: _ClassVar[ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier]
        RESPECT_NULLS: _ClassVar[ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier]
    DEFAULT_NULL_HANDLING: ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier
    IGNORE_NULLS: ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier
    RESPECT_NULLS: ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier
    def __init__(self) -> None: ...

class ResolvedAggregateHavingModifierEnums(_message.Message):
    __slots__ = ()
    class HavingModifierKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[ResolvedAggregateHavingModifierEnums.HavingModifierKind]
        MAX: _ClassVar[ResolvedAggregateHavingModifierEnums.HavingModifierKind]
        MIN: _ClassVar[ResolvedAggregateHavingModifierEnums.HavingModifierKind]
    INVALID: ResolvedAggregateHavingModifierEnums.HavingModifierKind
    MAX: ResolvedAggregateHavingModifierEnums.HavingModifierKind
    MIN: ResolvedAggregateHavingModifierEnums.HavingModifierKind
    def __init__(self) -> None: ...

class ResolvedStatementEnums(_message.Message):
    __slots__ = ()
    class ObjectAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ResolvedStatementEnums.ObjectAccess]
        READ: _ClassVar[ResolvedStatementEnums.ObjectAccess]
        WRITE: _ClassVar[ResolvedStatementEnums.ObjectAccess]
        READ_WRITE: _ClassVar[ResolvedStatementEnums.ObjectAccess]
    NONE: ResolvedStatementEnums.ObjectAccess
    READ: ResolvedStatementEnums.ObjectAccess
    WRITE: ResolvedStatementEnums.ObjectAccess
    READ_WRITE: ResolvedStatementEnums.ObjectAccess
    def __init__(self) -> None: ...

class ResolvedImportStmtEnums(_message.Message):
    __slots__ = ()
    class ImportKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODULE: _ClassVar[ResolvedImportStmtEnums.ImportKind]
        PROTO: _ClassVar[ResolvedImportStmtEnums.ImportKind]
        __ImportKind__switch_must_have_a_default__: _ClassVar[ResolvedImportStmtEnums.ImportKind]
    MODULE: ResolvedImportStmtEnums.ImportKind
    PROTO: ResolvedImportStmtEnums.ImportKind
    __ImportKind__switch_must_have_a_default__: ResolvedImportStmtEnums.ImportKind
    def __init__(self) -> None: ...

class ResolvedForeignKeyEnums(_message.Message):
    __slots__ = ()
    class MatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIMPLE: _ClassVar[ResolvedForeignKeyEnums.MatchMode]
        FULL: _ClassVar[ResolvedForeignKeyEnums.MatchMode]
        NOT_DISTINCT: _ClassVar[ResolvedForeignKeyEnums.MatchMode]
    SIMPLE: ResolvedForeignKeyEnums.MatchMode
    FULL: ResolvedForeignKeyEnums.MatchMode
    NOT_DISTINCT: ResolvedForeignKeyEnums.MatchMode
    class ActionOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACTION: _ClassVar[ResolvedForeignKeyEnums.ActionOperation]
        RESTRICT: _ClassVar[ResolvedForeignKeyEnums.ActionOperation]
        CASCADE: _ClassVar[ResolvedForeignKeyEnums.ActionOperation]
        SET_NULL: _ClassVar[ResolvedForeignKeyEnums.ActionOperation]
    NO_ACTION: ResolvedForeignKeyEnums.ActionOperation
    RESTRICT: ResolvedForeignKeyEnums.ActionOperation
    CASCADE: ResolvedForeignKeyEnums.ActionOperation
    SET_NULL: ResolvedForeignKeyEnums.ActionOperation
    def __init__(self) -> None: ...

class ResolvedAuxLoadDataStmtEnums(_message.Message):
    __slots__ = ()
    class InsertionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ResolvedAuxLoadDataStmtEnums.InsertionMode]
        APPEND: _ClassVar[ResolvedAuxLoadDataStmtEnums.InsertionMode]
        OVERWRITE: _ClassVar[ResolvedAuxLoadDataStmtEnums.InsertionMode]
    NONE: ResolvedAuxLoadDataStmtEnums.InsertionMode
    APPEND: ResolvedAuxLoadDataStmtEnums.InsertionMode
    OVERWRITE: ResolvedAuxLoadDataStmtEnums.InsertionMode
    def __init__(self) -> None: ...

class ResolvedMatchRecognizeScanEnums(_message.Message):
    __slots__ = ()
    class AfterMatchSkipMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AFTER_MATCH_SKIP_MODE_UNSPECIFIED: _ClassVar[ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode]
        END_OF_MATCH: _ClassVar[ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode]
        NEXT_ROW: _ClassVar[ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode]
    AFTER_MATCH_SKIP_MODE_UNSPECIFIED: ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode
    END_OF_MATCH: ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode
    NEXT_ROW: ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode
    def __init__(self) -> None: ...

class ResolvedMatchRecognizePatternAnchorEnums(_message.Message):
    __slots__ = ()
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[ResolvedMatchRecognizePatternAnchorEnums.Mode]
        START: _ClassVar[ResolvedMatchRecognizePatternAnchorEnums.Mode]
        END: _ClassVar[ResolvedMatchRecognizePatternAnchorEnums.Mode]
    MODE_UNSPECIFIED: ResolvedMatchRecognizePatternAnchorEnums.Mode
    START: ResolvedMatchRecognizePatternAnchorEnums.Mode
    END: ResolvedMatchRecognizePatternAnchorEnums.Mode
    def __init__(self) -> None: ...

class ResolvedMatchRecognizePatternOperationEnums(_message.Message):
    __slots__ = ()
    class MatchRecognizePatternOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType]
        CONCAT: _ClassVar[ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType]
        ALTERNATE: _ClassVar[ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType]
    OPERATION_TYPE_UNSPECIFIED: ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType
    CONCAT: ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType
    ALTERNATE: ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType
    def __init__(self) -> None: ...

class ResolvedGraphLabelNaryExprEnums(_message.Message):
    __slots__ = ()
    class GraphLogicalOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType]
        NOT: _ClassVar[ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType]
        AND: _ClassVar[ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType]
        OR: _ClassVar[ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType]
    OPERATION_TYPE_UNSPECIFIED: ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType
    NOT: ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType
    AND: ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType
    OR: ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType
    def __init__(self) -> None: ...

class ResolvedGraphEdgeScanEnums(_message.Message):
    __slots__ = ()
    class EdgeOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[ResolvedGraphEdgeScanEnums.EdgeOrientation]
        LEFT: _ClassVar[ResolvedGraphEdgeScanEnums.EdgeOrientation]
        RIGHT: _ClassVar[ResolvedGraphEdgeScanEnums.EdgeOrientation]
    ANY: ResolvedGraphEdgeScanEnums.EdgeOrientation
    LEFT: ResolvedGraphEdgeScanEnums.EdgeOrientation
    RIGHT: ResolvedGraphEdgeScanEnums.EdgeOrientation
    def __init__(self) -> None: ...

class ResolvedGraphPathModeEnums(_message.Message):
    __slots__ = ()
    class PathMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATH_MODE_UNSPECIFIED: _ClassVar[ResolvedGraphPathModeEnums.PathMode]
        WALK: _ClassVar[ResolvedGraphPathModeEnums.PathMode]
        TRAIL: _ClassVar[ResolvedGraphPathModeEnums.PathMode]
        SIMPLE: _ClassVar[ResolvedGraphPathModeEnums.PathMode]
        ACYCLIC: _ClassVar[ResolvedGraphPathModeEnums.PathMode]
    PATH_MODE_UNSPECIFIED: ResolvedGraphPathModeEnums.PathMode
    WALK: ResolvedGraphPathModeEnums.PathMode
    TRAIL: ResolvedGraphPathModeEnums.PathMode
    SIMPLE: ResolvedGraphPathModeEnums.PathMode
    ACYCLIC: ResolvedGraphPathModeEnums.PathMode
    def __init__(self) -> None: ...

class ResolvedGraphPathSearchPrefixEnums(_message.Message):
    __slots__ = ()
    class PathSearchPrefixType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATH_SEARCH_PREFIX_TYPE_UNSPECIFIED: _ClassVar[ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType]
        ANY: _ClassVar[ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType]
        SHORTEST: _ClassVar[ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType]
        CHEAPEST: _ClassVar[ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType]
    PATH_SEARCH_PREFIX_TYPE_UNSPECIFIED: ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType
    ANY: ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType
    SHORTEST: ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType
    CHEAPEST: ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType
    def __init__(self) -> None: ...

class ResolvedDropIndexStmtEnums(_message.Message):
    __slots__ = ()
    class IndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_DEFAULT: _ClassVar[ResolvedDropIndexStmtEnums.IndexType]
        INDEX_SEARCH: _ClassVar[ResolvedDropIndexStmtEnums.IndexType]
        INDEX_VECTOR: _ClassVar[ResolvedDropIndexStmtEnums.IndexType]
    INDEX_DEFAULT: ResolvedDropIndexStmtEnums.IndexType
    INDEX_SEARCH: ResolvedDropIndexStmtEnums.IndexType
    INDEX_VECTOR: ResolvedDropIndexStmtEnums.IndexType
    def __init__(self) -> None: ...

class ResolvedOptionEnums(_message.Message):
    __slots__ = ()
    class AssignmentOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_ASSIGN: _ClassVar[ResolvedOptionEnums.AssignmentOp]
        ADD_ASSIGN: _ClassVar[ResolvedOptionEnums.AssignmentOp]
        SUB_ASSIGN: _ClassVar[ResolvedOptionEnums.AssignmentOp]
    DEFAULT_ASSIGN: ResolvedOptionEnums.AssignmentOp
    ADD_ASSIGN: ResolvedOptionEnums.AssignmentOp
    SUB_ASSIGN: ResolvedOptionEnums.AssignmentOp
    def __init__(self) -> None: ...

class ResolvedLockModeEnums(_message.Message):
    __slots__ = ()
    class LockStrengthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE: _ClassVar[ResolvedLockModeEnums.LockStrengthType]
    UPDATE: ResolvedLockModeEnums.LockStrengthType
    def __init__(self) -> None: ...

class ResolvedAlterIndexStmtEnums(_message.Message):
    __slots__ = ()
    class AlterIndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_DEFAULT: _ClassVar[ResolvedAlterIndexStmtEnums.AlterIndexType]
        INDEX_SEARCH: _ClassVar[ResolvedAlterIndexStmtEnums.AlterIndexType]
        INDEX_VECTOR: _ClassVar[ResolvedAlterIndexStmtEnums.AlterIndexType]
    INDEX_DEFAULT: ResolvedAlterIndexStmtEnums.AlterIndexType
    INDEX_SEARCH: ResolvedAlterIndexStmtEnums.AlterIndexType
    INDEX_VECTOR: ResolvedAlterIndexStmtEnums.AlterIndexType
    def __init__(self) -> None: ...

class ResolvedUpdateFieldItemEnums(_message.Message):
    __slots__ = ()
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE_SINGLE: _ClassVar[ResolvedUpdateFieldItemEnums.Operation]
        UPDATE_MANY: _ClassVar[ResolvedUpdateFieldItemEnums.Operation]
        UPDATE_SINGLE_NO_CREATION: _ClassVar[ResolvedUpdateFieldItemEnums.Operation]
    UPDATE_SINGLE: ResolvedUpdateFieldItemEnums.Operation
    UPDATE_MANY: ResolvedUpdateFieldItemEnums.Operation
    UPDATE_SINGLE_NO_CREATION: ResolvedUpdateFieldItemEnums.Operation
    def __init__(self) -> None: ...
