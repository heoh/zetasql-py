from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaObjectKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    __SchemaObjectKind__switch_must_have_a_default__: _ClassVar[SchemaObjectKind]
    kInvalidSchemaObjectKind: _ClassVar[SchemaObjectKind]
    kAggregateFunction: _ClassVar[SchemaObjectKind]
    kApproxView: _ClassVar[SchemaObjectKind]
    kConnection: _ClassVar[SchemaObjectKind]
    kConstant: _ClassVar[SchemaObjectKind]
    kDatabase: _ClassVar[SchemaObjectKind]
    kExternalTable: _ClassVar[SchemaObjectKind]
    kFunction: _ClassVar[SchemaObjectKind]
    kIndex: _ClassVar[SchemaObjectKind]
    kMaterializedView: _ClassVar[SchemaObjectKind]
    kModel: _ClassVar[SchemaObjectKind]
    kProcedure: _ClassVar[SchemaObjectKind]
    kSchema: _ClassVar[SchemaObjectKind]
    kTable: _ClassVar[SchemaObjectKind]
    kTableFunction: _ClassVar[SchemaObjectKind]
    kView: _ClassVar[SchemaObjectKind]
    kSnapshotTable: _ClassVar[SchemaObjectKind]
    kPropertyGraph: _ClassVar[SchemaObjectKind]
    kExternalSchema: _ClassVar[SchemaObjectKind]
    kSequence: _ClassVar[SchemaObjectKind]
__SchemaObjectKind__switch_must_have_a_default__: SchemaObjectKind
kInvalidSchemaObjectKind: SchemaObjectKind
kAggregateFunction: SchemaObjectKind
kApproxView: SchemaObjectKind
kConnection: SchemaObjectKind
kConstant: SchemaObjectKind
kDatabase: SchemaObjectKind
kExternalTable: SchemaObjectKind
kFunction: SchemaObjectKind
kIndex: SchemaObjectKind
kMaterializedView: SchemaObjectKind
kModel: SchemaObjectKind
kProcedure: SchemaObjectKind
kSchema: SchemaObjectKind
kTable: SchemaObjectKind
kTableFunction: SchemaObjectKind
kView: SchemaObjectKind
kSnapshotTable: SchemaObjectKind
kPropertyGraph: SchemaObjectKind
kExternalSchema: SchemaObjectKind
kSequence: SchemaObjectKind

class ASTBinaryExpressionEnums(_message.Message):
    __slots__ = ()
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTBinaryExpressionEnums.Op]
        LIKE: _ClassVar[ASTBinaryExpressionEnums.Op]
        IS: _ClassVar[ASTBinaryExpressionEnums.Op]
        EQ: _ClassVar[ASTBinaryExpressionEnums.Op]
        NE: _ClassVar[ASTBinaryExpressionEnums.Op]
        NE2: _ClassVar[ASTBinaryExpressionEnums.Op]
        GT: _ClassVar[ASTBinaryExpressionEnums.Op]
        LT: _ClassVar[ASTBinaryExpressionEnums.Op]
        GE: _ClassVar[ASTBinaryExpressionEnums.Op]
        LE: _ClassVar[ASTBinaryExpressionEnums.Op]
        BITWISE_OR: _ClassVar[ASTBinaryExpressionEnums.Op]
        BITWISE_XOR: _ClassVar[ASTBinaryExpressionEnums.Op]
        BITWISE_AND: _ClassVar[ASTBinaryExpressionEnums.Op]
        PLUS: _ClassVar[ASTBinaryExpressionEnums.Op]
        MINUS: _ClassVar[ASTBinaryExpressionEnums.Op]
        MULTIPLY: _ClassVar[ASTBinaryExpressionEnums.Op]
        DIVIDE: _ClassVar[ASTBinaryExpressionEnums.Op]
        CONCAT_OP: _ClassVar[ASTBinaryExpressionEnums.Op]
        DISTINCT: _ClassVar[ASTBinaryExpressionEnums.Op]
        IS_SOURCE_NODE: _ClassVar[ASTBinaryExpressionEnums.Op]
        IS_DEST_NODE: _ClassVar[ASTBinaryExpressionEnums.Op]
    NOT_SET: ASTBinaryExpressionEnums.Op
    LIKE: ASTBinaryExpressionEnums.Op
    IS: ASTBinaryExpressionEnums.Op
    EQ: ASTBinaryExpressionEnums.Op
    NE: ASTBinaryExpressionEnums.Op
    NE2: ASTBinaryExpressionEnums.Op
    GT: ASTBinaryExpressionEnums.Op
    LT: ASTBinaryExpressionEnums.Op
    GE: ASTBinaryExpressionEnums.Op
    LE: ASTBinaryExpressionEnums.Op
    BITWISE_OR: ASTBinaryExpressionEnums.Op
    BITWISE_XOR: ASTBinaryExpressionEnums.Op
    BITWISE_AND: ASTBinaryExpressionEnums.Op
    PLUS: ASTBinaryExpressionEnums.Op
    MINUS: ASTBinaryExpressionEnums.Op
    MULTIPLY: ASTBinaryExpressionEnums.Op
    DIVIDE: ASTBinaryExpressionEnums.Op
    CONCAT_OP: ASTBinaryExpressionEnums.Op
    DISTINCT: ASTBinaryExpressionEnums.Op
    IS_SOURCE_NODE: ASTBinaryExpressionEnums.Op
    IS_DEST_NODE: ASTBinaryExpressionEnums.Op
    def __init__(self) -> None: ...

class ASTOptionsEntryEnums(_message.Message):
    __slots__ = ()
    class AssignmentOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTOptionsEntryEnums.AssignmentOp]
        ASSIGN: _ClassVar[ASTOptionsEntryEnums.AssignmentOp]
        ADD_ASSIGN: _ClassVar[ASTOptionsEntryEnums.AssignmentOp]
        SUB_ASSIGN: _ClassVar[ASTOptionsEntryEnums.AssignmentOp]
    NOT_SET: ASTOptionsEntryEnums.AssignmentOp
    ASSIGN: ASTOptionsEntryEnums.AssignmentOp
    ADD_ASSIGN: ASTOptionsEntryEnums.AssignmentOp
    SUB_ASSIGN: ASTOptionsEntryEnums.AssignmentOp
    def __init__(self) -> None: ...

class ASTOrderingExpressionEnums(_message.Message):
    __slots__ = ()
    class OrderingSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTOrderingExpressionEnums.OrderingSpec]
        ASC: _ClassVar[ASTOrderingExpressionEnums.OrderingSpec]
        DESC: _ClassVar[ASTOrderingExpressionEnums.OrderingSpec]
        UNSPECIFIED: _ClassVar[ASTOrderingExpressionEnums.OrderingSpec]
    NOT_SET: ASTOrderingExpressionEnums.OrderingSpec
    ASC: ASTOrderingExpressionEnums.OrderingSpec
    DESC: ASTOrderingExpressionEnums.OrderingSpec
    UNSPECIFIED: ASTOrderingExpressionEnums.OrderingSpec
    def __init__(self) -> None: ...

class ASTJoinEnums(_message.Message):
    __slots__ = ()
    class JoinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_JOIN_TYPE: _ClassVar[ASTJoinEnums.JoinType]
        COMMA: _ClassVar[ASTJoinEnums.JoinType]
        CROSS: _ClassVar[ASTJoinEnums.JoinType]
        FULL: _ClassVar[ASTJoinEnums.JoinType]
        INNER: _ClassVar[ASTJoinEnums.JoinType]
        LEFT: _ClassVar[ASTJoinEnums.JoinType]
        RIGHT: _ClassVar[ASTJoinEnums.JoinType]
    DEFAULT_JOIN_TYPE: ASTJoinEnums.JoinType
    COMMA: ASTJoinEnums.JoinType
    CROSS: ASTJoinEnums.JoinType
    FULL: ASTJoinEnums.JoinType
    INNER: ASTJoinEnums.JoinType
    LEFT: ASTJoinEnums.JoinType
    RIGHT: ASTJoinEnums.JoinType
    class JoinHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_JOIN_HINT: _ClassVar[ASTJoinEnums.JoinHint]
        HASH: _ClassVar[ASTJoinEnums.JoinHint]
        LOOKUP: _ClassVar[ASTJoinEnums.JoinHint]
    NO_JOIN_HINT: ASTJoinEnums.JoinHint
    HASH: ASTJoinEnums.JoinHint
    LOOKUP: ASTJoinEnums.JoinHint
    def __init__(self) -> None: ...

class ASTSelectAsEnums(_message.Message):
    __slots__ = ()
    class AsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTSelectAsEnums.AsMode]
        STRUCT: _ClassVar[ASTSelectAsEnums.AsMode]
        VALUE: _ClassVar[ASTSelectAsEnums.AsMode]
        TYPE_NAME: _ClassVar[ASTSelectAsEnums.AsMode]
    NOT_SET: ASTSelectAsEnums.AsMode
    STRUCT: ASTSelectAsEnums.AsMode
    VALUE: ASTSelectAsEnums.AsMode
    TYPE_NAME: ASTSelectAsEnums.AsMode
    def __init__(self) -> None: ...

class ASTFunctionCallEnums(_message.Message):
    __slots__ = ()
    class NullHandlingModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_NULL_HANDLING: _ClassVar[ASTFunctionCallEnums.NullHandlingModifier]
        IGNORE_NULLS: _ClassVar[ASTFunctionCallEnums.NullHandlingModifier]
        RESPECT_NULLS: _ClassVar[ASTFunctionCallEnums.NullHandlingModifier]
    DEFAULT_NULL_HANDLING: ASTFunctionCallEnums.NullHandlingModifier
    IGNORE_NULLS: ASTFunctionCallEnums.NullHandlingModifier
    RESPECT_NULLS: ASTFunctionCallEnums.NullHandlingModifier
    def __init__(self) -> None: ...

class ASTExpressionSubqueryEnums(_message.Message):
    __slots__ = ()
    class Modifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ASTExpressionSubqueryEnums.Modifier]
        ARRAY: _ClassVar[ASTExpressionSubqueryEnums.Modifier]
        EXISTS: _ClassVar[ASTExpressionSubqueryEnums.Modifier]
        VALUE: _ClassVar[ASTExpressionSubqueryEnums.Modifier]
    NONE: ASTExpressionSubqueryEnums.Modifier
    ARRAY: ASTExpressionSubqueryEnums.Modifier
    EXISTS: ASTExpressionSubqueryEnums.Modifier
    VALUE: ASTExpressionSubqueryEnums.Modifier
    def __init__(self) -> None: ...

class ASTHavingModifierEnums(_message.Message):
    __slots__ = ()
    class ModifierKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTHavingModifierEnums.ModifierKind]
        MIN: _ClassVar[ASTHavingModifierEnums.ModifierKind]
        MAX: _ClassVar[ASTHavingModifierEnums.ModifierKind]
    NOT_SET: ASTHavingModifierEnums.ModifierKind
    MIN: ASTHavingModifierEnums.ModifierKind
    MAX: ASTHavingModifierEnums.ModifierKind
    def __init__(self) -> None: ...

class ASTSetOperationEnums(_message.Message):
    __slots__ = ()
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTSetOperationEnums.OperationType]
        UNION: _ClassVar[ASTSetOperationEnums.OperationType]
        EXCEPT: _ClassVar[ASTSetOperationEnums.OperationType]
        INTERSECT: _ClassVar[ASTSetOperationEnums.OperationType]
    NOT_SET: ASTSetOperationEnums.OperationType
    UNION: ASTSetOperationEnums.OperationType
    EXCEPT: ASTSetOperationEnums.OperationType
    INTERSECT: ASTSetOperationEnums.OperationType
    class AllOrDistinct(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL_OR_DISTINCT_NOT_SET: _ClassVar[ASTSetOperationEnums.AllOrDistinct]
        ALL: _ClassVar[ASTSetOperationEnums.AllOrDistinct]
        DISTINCT: _ClassVar[ASTSetOperationEnums.AllOrDistinct]
    ALL_OR_DISTINCT_NOT_SET: ASTSetOperationEnums.AllOrDistinct
    ALL: ASTSetOperationEnums.AllOrDistinct
    DISTINCT: ASTSetOperationEnums.AllOrDistinct
    class ColumnMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BY_POSITION: _ClassVar[ASTSetOperationEnums.ColumnMatchMode]
        CORRESPONDING: _ClassVar[ASTSetOperationEnums.ColumnMatchMode]
        CORRESPONDING_BY: _ClassVar[ASTSetOperationEnums.ColumnMatchMode]
        BY_NAME: _ClassVar[ASTSetOperationEnums.ColumnMatchMode]
        BY_NAME_ON: _ClassVar[ASTSetOperationEnums.ColumnMatchMode]
    BY_POSITION: ASTSetOperationEnums.ColumnMatchMode
    CORRESPONDING: ASTSetOperationEnums.ColumnMatchMode
    CORRESPONDING_BY: ASTSetOperationEnums.ColumnMatchMode
    BY_NAME: ASTSetOperationEnums.ColumnMatchMode
    BY_NAME_ON: ASTSetOperationEnums.ColumnMatchMode
    class ColumnPropagationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRICT: _ClassVar[ASTSetOperationEnums.ColumnPropagationMode]
        INNER: _ClassVar[ASTSetOperationEnums.ColumnPropagationMode]
        LEFT: _ClassVar[ASTSetOperationEnums.ColumnPropagationMode]
        FULL: _ClassVar[ASTSetOperationEnums.ColumnPropagationMode]
    STRICT: ASTSetOperationEnums.ColumnPropagationMode
    INNER: ASTSetOperationEnums.ColumnPropagationMode
    LEFT: ASTSetOperationEnums.ColumnPropagationMode
    FULL: ASTSetOperationEnums.ColumnPropagationMode
    def __init__(self) -> None: ...

class ASTUnaryExpressionEnums(_message.Message):
    __slots__ = ()
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTUnaryExpressionEnums.Op]
        NOT: _ClassVar[ASTUnaryExpressionEnums.Op]
        BITWISE_NOT: _ClassVar[ASTUnaryExpressionEnums.Op]
        MINUS: _ClassVar[ASTUnaryExpressionEnums.Op]
        PLUS: _ClassVar[ASTUnaryExpressionEnums.Op]
        IS_UNKNOWN: _ClassVar[ASTUnaryExpressionEnums.Op]
        IS_NOT_UNKNOWN: _ClassVar[ASTUnaryExpressionEnums.Op]
    NOT_SET: ASTUnaryExpressionEnums.Op
    NOT: ASTUnaryExpressionEnums.Op
    BITWISE_NOT: ASTUnaryExpressionEnums.Op
    MINUS: ASTUnaryExpressionEnums.Op
    PLUS: ASTUnaryExpressionEnums.Op
    IS_UNKNOWN: ASTUnaryExpressionEnums.Op
    IS_NOT_UNKNOWN: ASTUnaryExpressionEnums.Op
    def __init__(self) -> None: ...

class ASTWindowFrameEnums(_message.Message):
    __slots__ = ()
    class FrameUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROWS: _ClassVar[ASTWindowFrameEnums.FrameUnit]
        RANGE: _ClassVar[ASTWindowFrameEnums.FrameUnit]
    ROWS: ASTWindowFrameEnums.FrameUnit
    RANGE: ASTWindowFrameEnums.FrameUnit
    def __init__(self) -> None: ...

class ASTWindowFrameExprEnums(_message.Message):
    __slots__ = ()
    class BoundaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNBOUNDED_PRECEDING: _ClassVar[ASTWindowFrameExprEnums.BoundaryType]
        OFFSET_PRECEDING: _ClassVar[ASTWindowFrameExprEnums.BoundaryType]
        CURRENT_ROW: _ClassVar[ASTWindowFrameExprEnums.BoundaryType]
        OFFSET_FOLLOWING: _ClassVar[ASTWindowFrameExprEnums.BoundaryType]
        UNBOUNDED_FOLLOWING: _ClassVar[ASTWindowFrameExprEnums.BoundaryType]
    UNBOUNDED_PRECEDING: ASTWindowFrameExprEnums.BoundaryType
    OFFSET_PRECEDING: ASTWindowFrameExprEnums.BoundaryType
    CURRENT_ROW: ASTWindowFrameExprEnums.BoundaryType
    OFFSET_FOLLOWING: ASTWindowFrameExprEnums.BoundaryType
    UNBOUNDED_FOLLOWING: ASTWindowFrameExprEnums.BoundaryType
    def __init__(self) -> None: ...

class ASTAnySomeAllOpEnums(_message.Message):
    __slots__ = ()
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUninitialized: _ClassVar[ASTAnySomeAllOpEnums.Op]
        kAny: _ClassVar[ASTAnySomeAllOpEnums.Op]
        kSome: _ClassVar[ASTAnySomeAllOpEnums.Op]
        kAll: _ClassVar[ASTAnySomeAllOpEnums.Op]
    kUninitialized: ASTAnySomeAllOpEnums.Op
    kAny: ASTAnySomeAllOpEnums.Op
    kSome: ASTAnySomeAllOpEnums.Op
    kAll: ASTAnySomeAllOpEnums.Op
    def __init__(self) -> None: ...

class ASTTransactionReadWriteModeEnums(_message.Message):
    __slots__ = ()
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[ASTTransactionReadWriteModeEnums.Mode]
        READ_ONLY: _ClassVar[ASTTransactionReadWriteModeEnums.Mode]
        READ_WRITE: _ClassVar[ASTTransactionReadWriteModeEnums.Mode]
    INVALID: ASTTransactionReadWriteModeEnums.Mode
    READ_ONLY: ASTTransactionReadWriteModeEnums.Mode
    READ_WRITE: ASTTransactionReadWriteModeEnums.Mode
    def __init__(self) -> None: ...

class ASTImportStatementEnums(_message.Message):
    __slots__ = ()
    class ImportKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODULE: _ClassVar[ASTImportStatementEnums.ImportKind]
        PROTO: _ClassVar[ASTImportStatementEnums.ImportKind]
    MODULE: ASTImportStatementEnums.ImportKind
    PROTO: ASTImportStatementEnums.ImportKind
    def __init__(self) -> None: ...

class ASTUnpivotClauseEnums(_message.Message):
    __slots__ = ()
    class NullFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnspecified: _ClassVar[ASTUnpivotClauseEnums.NullFilter]
        kInclude: _ClassVar[ASTUnpivotClauseEnums.NullFilter]
        kExclude: _ClassVar[ASTUnpivotClauseEnums.NullFilter]
    kUnspecified: ASTUnpivotClauseEnums.NullFilter
    kInclude: ASTUnpivotClauseEnums.NullFilter
    kExclude: ASTUnpivotClauseEnums.NullFilter
    def __init__(self) -> None: ...

class ASTCreateStatementEnums(_message.Message):
    __slots__ = ()
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_SCOPE: _ClassVar[ASTCreateStatementEnums.Scope]
        PRIVATE: _ClassVar[ASTCreateStatementEnums.Scope]
        PUBLIC: _ClassVar[ASTCreateStatementEnums.Scope]
        TEMPORARY: _ClassVar[ASTCreateStatementEnums.Scope]
    DEFAULT_SCOPE: ASTCreateStatementEnums.Scope
    PRIVATE: ASTCreateStatementEnums.Scope
    PUBLIC: ASTCreateStatementEnums.Scope
    TEMPORARY: ASTCreateStatementEnums.Scope
    class SqlSecurity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_SECURITY_UNSPECIFIED: _ClassVar[ASTCreateStatementEnums.SqlSecurity]
        SQL_SECURITY_DEFINER: _ClassVar[ASTCreateStatementEnums.SqlSecurity]
        SQL_SECURITY_INVOKER: _ClassVar[ASTCreateStatementEnums.SqlSecurity]
    SQL_SECURITY_UNSPECIFIED: ASTCreateStatementEnums.SqlSecurity
    SQL_SECURITY_DEFINER: ASTCreateStatementEnums.SqlSecurity
    SQL_SECURITY_INVOKER: ASTCreateStatementEnums.SqlSecurity
    def __init__(self) -> None: ...

class ASTFunctionParameterEnums(_message.Message):
    __slots__ = ()
    class ProcedureParameterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTFunctionParameterEnums.ProcedureParameterMode]
        IN: _ClassVar[ASTFunctionParameterEnums.ProcedureParameterMode]
        OUT: _ClassVar[ASTFunctionParameterEnums.ProcedureParameterMode]
        INOUT: _ClassVar[ASTFunctionParameterEnums.ProcedureParameterMode]
    NOT_SET: ASTFunctionParameterEnums.ProcedureParameterMode
    IN: ASTFunctionParameterEnums.ProcedureParameterMode
    OUT: ASTFunctionParameterEnums.ProcedureParameterMode
    INOUT: ASTFunctionParameterEnums.ProcedureParameterMode
    def __init__(self) -> None: ...

class ASTTemplatedParameterTypeEnums(_message.Message):
    __slots__ = ()
    class TemplatedTypeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNINITIALIZED: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_TYPE: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_PROTO: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_ENUM: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_STRUCT: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_ARRAY: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
        ANY_TABLE: _ClassVar[ASTTemplatedParameterTypeEnums.TemplatedTypeKind]
    UNINITIALIZED: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_TYPE: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_PROTO: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_ENUM: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_STRUCT: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_ARRAY: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    ANY_TABLE: ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    def __init__(self) -> None: ...

class ASTGeneratedColumnInfoEnums(_message.Message):
    __slots__ = ()
    class StoredMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NON_STORED: _ClassVar[ASTGeneratedColumnInfoEnums.StoredMode]
        STORED: _ClassVar[ASTGeneratedColumnInfoEnums.StoredMode]
        STORED_VOLATILE: _ClassVar[ASTGeneratedColumnInfoEnums.StoredMode]
    NON_STORED: ASTGeneratedColumnInfoEnums.StoredMode
    STORED: ASTGeneratedColumnInfoEnums.StoredMode
    STORED_VOLATILE: ASTGeneratedColumnInfoEnums.StoredMode
    class GeneratedMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALWAYS: _ClassVar[ASTGeneratedColumnInfoEnums.GeneratedMode]
        BY_DEFAULT: _ClassVar[ASTGeneratedColumnInfoEnums.GeneratedMode]
    ALWAYS: ASTGeneratedColumnInfoEnums.GeneratedMode
    BY_DEFAULT: ASTGeneratedColumnInfoEnums.GeneratedMode
    def __init__(self) -> None: ...

class ASTColumnPositionEnums(_message.Message):
    __slots__ = ()
    class RelativePositionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRECEDING: _ClassVar[ASTColumnPositionEnums.RelativePositionType]
        FOLLOWING: _ClassVar[ASTColumnPositionEnums.RelativePositionType]
    PRECEDING: ASTColumnPositionEnums.RelativePositionType
    FOLLOWING: ASTColumnPositionEnums.RelativePositionType
    def __init__(self) -> None: ...

class ASTInsertStatementEnums(_message.Message):
    __slots__ = ()
    class InsertMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_MODE: _ClassVar[ASTInsertStatementEnums.InsertMode]
        REPLACE: _ClassVar[ASTInsertStatementEnums.InsertMode]
        UPDATE: _ClassVar[ASTInsertStatementEnums.InsertMode]
        IGNORE: _ClassVar[ASTInsertStatementEnums.InsertMode]
    DEFAULT_MODE: ASTInsertStatementEnums.InsertMode
    REPLACE: ASTInsertStatementEnums.InsertMode
    UPDATE: ASTInsertStatementEnums.InsertMode
    IGNORE: ASTInsertStatementEnums.InsertMode
    class ParseProgress(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInitial: _ClassVar[ASTInsertStatementEnums.ParseProgress]
        kSeenOrIgnoreReplaceUpdate: _ClassVar[ASTInsertStatementEnums.ParseProgress]
        kSeenTargetPath: _ClassVar[ASTInsertStatementEnums.ParseProgress]
        kSeenColumnList: _ClassVar[ASTInsertStatementEnums.ParseProgress]
        kSeenValuesList: _ClassVar[ASTInsertStatementEnums.ParseProgress]
    kInitial: ASTInsertStatementEnums.ParseProgress
    kSeenOrIgnoreReplaceUpdate: ASTInsertStatementEnums.ParseProgress
    kSeenTargetPath: ASTInsertStatementEnums.ParseProgress
    kSeenColumnList: ASTInsertStatementEnums.ParseProgress
    kSeenValuesList: ASTInsertStatementEnums.ParseProgress
    def __init__(self) -> None: ...

class ASTOnConflictClauseEnums(_message.Message):
    __slots__ = ()
    class ConflictAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTOnConflictClauseEnums.ConflictAction]
        NOTHING: _ClassVar[ASTOnConflictClauseEnums.ConflictAction]
        UPDATE: _ClassVar[ASTOnConflictClauseEnums.ConflictAction]
    NOT_SET: ASTOnConflictClauseEnums.ConflictAction
    NOTHING: ASTOnConflictClauseEnums.ConflictAction
    UPDATE: ASTOnConflictClauseEnums.ConflictAction
    def __init__(self) -> None: ...

class ASTMergeActionEnums(_message.Message):
    __slots__ = ()
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTMergeActionEnums.ActionType]
        INSERT: _ClassVar[ASTMergeActionEnums.ActionType]
        UPDATE: _ClassVar[ASTMergeActionEnums.ActionType]
        DELETE: _ClassVar[ASTMergeActionEnums.ActionType]
    NOT_SET: ASTMergeActionEnums.ActionType
    INSERT: ASTMergeActionEnums.ActionType
    UPDATE: ASTMergeActionEnums.ActionType
    DELETE: ASTMergeActionEnums.ActionType
    def __init__(self) -> None: ...

class ASTMergeWhenClauseEnums(_message.Message):
    __slots__ = ()
    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTMergeWhenClauseEnums.MatchType]
        MATCHED: _ClassVar[ASTMergeWhenClauseEnums.MatchType]
        NOT_MATCHED_BY_SOURCE: _ClassVar[ASTMergeWhenClauseEnums.MatchType]
        NOT_MATCHED_BY_TARGET: _ClassVar[ASTMergeWhenClauseEnums.MatchType]
    NOT_SET: ASTMergeWhenClauseEnums.MatchType
    MATCHED: ASTMergeWhenClauseEnums.MatchType
    NOT_MATCHED_BY_SOURCE: ASTMergeWhenClauseEnums.MatchType
    NOT_MATCHED_BY_TARGET: ASTMergeWhenClauseEnums.MatchType
    def __init__(self) -> None: ...

class ASTFilterFieldsArgEnums(_message.Message):
    __slots__ = ()
    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTFilterFieldsArgEnums.FilterType]
        INCLUDE: _ClassVar[ASTFilterFieldsArgEnums.FilterType]
        EXCLUDE: _ClassVar[ASTFilterFieldsArgEnums.FilterType]
    NOT_SET: ASTFilterFieldsArgEnums.FilterType
    INCLUDE: ASTFilterFieldsArgEnums.FilterType
    EXCLUDE: ASTFilterFieldsArgEnums.FilterType
    def __init__(self) -> None: ...

class ASTSampleSizeEnums(_message.Message):
    __slots__ = ()
    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTSampleSizeEnums.Unit]
        ROWS: _ClassVar[ASTSampleSizeEnums.Unit]
        PERCENT: _ClassVar[ASTSampleSizeEnums.Unit]
    NOT_SET: ASTSampleSizeEnums.Unit
    ROWS: ASTSampleSizeEnums.Unit
    PERCENT: ASTSampleSizeEnums.Unit
    def __init__(self) -> None: ...

class ASTForeignKeyActionsEnums(_message.Message):
    __slots__ = ()
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACTION: _ClassVar[ASTForeignKeyActionsEnums.Action]
        RESTRICT: _ClassVar[ASTForeignKeyActionsEnums.Action]
        CASCADE: _ClassVar[ASTForeignKeyActionsEnums.Action]
        SET_NULL: _ClassVar[ASTForeignKeyActionsEnums.Action]
    NO_ACTION: ASTForeignKeyActionsEnums.Action
    RESTRICT: ASTForeignKeyActionsEnums.Action
    CASCADE: ASTForeignKeyActionsEnums.Action
    SET_NULL: ASTForeignKeyActionsEnums.Action
    def __init__(self) -> None: ...

class ASTForeignKeyReferenceEnums(_message.Message):
    __slots__ = ()
    class Match(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIMPLE: _ClassVar[ASTForeignKeyReferenceEnums.Match]
        FULL: _ClassVar[ASTForeignKeyReferenceEnums.Match]
        NOT_DISTINCT: _ClassVar[ASTForeignKeyReferenceEnums.Match]
    SIMPLE: ASTForeignKeyReferenceEnums.Match
    FULL: ASTForeignKeyReferenceEnums.Match
    NOT_DISTINCT: ASTForeignKeyReferenceEnums.Match
    def __init__(self) -> None: ...

class ASTBreakContinueStatementEnums(_message.Message):
    __slots__ = ()
    class BreakContinueKeyword(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BREAK: _ClassVar[ASTBreakContinueStatementEnums.BreakContinueKeyword]
        LEAVE: _ClassVar[ASTBreakContinueStatementEnums.BreakContinueKeyword]
        CONTINUE: _ClassVar[ASTBreakContinueStatementEnums.BreakContinueKeyword]
        ITERATE: _ClassVar[ASTBreakContinueStatementEnums.BreakContinueKeyword]
    BREAK: ASTBreakContinueStatementEnums.BreakContinueKeyword
    LEAVE: ASTBreakContinueStatementEnums.BreakContinueKeyword
    CONTINUE: ASTBreakContinueStatementEnums.BreakContinueKeyword
    ITERATE: ASTBreakContinueStatementEnums.BreakContinueKeyword
    def __init__(self) -> None: ...

class ASTDropStatementEnums(_message.Message):
    __slots__ = ()
    class DropMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DROP_MODE_UNSPECIFIED: _ClassVar[ASTDropStatementEnums.DropMode]
        RESTRICT: _ClassVar[ASTDropStatementEnums.DropMode]
        CASCADE: _ClassVar[ASTDropStatementEnums.DropMode]
    DROP_MODE_UNSPECIFIED: ASTDropStatementEnums.DropMode
    RESTRICT: ASTDropStatementEnums.DropMode
    CASCADE: ASTDropStatementEnums.DropMode
    def __init__(self) -> None: ...

class ASTCreateFunctionStmtBaseEnums(_message.Message):
    __slots__ = ()
    class DeterminismLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETERMINISM_UNSPECIFIED: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
        DETERMINISTIC: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
        NOT_DETERMINISTIC: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
        IMMUTABLE: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
        STABLE: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
        VOLATILE: _ClassVar[ASTCreateFunctionStmtBaseEnums.DeterminismLevel]
    DETERMINISM_UNSPECIFIED: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    DETERMINISTIC: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    NOT_DETERMINISTIC: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    IMMUTABLE: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    STABLE: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    VOLATILE: ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    def __init__(self) -> None: ...

class ASTAuxLoadDataStatementEnums(_message.Message):
    __slots__ = ()
    class InsertionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTAuxLoadDataStatementEnums.InsertionMode]
        APPEND: _ClassVar[ASTAuxLoadDataStatementEnums.InsertionMode]
        OVERWRITE: _ClassVar[ASTAuxLoadDataStatementEnums.InsertionMode]
    NOT_SET: ASTAuxLoadDataStatementEnums.InsertionMode
    APPEND: ASTAuxLoadDataStatementEnums.InsertionMode
    OVERWRITE: ASTAuxLoadDataStatementEnums.InsertionMode
    def __init__(self) -> None: ...

class ASTSpannerInterleaveClauseEnums(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTSpannerInterleaveClauseEnums.Type]
        IN: _ClassVar[ASTSpannerInterleaveClauseEnums.Type]
        IN_PARENT: _ClassVar[ASTSpannerInterleaveClauseEnums.Type]
    NOT_SET: ASTSpannerInterleaveClauseEnums.Type
    IN: ASTSpannerInterleaveClauseEnums.Type
    IN_PARENT: ASTSpannerInterleaveClauseEnums.Type
    def __init__(self) -> None: ...

class ASTAfterMatchSkipClauseEnums(_message.Message):
    __slots__ = ()
    class AfterMatchSkipTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AFTER_MATCH_SKIP_TARGET_UNSPECIFIED: _ClassVar[ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType]
        PAST_LAST_ROW: _ClassVar[ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType]
        TO_NEXT_ROW: _ClassVar[ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType]
    AFTER_MATCH_SKIP_TARGET_UNSPECIFIED: ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType
    PAST_LAST_ROW: ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType
    TO_NEXT_ROW: ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType
    def __init__(self) -> None: ...

class ASTRowPatternAnchorEnums(_message.Message):
    __slots__ = ()
    class Anchor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANCHOR_UNSPECIFIED: _ClassVar[ASTRowPatternAnchorEnums.Anchor]
        START: _ClassVar[ASTRowPatternAnchorEnums.Anchor]
        END: _ClassVar[ASTRowPatternAnchorEnums.Anchor]
    ANCHOR_UNSPECIFIED: ASTRowPatternAnchorEnums.Anchor
    START: ASTRowPatternAnchorEnums.Anchor
    END: ASTRowPatternAnchorEnums.Anchor
    def __init__(self) -> None: ...

class ASTRowPatternOperationEnums(_message.Message):
    __slots__ = ()
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[ASTRowPatternOperationEnums.OperationType]
        CONCAT: _ClassVar[ASTRowPatternOperationEnums.OperationType]
        ALTERNATE: _ClassVar[ASTRowPatternOperationEnums.OperationType]
        PERMUTE: _ClassVar[ASTRowPatternOperationEnums.OperationType]
        EXCLUDE: _ClassVar[ASTRowPatternOperationEnums.OperationType]
    OPERATION_TYPE_UNSPECIFIED: ASTRowPatternOperationEnums.OperationType
    CONCAT: ASTRowPatternOperationEnums.OperationType
    ALTERNATE: ASTRowPatternOperationEnums.OperationType
    PERMUTE: ASTRowPatternOperationEnums.OperationType
    EXCLUDE: ASTRowPatternOperationEnums.OperationType
    def __init__(self) -> None: ...

class ASTSymbolQuantifierEnums(_message.Message):
    __slots__ = ()
    class Symbol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYMBOL_UNSPECIFIED: _ClassVar[ASTSymbolQuantifierEnums.Symbol]
        QUESTION_MARK: _ClassVar[ASTSymbolQuantifierEnums.Symbol]
        PLUS: _ClassVar[ASTSymbolQuantifierEnums.Symbol]
        STAR: _ClassVar[ASTSymbolQuantifierEnums.Symbol]
    SYMBOL_UNSPECIFIED: ASTSymbolQuantifierEnums.Symbol
    QUESTION_MARK: ASTSymbolQuantifierEnums.Symbol
    PLUS: ASTSymbolQuantifierEnums.Symbol
    STAR: ASTSymbolQuantifierEnums.Symbol
    def __init__(self) -> None: ...

class ASTGraphNodeTableReferenceEnums(_message.Message):
    __slots__ = ()
    class NodeReferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_REFERENCE_TYPE_UNSPECIFIED: _ClassVar[ASTGraphNodeTableReferenceEnums.NodeReferenceType]
        SOURCE: _ClassVar[ASTGraphNodeTableReferenceEnums.NodeReferenceType]
        DESTINATION: _ClassVar[ASTGraphNodeTableReferenceEnums.NodeReferenceType]
    NODE_REFERENCE_TYPE_UNSPECIFIED: ASTGraphNodeTableReferenceEnums.NodeReferenceType
    SOURCE: ASTGraphNodeTableReferenceEnums.NodeReferenceType
    DESTINATION: ASTGraphNodeTableReferenceEnums.NodeReferenceType
    def __init__(self) -> None: ...

class ASTGraphLabelOperationEnums(_message.Message):
    __slots__ = ()
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[ASTGraphLabelOperationEnums.OperationType]
        NOT: _ClassVar[ASTGraphLabelOperationEnums.OperationType]
        AND: _ClassVar[ASTGraphLabelOperationEnums.OperationType]
        OR: _ClassVar[ASTGraphLabelOperationEnums.OperationType]
    OPERATION_TYPE_UNSPECIFIED: ASTGraphLabelOperationEnums.OperationType
    NOT: ASTGraphLabelOperationEnums.OperationType
    AND: ASTGraphLabelOperationEnums.OperationType
    OR: ASTGraphLabelOperationEnums.OperationType
    def __init__(self) -> None: ...

class ASTGraphEdgePatternEnums(_message.Message):
    __slots__ = ()
    class EdgeOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDGE_ORIENTATION_NOT_SET: _ClassVar[ASTGraphEdgePatternEnums.EdgeOrientation]
        ANY: _ClassVar[ASTGraphEdgePatternEnums.EdgeOrientation]
        LEFT: _ClassVar[ASTGraphEdgePatternEnums.EdgeOrientation]
        RIGHT: _ClassVar[ASTGraphEdgePatternEnums.EdgeOrientation]
    EDGE_ORIENTATION_NOT_SET: ASTGraphEdgePatternEnums.EdgeOrientation
    ANY: ASTGraphEdgePatternEnums.EdgeOrientation
    LEFT: ASTGraphEdgePatternEnums.EdgeOrientation
    RIGHT: ASTGraphEdgePatternEnums.EdgeOrientation
    def __init__(self) -> None: ...

class ASTGraphPathModeEnums(_message.Message):
    __slots__ = ()
    class PathMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATH_MODE_UNSPECIFIED: _ClassVar[ASTGraphPathModeEnums.PathMode]
        WALK: _ClassVar[ASTGraphPathModeEnums.PathMode]
        TRAIL: _ClassVar[ASTGraphPathModeEnums.PathMode]
        SIMPLE: _ClassVar[ASTGraphPathModeEnums.PathMode]
        ACYCLIC: _ClassVar[ASTGraphPathModeEnums.PathMode]
    PATH_MODE_UNSPECIFIED: ASTGraphPathModeEnums.PathMode
    WALK: ASTGraphPathModeEnums.PathMode
    TRAIL: ASTGraphPathModeEnums.PathMode
    SIMPLE: ASTGraphPathModeEnums.PathMode
    ACYCLIC: ASTGraphPathModeEnums.PathMode
    def __init__(self) -> None: ...

class ASTGraphPathSearchPrefixEnums(_message.Message):
    __slots__ = ()
    class PathSearchPrefixType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATH_SEARCH_PREFIX_TYPE_UNSPECIFIED: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        ANY: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        SHORTEST: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        ALL: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        ALL_SHORTEST: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        CHEAPEST: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
        ALL_CHEAPEST: _ClassVar[ASTGraphPathSearchPrefixEnums.PathSearchPrefixType]
    PATH_SEARCH_PREFIX_TYPE_UNSPECIFIED: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    ANY: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    SHORTEST: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    ALL: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    ALL_SHORTEST: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    CHEAPEST: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    ALL_CHEAPEST: ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    def __init__(self) -> None: ...

class ASTLockModeEnums(_message.Message):
    __slots__ = ()
    class LockStrengthSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_SET: _ClassVar[ASTLockModeEnums.LockStrengthSpec]
        UPDATE: _ClassVar[ASTLockModeEnums.LockStrengthSpec]
    NOT_SET: ASTLockModeEnums.LockStrengthSpec
    UPDATE: ASTLockModeEnums.LockStrengthSpec
    def __init__(self) -> None: ...

class ASTBracedConstructorLhsEnums(_message.Message):
    __slots__ = ()
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE_SINGLE: _ClassVar[ASTBracedConstructorLhsEnums.Operation]
        UPDATE_MANY: _ClassVar[ASTBracedConstructorLhsEnums.Operation]
        UPDATE_SINGLE_NO_CREATION: _ClassVar[ASTBracedConstructorLhsEnums.Operation]
    UPDATE_SINGLE: ASTBracedConstructorLhsEnums.Operation
    UPDATE_MANY: ASTBracedConstructorLhsEnums.Operation
    UPDATE_SINGLE_NO_CREATION: ASTBracedConstructorLhsEnums.Operation
    def __init__(self) -> None: ...

class ASTAlterIndexStatementEnums(_message.Message):
    __slots__ = ()
    class IndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_DEFAULT: _ClassVar[ASTAlterIndexStatementEnums.IndexType]
        INDEX_SEARCH: _ClassVar[ASTAlterIndexStatementEnums.IndexType]
        INDEX_VECTOR: _ClassVar[ASTAlterIndexStatementEnums.IndexType]
    INDEX_DEFAULT: ASTAlterIndexStatementEnums.IndexType
    INDEX_SEARCH: ASTAlterIndexStatementEnums.IndexType
    INDEX_VECTOR: ASTAlterIndexStatementEnums.IndexType
    def __init__(self) -> None: ...
