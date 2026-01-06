# ProtoModel Inheritance Hierarchy

This document describes the inheritance structure of the ProtoModel system in zetasql-py.

## Overview

The ProtoModel system provides a Pythonic wrapper layer over ZetaSQL protobuf messages. It uses dataclass-based models with automatic bidirectional proto conversion.

**Statistics:**
- Total ProtoModel classes: 1,196
- Direct ProtoModel subclasses: 354
- Classes with inheritance: 66+
- Maximum inheritance depth: 3 levels

## Base Classes

### `ProtoModel`

The root base class for all ZetaSQL proto model wrappers.

**Location:** `zetasql.types.proto_model.proto_model.ProtoModel`

**Key Features:**
- Automatic proto conversion (`from_proto()`, `to_proto()`)
- MRO-based parent chain tracking
- Union type handling
- Field metadata system

**Class Variables:**
```python
_PROTO_CLASS: ClassVar[type]              # Associated protobuf class
_PROTO_FIELD_MAP: ClassVar[dict]          # Field metadata mapping
```

**Core Methods:**
```python
@classmethod
def from_proto(proto) -> Self             # Create from protobuf message
def to_proto() -> Message                  # Convert to protobuf message
```

## Major Inheritance Chains

### 1. AST Node Hierarchy

The Abstract Syntax Tree (AST) represents parsed SQL structure.

```
ProtoModel
└── ASTNode                               # Base for all AST nodes
    ├── ASTStatement                      # SQL statements
    │   ├── ASTQueryStatement            # SELECT, WITH, etc.
    │   ├── ASTDdlStatement              # DDL statements
    │   │   ├── ASTCreateStatement       # CREATE ...
    │   │   │   ├── ASTCreateTableStatement
    │   │   │   ├── ASTCreateViewStatement
    │   │   │   ├── ASTCreateFunctionStatement
    │   │   │   └── ...
    │   │   ├── ASTAlterStatement        # ALTER ...
    │   │   ├── ASTDropStatement         # DROP ...
    │   │   └── ...
    │   ├── ASTDmlStatement              # DML statements
    │   │   ├── ASTInsertStatement
    │   │   ├── ASTUpdateStatement
    │   │   ├── ASTDeleteStatement
    │   │   └── ASTMergeStatement
    │   └── ASTScriptStatement           # Scripting statements
    │       ├── ASTIfStatement
    │       ├── ASTWhileStatement
    │       ├── ASTForInStatement
    │       └── ...
    ├── ASTExpression                     # Expressions
    │   ├── ASTLeaf                      # Terminal expressions
    │   │   ├── ASTIntLiteral
    │   │   ├── ASTStringLiteral
    │   │   ├── ASTIdentifier
    │   │   └── ...
    │   ├── ASTBinaryExpression          # Binary operations
    │   ├── ASTUnaryExpression           # Unary operations
    │   ├── ASTFunctionCall              # Function calls
    │   ├── ASTCastExpression            # Type casts
    │   └── ...
    ├── ASTType                          # Type specifications
    │   ├── ASTSimpleType
    │   ├── ASTArrayType
    │   ├── ASTStructType
    │   └── ...
    ├── ASTTableExpression               # Table references
    │   ├── ASTTablePathExpression
    │   ├── ASTTableSubquery
    │   ├── ASTJoin
    │   └── ...
    ├── ASTAlterAction                   # ALTER statement actions
    │   ├── ASTAddColumnAction
    │   ├── ASTDropColumnAction
    │   ├── ASTSetOptionsAction
    │   └── ...
    └── (many other specialized node types)
```

**Key Node Types:**
- **Statements**: Top-level SQL commands
- **Expressions**: Computations and values
- **Types**: Type specifications
- **Table Expressions**: FROM clause components
- **Clauses**: WHERE, GROUP BY, ORDER BY, etc.

### 2. Resolved AST Hierarchy

The Resolved AST represents analyzed and type-checked SQL.

```
ProtoModel
└── ResolvedNode                          # Base for resolved AST
    ├── ResolvedStatement                 # Resolved statements
    │   ├── ResolvedQueryStmt            # SELECT queries
    │   ├── ResolvedCreateTableStmt
    │   ├── ResolvedInsertStmt
    │   └── ...
    ├── ResolvedExpr                      # Resolved expressions
    │   ├── ResolvedLiteral              # Constant values
    │   ├── ResolvedColumnRef            # Column references
    │   ├── ResolvedFunctionCall         # Function calls
    │   ├── ResolvedCast                 # Type conversions
    │   └── ...
    ├── ResolvedScan                      # Table scans
    │   ├── ResolvedTableScan
    │   ├── ResolvedJoinScan
    │   ├── ResolvedArrayScan
    │   ├── ResolvedFilterScan
    │   ├── ResolvedAggregateScan
    │   └── ...
    └── (other resolved node types)
```

**Purpose:**
- Post-analysis representation
- Contains full type information
- Resolves names to catalog entries
- Used for query execution

### 3. Type System

```
ProtoModel
├── Type                                  # Base type class
│   ├── SimpleType                       # INT64, STRING, etc.
│   ├── ArrayType                        # ARRAY<T>
│   ├── StructType                       # STRUCT<...>
│   ├── ProtoType                        # Protocol buffer types
│   ├── EnumType                         # ENUM types
│   └── ...
├── TypeParameters                        # Type parameterization
├── TypeModifiers                         # Type modifiers (collation, etc.)
└── FieldDescriptor                       # Struct field metadata
```

### 4. Catalog System

```
ProtoModel
├── SimpleCatalog                         # Catalog container
├── SimpleTable                           # Table definitions
├── SimpleColumn                          # Column metadata
├── Function                              # Function definitions
│   └── FunctionSignature                # Function signature
├── SimpleConstant                        # Named constants
├── SimpleProcedure                       # Stored procedures
└── SimpleTVF                            # Table-valued functions
```

### 5. Options and Configuration

```
ProtoModel
├── AnalyzerOptions                       # Analysis configuration
│   └── QueryParameters                  # Query parameters
├── LanguageOptions                       # Language features
│   └── LanguageFeature (IntEnum)        # Individual features
├── ZetaSQLBuiltinFunctionOptions        # Builtin function config
├── ExecuteQueryOptions                   # Execution options
└── FormatterOptions                      # SQL formatting options
```

### 6. Value System

```
ProtoModel
├── Value                                 # SQL values
│   ├── Value.Array                      # Array values
│   └── Value.Struct                     # Struct values
└── ValueWithType                        # Value + type pair
```

## Enum Classes

Many enums are defined as `IntEnum` subclasses (not ProtoModel):

```python
class TypeKind(IntEnum):                  # Type identifiers
    TYPE_INT64 = 1
    TYPE_STRING = 3
    TYPE_ARRAY = 13
    # ... 30+ types

class LanguageFeature(IntEnum):           # Language features
    FEATURE_ANALYTIC_FUNCTIONS = 1
    FEATURE_TABLESAMPLE = 2
    # ... 200+ features

class ResolvedNodeKind(IntEnum):          # Resolved node types
    RESOLVED_LITERAL = 1
    RESOLVED_QUERY_STMT = 2
    # ... 200+ kinds

class SignatureArgumentKind(IntEnum):     # Function argument kinds
    ARG_TYPE_FIXED = 1
    ARG_TYPE_ANY_1 = 2
    # ... etc.
```

## Nested Enums

Some ProtoModel classes contain nested enum classes:

```python
class FunctionEnums(ProtoModel):
    class Mode(IntEnum):                  # Function modes
        SCALAR = 0
        AGGREGATE = 1
        ANALYTIC = 2
        # ...
    
    class ArgumentCardinality(IntEnum):   # Argument cardinality
        REQUIRED = 0
        OPTIONAL = 1
        REPEATED = 2

class ASTJoinEnums(ProtoModel):
    class JoinType(IntEnum):              # JOIN types
        DEFAULT = 0
        COMMA = 1
        CROSS = 2
        FULL = 3
        INNER = 4
        LEFT = 5
        RIGHT = 6
```

## Union Types

ZetaSQL uses union types for polymorphic fields. The ProtoModel system handles these automatically:

```python
# Example: AnyASTExpression is a union of all expression types
class AnyASTExpression(ProtoModel):
    """Union type for any AST expression."""
    # Contains oneof fields for each expression variant
    # Automatically unwraps to concrete type on access
```

**Common Union Types:**
- `AnyASTExpression` - Any expression node
- `AnyASTStatement` - Any statement node
- `AnyASTType` - Any type specification
- `AnyResolvedNode` - Any resolved AST node

## Field Metadata

Each ProtoModel class defines field metadata in `_PROTO_FIELD_MAP`:

```python
_PROTO_FIELD_MAP = {
    "field_name": {
        "proto_field": "field_name",      # Proto field name
        "python_field": "field_name",     # Python field name
        "is_repeated": False,             # List field?
        "is_message": True,               # Proto message?
        "message_type": "SomeType",       # Message type name
        "enum_type_name": "SomeEnum",     # Enum type (if enum field)
        "is_union": False,                # Union type?
    }
}
```

## Mixins

Some classes use mixins for additional functionality:

```python
class TypeKind(proto_model_mixins.TypeKindMixin, IntEnum):
    """TypeKind with helper methods."""
    
    def is_simple_type(self) -> bool:
        """Check if this is a simple type."""
        return self in (TYPE_INT64, TYPE_STRING, TYPE_BOOL, ...)
    
    def is_complex_type(self) -> bool:
        """Check if this is a complex type."""
        return self in (TYPE_ARRAY, TYPE_STRUCT, TYPE_PROTO, ...)
```

## Usage Patterns

### Creating Instances

```python
from zetasql.types import ResolvedLiteral, Type, TypeKind

# Direct instantiation (no proto needed)
literal = ResolvedLiteral(
    type=Type(type_kind=TypeKind.TYPE_INT64),
    value=42,
    has_explicit_type=False
)
```

### Converting to/from Proto

```python
# To proto
proto = literal.to_proto()

# From proto
literal2 = ResolvedLiteral.from_proto(proto)
```

### Accessing Fields

```python
# Direct field access
print(literal.value)
print(literal.type.type_kind)

# Handle optional fields
if literal.has_explicit_type:
    print("Has explicit type")
```

### Working with Lists

```python
from zetasql.types import ResolvedQueryStmt

stmt = ResolvedQueryStmt(
    output_column_list=[
        OutputColumn(name="id", column=...),
        OutputColumn(name="name", column=...),
    ]
)

# Iterate
for col in stmt.output_column_list:
    print(col.name)
```

## Design Principles

1. **Dataclass-based**: All models use `@dataclass` for clean Python syntax
2. **Proto-agnostic**: Can create instances without proto messages
3. **Automatic conversion**: Seamless proto ↔ model conversion
4. **Type safety**: Full type hints for IDE support
5. **MRO-aware**: Properly handles inheritance chains
6. **Union handling**: Automatic wrapping/unwrapping of union types

## Implementation Details

### Proto Conversion Algorithm

```
to_proto():
1. Create proto instance from _PROTO_CLASS
2. For each field in _PROTO_FIELD_MAP:
   a. Get value from dataclass field
   b. If None, skip
   c. If repeated: convert list recursively
   d. If message: convert ProtoModel recursively
   e. If union: wrap in union proto
   f. Set proto field
3. Return proto

from_proto():
1. Extract values from proto
2. For each field:
   a. Get proto value
   b. If message: convert to ProtoModel
   c. If repeated: convert list recursively
   d. If enum: convert to IntEnum
   e. Store in dict
3. Create dataclass instance from dict
```

### Union Type Resolution

When setting a field that expects a union type:
1. Check if target field is a union (has oneofs)
2. Find matching variant field in union
3. Wrap value in union proto
4. Handle nested unions recursively

## See Also

- [Architecture Documentation](architecture.md) - Overall system design
- [API Reference](api-reference.md) - Public API documentation
- [Type System](getting-started.md#types-and-values) - Working with types
- Source: `src/zetasql/types/proto_model/`

## All ProtoModel Hierarchy

```
ProtoModel
├── ASTAfterMatchSkipClauseEnums
├── ASTAlterIndexStatementEnums
├── ASTAnySomeAllOpEnums
├── ASTAuxLoadDataStatementEnums
├── ASTBinaryExpressionEnums
├── ASTBracedConstructorLhsEnums
├── ASTBreakContinueStatementEnums
├── ASTColumnPositionEnums
├── ASTCreateFunctionStmtBaseEnums
├── ASTCreateStatementEnums
├── ASTDropStatementEnums
├── ASTExpressionSubqueryEnums
├── ASTFilterFieldsArgEnums
├── ASTForeignKeyActionsEnums
├── ASTForeignKeyReferenceEnums
├── ASTFunctionCallEnums
├── ASTFunctionParameterEnums
├── ASTGeneratedColumnInfoEnums
├── ASTGraphEdgePatternEnums
├── ASTGraphLabelOperationEnums
├── ASTGraphNodeTableReferenceEnums
├── ASTGraphPathModeEnums
├── ASTGraphPathSearchPrefixEnums
├── ASTHavingModifierEnums
├── ASTImportStatementEnums
├── ASTInsertStatementEnums
├── ASTJoinEnums
├── ASTLockModeEnums
├── ASTMergeActionEnums
├── ASTMergeWhenClauseEnums
├── ASTNode
│   ├── ASTAfterMatchSkipClause
│   ├── ASTAlias
│   ├── ASTAliasedQuery
│   ├── ASTAliasedQueryList
│   ├── ASTAliasedQueryModifiers
│   ├── ASTAlterAction
│   │   ├── ASTAddColumnAction
│   │   ├── ASTAddColumnIdentifierAction
│   │   ├── ASTAddConstraintAction
│   │   ├── ASTAddSubEntityAction
│   │   ├── ASTAddToRestricteeListClause
│   │   ├── ASTAddTtlAction
│   │   ├── ASTAlterColumnDropDefaultAction
│   │   ├── ASTAlterColumnDropGeneratedAction
│   │   ├── ASTAlterColumnDropNotNullAction
│   │   ├── ASTAlterColumnOptionsAction
│   │   ├── ASTAlterColumnSetDefaultAction
│   │   ├── ASTAlterColumnSetGeneratedAction
│   │   ├── ASTAlterColumnTypeAction
│   │   ├── ASTAlterConstraintEnforcementAction
│   │   ├── ASTAlterConstraintSetOptionsAction
│   │   ├── ASTAlterSubEntityAction
│   │   ├── ASTDropColumnAction
│   │   ├── ASTDropConstraintAction
│   │   ├── ASTDropPrimaryKeyAction
│   │   ├── ASTDropSubEntityAction
│   │   ├── ASTDropTtlAction
│   │   ├── ASTFilterUsingClause
│   │   ├── ASTGrantToClause
│   │   ├── ASTRebuildAction
│   │   ├── ASTRemoveFromRestricteeListClause
│   │   ├── ASTRenameColumnAction
│   │   ├── ASTRenameToClause
│   │   ├── ASTReplaceTtlAction
│   │   ├── ASTRestrictToClause
│   │   ├── ASTRevokeFromClause
│   │   ├── ASTSetAsAction
│   │   ├── ASTSetCollateClause
│   │   ├── ASTSetOptionsAction
│   │   ├── ASTSpannerAlterColumnAction
│   │   └── ASTSpannerSetOnDeleteAction
│   ├── ASTAlterActionList
│   ├── ASTAnySomeAllOp
│   ├── ASTAssertRowsModified
│   ├── ASTAuxLoadDataFromFilesOptionsList
│   ├── ASTAuxLoadDataPartitionsClause
│   ├── ASTBracedConstructorField
│   ├── ASTBracedConstructorFieldValue
│   ├── ASTChainedBaseExpr
│   ├── ASTClampedBetweenModifier
│   ├── ASTCloneDataSourceList
│   ├── ASTClusterBy
│   ├── ASTCollate
│   ├── ASTColumnAttribute
│   │   ├── ASTForeignKeyColumnAttribute
│   │   ├── ASTHiddenColumnAttribute
│   │   ├── ASTNotNullColumnAttribute
│   │   └── ASTPrimaryKeyColumnAttribute
│   ├── ASTColumnAttributeList
│   ├── ASTColumnList
│   ├── ASTColumnPosition
│   ├── ASTColumnSchema
│   │   ├── ASTElementTypeColumnSchema
│   │   │   ├── ASTArrayColumnSchema
│   │   │   └── ASTRangeColumnSchema
│   │   ├── ASTInferredTypeColumnSchema
│   │   ├── ASTSimpleColumnSchema
│   │   └── ASTStructColumnSchema
│   ├── ASTColumnWithOptions
│   ├── ASTColumnWithOptionsList
│   ├── ASTConnectionClause
│   ├── ASTCube
│   ├── ASTDescriptor
│   ├── ASTDescriptorColumn
│   ├── ASTDescriptorColumnList
│   ├── ASTElseifClause
│   ├── ASTElseifClauseList
│   ├── ASTExceptionHandler
│   ├── ASTExceptionHandlerList
│   ├── ASTExecuteIntoClause
│   ├── ASTExecuteUsingArgument
│   ├── ASTExecuteUsingClause
│   ├── ASTExpression
│   │   ├── ASTAnalyticFunctionCall
│   │   ├── ASTAndExpr
│   │   ├── ASTArrayConstructor
│   │   ├── ASTBetweenExpression
│   │   ├── ASTBinaryExpression
│   │   ├── ASTBitwiseShiftExpression
│   │   ├── ASTBracedConstructor
│   │   ├── ASTBracedConstructorLhs
│   │   ├── ASTBracedNewConstructor
│   │   ├── ASTCaseNoValueExpression
│   │   ├── ASTCaseValueExpression
│   │   ├── ASTCastExpression
│   │   ├── ASTConcatExpr
│   │   ├── ASTDateOrTimeLiteral
│   │   ├── ASTDefaultLiteral
│   │   ├── ASTDotStar
│   │   ├── ASTDotStarWithModifiers
│   │   ├── ASTExpressionSubquery
│   │   ├── ASTExpressionWithAlias
│   │   ├── ASTExtractExpression
│   │   ├── ASTFunctionCall
│   │   ├── ASTGeneralizedPathExpression
│   │   │   ├── ASTArrayElement
│   │   │   ├── ASTDotGeneralizedField
│   │   │   ├── ASTDotIdentifier
│   │   │   ├── ASTExtendedPathExpression
│   │   │   └── ASTPathExpression
│   │   ├── ASTGraphIsLabeledPredicate
│   │   ├── ASTIdentifier
│   │   ├── ASTInExpression
│   │   ├── ASTInputTableArgument
│   │   ├── ASTIntOrUnbounded
│   │   ├── ASTIntervalExpr
│   │   ├── ASTLambda
│   │   ├── ASTLeaf
│   │   │   ├── ASTBigNumericLiteral
│   │   │   ├── ASTBytesLiteral
│   │   │   ├── ASTJSONLiteral
│   │   │   ├── ASTNumericLiteral
│   │   │   ├── ASTPrintableLeaf
│   │   │   │   ├── ASTBooleanLiteral
│   │   │   │   ├── ASTBytesLiteralComponent
│   │   │   │   ├── ASTFloatLiteral
│   │   │   │   ├── ASTIndexAllColumns
│   │   │   │   ├── ASTIntLiteral
│   │   │   │   ├── ASTMacroBody
│   │   │   │   ├── ASTMaxLiteral
│   │   │   │   ├── ASTNullLiteral
│   │   │   │   ├── ASTStar
│   │   │   │   └── ASTStringLiteralComponent
│   │   │   └── ASTStringLiteral
│   │   ├── ASTLikeExpression
│   │   ├── ASTNamedArgument
│   │   ├── ASTNewConstructor
│   │   ├── ASTOrExpr
│   │   ├── ASTParameterExprBase
│   │   │   ├── ASTParameterExpr
│   │   │   └── ASTSystemVariableExpr
│   │   ├── ASTRangeLiteral
│   │   ├── ASTReplaceFieldsExpression
│   │   ├── ASTSequenceArg
│   │   ├── ASTStarWithModifiers
│   │   ├── ASTStructBracedConstructor
│   │   ├── ASTStructConstructorWithKeyword
│   │   ├── ASTStructConstructorWithParens
│   │   ├── ASTUnaryExpression
│   │   ├── ASTUpdateConstructor
│   │   └── ASTWithExpression
│   ├── ASTExpressionWithOptAlias
│   ├── ASTFilterFieldsArg
│   ├── ASTForSystemTime
│   ├── ASTForeignKeyActions
│   ├── ASTForeignKeyReference
│   ├── ASTFormatClause
│   ├── ASTFromClause
│   ├── ASTFunctionDeclaration
│   ├── ASTFunctionParameter
│   ├── ASTFunctionParameters
│   ├── ASTFunctionTypeArgList
│   ├── ASTGeneratedColumnInfo
│   ├── ASTGqlLetVariableDefinition
│   ├── ASTGqlLetVariableDefinitionList
│   ├── ASTGqlOperator
│   │   ├── ASTGqlCallBase
│   │   │   ├── ASTGqlInlineSubqueryCall
│   │   │   └── ASTGqlNamedCall
│   │   ├── ASTGqlFilter
│   │   ├── ASTGqlFor
│   │   ├── ASTGqlLet
│   │   ├── ASTGqlMatch
│   │   ├── ASTGqlOperatorList
│   │   ├── ASTGqlOrderByAndPage
│   │   ├── ASTGqlReturn
│   │   ├── ASTGqlSample
│   │   ├── ASTGqlSetOperation
│   │   └── ASTGqlWith
│   ├── ASTGqlPage
│   ├── ASTGqlPageLimit
│   ├── ASTGqlPageOffset
│   ├── ASTGranteeList
│   ├── ASTGraphDerivedProperty
│   ├── ASTGraphDerivedPropertyList
│   ├── ASTGraphDynamicLabel
│   ├── ASTGraphDynamicProperties
│   ├── ASTGraphElementLabelAndProperties
│   ├── ASTGraphElementLabelAndPropertiesList
│   ├── ASTGraphElementPatternFiller
│   ├── ASTGraphElementTable
│   ├── ASTGraphElementTableList
│   ├── ASTGraphLabelExpression
│   │   ├── ASTGraphElementLabel
│   │   ├── ASTGraphLabelOperation
│   │   └── ASTGraphWildcardLabel
│   ├── ASTGraphLabelFilter
│   ├── ASTGraphLhsHint
│   ├── ASTGraphNodeTableReference
│   ├── ASTGraphPathBase
│   │   ├── ASTGraphElementPattern
│   │   │   ├── ASTGraphEdgePattern
│   │   │   └── ASTGraphNodePattern
│   │   └── ASTGraphPathPattern
│   ├── ASTGraphPathMode
│   ├── ASTGraphPathSearchPrefix
│   ├── ASTGraphPathSearchPrefixCount
│   ├── ASTGraphPattern
│   ├── ASTGraphProperties
│   ├── ASTGraphPropertyNameAndValue
│   ├── ASTGraphPropertySpecification
│   ├── ASTGraphRhsHint
│   ├── ASTGroupBy
│   ├── ASTGroupByAll
│   ├── ASTGroupingItem
│   ├── ASTGroupingItemOrder
│   ├── ASTGroupingSet
│   ├── ASTGroupingSetList
│   ├── ASTHaving
│   ├── ASTHavingModifier
│   ├── ASTHint
│   ├── ASTHintEntry
│   ├── ASTIdentifierList
│   ├── ASTIdentityColumnIncrementBy
│   ├── ASTIdentityColumnInfo
│   ├── ASTIdentityColumnMaxValue
│   ├── ASTIdentityColumnMinValue
│   ├── ASTIdentityColumnStartWith
│   ├── ASTInList
│   ├── ASTIndexItemList
│   ├── ASTIndexStoringExpressionList
│   ├── ASTIndexUnnestExpressionList
│   ├── ASTInputOutputClause
│   ├── ASTInsertValuesRow
│   ├── ASTInsertValuesRowList
│   ├── ASTIntoAlias
│   ├── ASTLabel
│   ├── ASTLimit
│   ├── ASTLimitAll
│   ├── ASTLimitOffset
│   ├── ASTLocation
│   ├── ASTLockMode
│   ├── ASTMergeAction
│   ├── ASTMergeWhenClause
│   ├── ASTMergeWhenClauseList
│   ├── ASTModelClause
│   ├── ASTNewConstructorArg
│   ├── ASTNullOrder
│   ├── ASTOnClause
│   ├── ASTOnConflictClause
│   ├── ASTOnOrUsingClauseList
│   ├── ASTOptionsEntry
│   ├── ASTOptionsList
│   ├── ASTOrderBy
│   ├── ASTOrderingExpression
│   ├── ASTPartitionBy
│   ├── ASTPathExpressionList
│   ├── ASTPipeOperator
│   │   ├── ASTPipeAggregate
│   │   ├── ASTPipeAs
│   │   ├── ASTPipeAssert
│   │   ├── ASTPipeCall
│   │   ├── ASTPipeCreateTable
│   │   ├── ASTPipeDescribe
│   │   ├── ASTPipeDistinct
│   │   ├── ASTPipeDrop
│   │   ├── ASTPipeExportData
│   │   ├── ASTPipeExtend
│   │   ├── ASTPipeFork
│   │   ├── ASTPipeIf
│   │   ├── ASTPipeIfCase
│   │   ├── ASTPipeInsert
│   │   ├── ASTPipeJoin
│   │   ├── ASTPipeLimitOffset
│   │   ├── ASTPipeLog
│   │   ├── ASTPipeMatchRecognize
│   │   ├── ASTPipeOrderBy
│   │   ├── ASTPipePivot
│   │   ├── ASTPipeRecursiveUnion
│   │   ├── ASTPipeRename
│   │   ├── ASTPipeRenameItem
│   │   ├── ASTPipeSelect
│   │   ├── ASTPipeSet
│   │   ├── ASTPipeSetOperation
│   │   ├── ASTPipeStaticDescribe
│   │   ├── ASTPipeTablesample
│   │   ├── ASTPipeTee
│   │   ├── ASTPipeUnpivot
│   │   ├── ASTPipeWhere
│   │   ├── ASTPipeWindow
│   │   └── ASTPipeWith
│   ├── ASTPipeSetItem
│   ├── ASTPivotExpression
│   ├── ASTPivotExpressionList
│   ├── ASTPivotValue
│   ├── ASTPivotValueList
│   ├── ASTPostfixTableOperator
│   │   ├── ASTMatchRecognizeClause
│   │   ├── ASTPivotClause
│   │   ├── ASTSampleClause
│   │   └── ASTUnpivotClause
│   ├── ASTPrimaryKeyElement
│   ├── ASTPrimaryKeyElementList
│   ├── ASTPrivilege
│   ├── ASTPrivileges
│   ├── ASTQualify
│   ├── ASTQuantifier
│   │   ├── ASTBoundedQuantifier
│   │   ├── ASTFixedQuantifier
│   │   └── ASTSymbolQuantifier
│   ├── ASTQuantifierBound
│   ├── ASTQueryExpression
│   │   ├── ASTAliasedQueryExpression
│   │   ├── ASTFromQuery
│   │   ├── ASTGqlGraphPatternQuery
│   │   ├── ASTGqlLinearOpsQuery
│   │   ├── ASTGqlQuery
│   │   ├── ASTQuery
│   │   ├── ASTSelect
│   │   ├── ASTSetOperation
│   │   └── ASTTableClause
│   ├── ASTRecursionDepthModifier
│   ├── ASTRepeatableClause
│   ├── ASTReplaceFieldsArg
│   ├── ASTReturningClause
│   ├── ASTRollup
│   ├── ASTRowPatternExpression
│   │   ├── ASTEmptyRowPattern
│   │   ├── ASTRowPatternAnchor
│   │   ├── ASTRowPatternOperation
│   │   ├── ASTRowPatternQuantification
│   │   └── ASTRowPatternVariable
│   ├── ASTSampleSize
│   ├── ASTSampleSuffix
│   ├── ASTScript
│   ├── ASTSelectAs
│   ├── ASTSelectColumn
│   ├── ASTSelectList
│   ├── ASTSelectWith
│   ├── ASTSetOperationAllOrDistinct
│   ├── ASTSetOperationColumnMatchMode
│   ├── ASTSetOperationColumnPropagationMode
│   ├── ASTSetOperationMetadata
│   ├── ASTSetOperationMetadataList
│   ├── ASTSetOperationType
│   ├── ASTSpannerInterleaveClause
│   ├── ASTSpannerTableOptions
│   ├── ASTSqlFunctionBody
│   ├── ASTStarExceptList
│   ├── ASTStarModifiers
│   ├── ASTStarReplaceItem
│   ├── ASTStatement
│   │   ├── ASTAbortBatchStatement
│   │   ├── ASTAlterAllRowAccessPoliciesStatement
│   │   ├── ASTAnalyzeStatement
│   │   ├── ASTAssertStatement
│   │   ├── ASTBeginStatement
│   │   ├── ASTCallStatement
│   │   ├── ASTCloneDataStatement
│   │   ├── ASTCommitStatement
│   │   ├── ASTCreateDatabaseStatement
│   │   ├── ASTCreateLocalityGroupStatement
│   │   ├── ASTDdlStatement
│   │   │   ├── ASTAlterStatementBase
│   │   │   │   ├── ASTAlterApproxViewStatement
│   │   │   │   ├── ASTAlterConnectionStatement
│   │   │   │   ├── ASTAlterDatabaseStatement
│   │   │   │   ├── ASTAlterEntityStatement
│   │   │   │   ├── ASTAlterExternalSchemaStatement
│   │   │   │   ├── ASTAlterIndexStatement
│   │   │   │   ├── ASTAlterMaterializedViewStatement
│   │   │   │   ├── ASTAlterModelStatement
│   │   │   │   ├── ASTAlterPrivilegeRestrictionStatement
│   │   │   │   ├── ASTAlterRowAccessPolicyStatement
│   │   │   │   ├── ASTAlterSchemaStatement
│   │   │   │   ├── ASTAlterSequenceStatement
│   │   │   │   ├── ASTAlterTableStatement
│   │   │   │   └── ASTAlterViewStatement
│   │   │   ├── ASTCreateStatement
│   │   │   │   ├── ASTCreateConnectionStatement
│   │   │   │   ├── ASTCreateConstantStatement
│   │   │   │   ├── ASTCreateEntityStatement
│   │   │   │   ├── ASTCreateFunctionStmtBase
│   │   │   │   │   ├── ASTCreateFunctionStatement
│   │   │   │   │   └── ASTCreateTableFunctionStatement
│   │   │   │   ├── ASTCreateIndexStatement
│   │   │   │   ├── ASTCreateModelStatement
│   │   │   │   ├── ASTCreatePrivilegeRestrictionStatement
│   │   │   │   ├── ASTCreateProcedureStatement
│   │   │   │   ├── ASTCreatePropertyGraphStatement
│   │   │   │   ├── ASTCreateRowAccessPolicyStatement
│   │   │   │   ├── ASTCreateSchemaStmtBase
│   │   │   │   │   ├── ASTCreateExternalSchemaStatement
│   │   │   │   │   └── ASTCreateSchemaStatement
│   │   │   │   ├── ASTCreateSequenceStatement
│   │   │   │   ├── ASTCreateSnapshotStatement
│   │   │   │   ├── ASTCreateSnapshotTableStatement
│   │   │   │   ├── ASTCreateTableStmtBase
│   │   │   │   │   ├── ASTAuxLoadDataStatement
│   │   │   │   │   ├── ASTCreateExternalTableStatement
│   │   │   │   │   └── ASTCreateTableStatement
│   │   │   │   └── ASTCreateViewStatementBase
│   │   │   │       ├── ASTCreateApproxViewStatement
│   │   │   │       ├── ASTCreateMaterializedViewStatement
│   │   │   │       └── ASTCreateViewStatement
│   │   │   ├── ASTDropEntityStatement
│   │   │   ├── ASTDropFunctionStatement
│   │   │   ├── ASTDropIndexStatement
│   │   │   │   ├── ASTDropSearchIndexStatement
│   │   │   │   └── ASTDropVectorIndexStatement
│   │   │   ├── ASTDropMaterializedViewStatement
│   │   │   ├── ASTDropPrivilegeRestrictionStatement
│   │   │   ├── ASTDropRowAccessPolicyStatement
│   │   │   ├── ASTDropSnapshotTableStatement
│   │   │   ├── ASTDropStatement
│   │   │   ├── ASTDropTableFunctionStatement
│   │   │   └── ASTUndropStatement
│   │   ├── ASTDefineMacroStatement
│   │   ├── ASTDefineTableStatement
│   │   ├── ASTDeleteStatement
│   │   ├── ASTDescribeStatement
│   │   ├── ASTDropAllRowAccessPoliciesStatement
│   │   ├── ASTExecuteImmediateStatement
│   │   ├── ASTExplainStatement
│   │   ├── ASTExportDataStatement
│   │   ├── ASTExportMetadataStatement
│   │   ├── ASTExportModelStatement
│   │   ├── ASTGrantStatement
│   │   ├── ASTHintedStatement
│   │   ├── ASTImportStatement
│   │   ├── ASTInsertStatement
│   │   ├── ASTMergeStatement
│   │   ├── ASTModuleStatement
│   │   ├── ASTParameterAssignment
│   │   ├── ASTQueryStatement
│   │   ├── ASTRenameStatement
│   │   ├── ASTRevokeStatement
│   │   ├── ASTRollbackStatement
│   │   ├── ASTRunBatchStatement
│   │   ├── ASTRunStatement
│   │   ├── ASTScriptStatement
│   │   │   ├── ASTAssignmentFromStruct
│   │   │   ├── ASTBeginEndBlock
│   │   │   ├── ASTBreakContinueStatement
│   │   │   │   ├── ASTBreakStatement
│   │   │   │   └── ASTContinueStatement
│   │   │   ├── ASTCaseStatement
│   │   │   ├── ASTIfStatement
│   │   │   ├── ASTLoopStatement
│   │   │   │   ├── ASTForInStatement
│   │   │   │   ├── ASTRepeatStatement
│   │   │   │   └── ASTWhileStatement
│   │   │   ├── ASTRaiseStatement
│   │   │   ├── ASTReturnStatement
│   │   │   ├── ASTSingleAssignment
│   │   │   └── ASTVariableDeclaration
│   │   ├── ASTSetTransactionStatement
│   │   ├── ASTShowStatement
│   │   ├── ASTStartBatchStatement
│   │   ├── ASTStatementWithPipeOperators
│   │   ├── ASTSubpipelineStatement
│   │   ├── ASTSystemVariableAssignment
│   │   ├── ASTTruncateStatement
│   │   └── ASTUpdateStatement
│   ├── ASTStatementList
│   ├── ASTStructColumnField
│   ├── ASTStructConstructorArg
│   ├── ASTStructField
│   ├── ASTSubpipeline
│   ├── ASTTVFArgument
│   ├── ASTTVFSchema
│   ├── ASTTVFSchemaColumn
│   ├── ASTTableAndColumnInfo
│   ├── ASTTableAndColumnInfoList
│   ├── ASTTableElement
│   │   ├── ASTColumnDefinition
│   │   └── ASTTableConstraint
│   │       ├── ASTCheckConstraint
│   │       ├── ASTForeignKey
│   │       └── ASTPrimaryKey
│   ├── ASTTableElementList
│   ├── ASTTableExpression
│   │   ├── ASTGraphTableQuery
│   │   ├── ASTJoin
│   │   ├── ASTParenthesizedJoin
│   │   ├── ASTPipeJoinLhsPlaceholder
│   │   ├── ASTTVF
│   │   ├── ASTTableDataSource
│   │   │   ├── ASTCloneDataSource
│   │   │   └── ASTCopyDataSource
│   │   ├── ASTTablePathExpression
│   │   └── ASTTableSubquery
│   ├── ASTTemplatedParameterType
│   ├── ASTTransactionMode
│   │   ├── ASTTransactionIsolationLevel
│   │   └── ASTTransactionReadWriteMode
│   ├── ASTTransactionModeList
│   ├── ASTTransformClause
│   ├── ASTTtlClause
│   ├── ASTType
│   │   ├── ASTArrayType
│   │   ├── ASTFunctionType
│   │   ├── ASTMapType
│   │   ├── ASTRangeType
│   │   ├── ASTSimpleType
│   │   └── ASTStructType
│   ├── ASTTypeParameterList
│   ├── ASTUnnestExpression
│   ├── ASTUnnestExpressionWithOptAliasAndOffset
│   ├── ASTUnpivotInItem
│   ├── ASTUnpivotInItemLabel
│   ├── ASTUnpivotInItemList
│   ├── ASTUntilClause
│   ├── ASTUpdateItem
│   ├── ASTUpdateItemList
│   ├── ASTUpdateSetValue
│   ├── ASTUsingClause
│   ├── ASTWhenThenClause
│   ├── ASTWhenThenClauseList
│   ├── ASTWhereClause
│   ├── ASTWindowClause
│   ├── ASTWindowDefinition
│   ├── ASTWindowFrame
│   ├── ASTWindowFrameExpr
│   ├── ASTWindowSpecification
│   ├── ASTWithClause
│   ├── ASTWithConnectionClause
│   ├── ASTWithOffset
│   ├── ASTWithPartitionColumnsClause
│   ├── ASTWithReportModifier
│   ├── ASTWithWeight
│   └── ASTYieldItemList
├── ASTOnConflictClauseEnums
├── ASTOptionsEntryEnums
├── ASTOrderingExpressionEnums
├── ASTRowPatternAnchorEnums
├── ASTRowPatternOperationEnums
├── ASTSampleSizeEnums
├── ASTSelectAsEnums
├── ASTSetOperationEnums
├── ASTSpannerInterleaveClauseEnums
├── ASTSymbolQuantifierEnums
├── ASTTemplatedParameterTypeEnums
├── ASTTransactionReadWriteModeEnums
├── ASTUnaryExpressionEnums
├── ASTUnpivotClauseEnums
├── ASTWindowFrameEnums
├── ASTWindowFrameExprEnums
├── AllowedHintsAndOptions
├── AnalyzeRequest
├── AnalyzeResponse
├── AnalyzerLogEntry
├── AnalyzerOptions
├── AnalyzerOptionsRequest
├── Annotation
├── AnnotationMap
├── AnonOutputValue
├── AnonOutputValues
├── AnonOutputWithReport
├── AnyASTAlterAction
├── AnyASTAlterStatementBase
├── AnyASTBreakContinueStatement
├── AnyASTColumnAttribute
├── AnyASTColumnSchema
├── AnyASTCreateFunctionStmtBase
├── AnyASTCreateSchemaStmtBase
├── AnyASTCreateStatement
├── AnyASTCreateTableStmtBase
├── AnyASTCreateViewStatementBase
├── AnyASTDdlStatement
├── AnyASTDropIndexStatement
├── AnyASTElementTypeColumnSchema
├── AnyASTExpression
├── AnyASTGeneralizedPathExpression
├── AnyASTGqlCallBase
├── AnyASTGqlOperator
├── AnyASTGraphElementPattern
├── AnyASTGraphLabelExpression
├── AnyASTGraphPathBase
├── AnyASTLeaf
├── AnyASTLoopStatement
├── AnyASTNode
├── AnyASTParameterExprBase
├── AnyASTPipeOperator
├── AnyASTPostfixTableOperator
├── AnyASTPrintableLeaf
├── AnyASTQuantifier
├── AnyASTQueryExpression
├── AnyASTRowPatternExpression
├── AnyASTScriptStatement
├── AnyASTStatement
├── AnyASTTableConstraint
├── AnyASTTableDataSource
├── AnyASTTableElement
├── AnyASTTableExpression
├── AnyASTTransactionMode
├── AnyASTType
├── AnyResolvedAggregateScanBase
├── AnyResolvedAlterAction
├── AnyResolvedAlterColumnAction
├── AnyResolvedAlterObjectStmt
├── AnyResolvedArgument
├── AnyResolvedComputedColumnBase
├── AnyResolvedComputedColumnImpl
├── AnyResolvedConstraint
├── AnyResolvedCreateSchemaStmtBase
├── AnyResolvedCreateStatement
├── AnyResolvedCreateTableStmtBase
├── AnyResolvedCreateViewBase
├── AnyResolvedExpr
├── AnyResolvedFunctionCallBase
├── AnyResolvedGrantOrRevokeStmt
├── AnyResolvedGraphElementScan
├── AnyResolvedGraphLabelExpr
├── AnyResolvedGraphPathScanBase
├── AnyResolvedGraphScanBase
├── AnyResolvedGroupingSetBase
├── AnyResolvedMatchRecognizePatternExpr
├── AnyResolvedNode
├── AnyResolvedNonScalarFunctionCallBase
├── AnyResolvedScan
├── AnyResolvedStatement
├── ArgumentTypeLambda
├── ArrayFindEnums
├── ArrayType
├── ArrayZipEnums
├── BitwiseAggEnums
├── BoundingReport
├── BuildSqlRequest
├── BuildSqlResponse
├── Collation
├── Column
├── ColumnRef
├── CompiledPattern
├── ComplianceTestCaseLabels
├── ComplianceTestsLabels
├── ConnectionRef
├── ConstantRef
├── ConstnessLevel
├── DeprecatedEncoding
├── DeprecationWarning
├── DescriptorPoolIdList
├── DescriptorPoolList
├── DifferentialPrivacyBoundingReport
├── DifferentialPrivacyEnums
├── DifferentialPrivacyOutputValue
├── DifferentialPrivacyOutputValues
├── DifferentialPrivacyOutputWithReport
├── DifferentiallyPrivateCountDistinctBoundingReport
├── Edits
├── EnabledRewrite
├── EnumType
├── ErrorFixSuggestions
├── ErrorLocation
├── ErrorMessageModeForPayload
├── ErrorSource
├── EvaluateModifyBatchRequest
├── EvaluateModifyBatchResponse
├── EvaluateModifyRequest
├── EvaluateModifyResponse
├── EvaluateQueryBatchRequest
├── EvaluateQueryBatchResponse
├── EvaluateQueryRequest
├── EvaluateQueryResponse
├── EvaluateRequest
├── EvaluateRequestBatch
├── EvaluateResponse
├── EvaluateResponseBatch
├── EvaluatorTableIterator
├── ExecutionStats
├── ExpressionAttribute
├── ExtendedTypeParameters
├── ExtractTableNamesFromNextStatementRequest
├── ExtractTableNamesFromNextStatementResponse
├── ExtractTableNamesFromStatementRequest
├── ExtractTableNamesFromStatementResponse
├── FeatureLabelDictionary
├── FieldDescriptorRef
├── FieldFormat
├── Fix
├── FixRange
├── FormatSqlRequest
├── FormatSqlResponse
├── FormatterOptions
├── FormatterRange
├── FreestandingDeprecationWarning
├── Function
├── FunctionArgumentType
├── FunctionArgumentTypeOptions
├── FunctionEnums
├── FunctionOptions
├── FunctionRef
├── FunctionSignature
├── FunctionSignatureOptions
├── FunctionSignatureRewriteOptions
├── GetBuiltinFunctionsResponse
├── GraphElementLabel
├── GraphElementLabelRef
├── GraphElementTable
├── GraphElementTableRef
├── GraphElementType
├── GraphNodeTableReference
├── GraphPathType
├── GraphPropertyDeclaration
├── GraphPropertyDeclarationRef
├── GraphPropertyDefinition
├── GroupingSetRewriteOptions
├── InternalEdits
├── InternalErrorFixSuggestions
├── InternalErrorLocation
├── InternalFix
├── InternalFixRange
├── InternalTextEdit
├── KnownErrorEntry
├── KnownErrorFile
├── LanguageFeatureOptions
├── LanguageOptionsRequest
├── MapType
├── MatchPartitionResult
├── MatchResult
├── MeasureType
├── ModelRef
├── ModuleOptions
├── NoiseConfidenceInterval
├── NumericTypeParameters
├── OneofDescriptorRef
├── OpaqueEnumTypeOptions
├── OpaqueEnumValueOptions
├── Parameter
├── ParseLocationRange
├── ParseRequest
├── ParseResponse
├── ParseResumeLocation
├── ParserErrorContext
├── PerModuleOptions
├── PlaceholderDescriptor
├── PrepareModifyRequest
├── PrepareModifyResponse
├── PrepareQueryRequest
├── PrepareQueryResponse
├── PrepareRequest
├── PrepareResponse
├── PreparedModifyState
├── PreparedQueryState
├── PreparedState
├── Procedure
├── ProcedureExtension
├── ProcedureRef
├── PropertyGraph
├── PropertyGraphRef
├── ProtoType
├── RangeSessionizeEnums
├── RangeType
├── RankTypeEnums
├── RegisterCatalogRequest
├── RegisterResponse
├── ResolvedASTRewriteOptions
├── ResolvedAggregateHavingModifierEnums
├── ResolvedAlterIndexStmtEnums
├── ResolvedArgumentDefEnums
├── ResolvedAuxLoadDataStmtEnums
├── ResolvedBeginStmtEnums
├── ResolvedCollation
├── ResolvedColumn
├── ResolvedCreateStatementEnums
├── ResolvedDropIndexStmtEnums
├── ResolvedDropStmtEnums
├── ResolvedForeignKeyEnums
├── ResolvedFunctionCallBaseEnums
├── ResolvedFunctionCallInfo
├── ResolvedGeneratedColumnInfoEnums
├── ResolvedGraphEdgeScanEnums
├── ResolvedGraphLabelNaryExprEnums
├── ResolvedGraphPathModeEnums
├── ResolvedGraphPathSearchPrefixEnums
├── ResolvedImportStmtEnums
├── ResolvedInsertStmtEnums
├── ResolvedJoinScanEnums
├── ResolvedLockModeEnums
├── ResolvedMatchRecognizePatternAnchorEnums
├── ResolvedMatchRecognizePatternOperationEnums
├── ResolvedMatchRecognizeScanEnums
├── ResolvedMergeWhenEnums
├── ResolvedNode
│   ├── ResolvedArgument
│   │   ├── ResolvedAggregateHavingModifier
│   │   ├── ResolvedAlterAction
│   │   │   ├── ResolvedAddColumnAction
│   │   │   ├── ResolvedAddColumnIdentifierAction
│   │   │   ├── ResolvedAddConstraintAction
│   │   │   ├── ResolvedAddSubEntityAction
│   │   │   ├── ResolvedAddToRestricteeListAction
│   │   │   ├── ResolvedAlterColumnAction
│   │   │   │   ├── ResolvedAlterColumnDropDefaultAction
│   │   │   │   ├── ResolvedAlterColumnDropGeneratedAction
│   │   │   │   ├── ResolvedAlterColumnDropNotNullAction
│   │   │   │   ├── ResolvedAlterColumnOptionsAction
│   │   │   │   ├── ResolvedAlterColumnSetDataTypeAction
│   │   │   │   ├── ResolvedAlterColumnSetDefaultAction
│   │   │   │   └── ResolvedAlterColumnSetGeneratedAction
│   │   │   ├── ResolvedAlterSubEntityAction
│   │   │   ├── ResolvedDropColumnAction
│   │   │   ├── ResolvedDropConstraintAction
│   │   │   ├── ResolvedDropPrimaryKeyAction
│   │   │   ├── ResolvedDropSubEntityAction
│   │   │   ├── ResolvedFilterUsingAction
│   │   │   ├── ResolvedGrantToAction
│   │   │   ├── ResolvedRebuildAction
│   │   │   ├── ResolvedRemoveFromRestricteeListAction
│   │   │   ├── ResolvedRenameColumnAction
│   │   │   ├── ResolvedRenameToAction
│   │   │   ├── ResolvedRestrictToAction
│   │   │   ├── ResolvedRevokeFromAction
│   │   │   ├── ResolvedSetAsAction
│   │   │   ├── ResolvedSetCollateClause
│   │   │   └── ResolvedSetOptionsAction
│   │   ├── ResolvedAnalyticFunctionGroup
│   │   ├── ResolvedArgumentDef
│   │   ├── ResolvedArgumentList
│   │   ├── ResolvedAssertRowsModified
│   │   ├── ResolvedAuxLoadDataPartitionFilter
│   │   ├── ResolvedColumnAnnotations
│   │   ├── ResolvedColumnDefaultValue
│   │   ├── ResolvedColumnDefinition
│   │   ├── ResolvedColumnHolder
│   │   ├── ResolvedComputedColumnBase
│   │   │   └── ResolvedComputedColumnImpl
│   │   │       ├── ResolvedComputedColumn
│   │   │       └── ResolvedDeferredComputedColumn
│   │   ├── ResolvedConnection
│   │   ├── ResolvedConstraint
│   │   │   ├── ResolvedCheckConstraint
│   │   │   ├── ResolvedForeignKey
│   │   │   └── ResolvedPrimaryKey
│   │   ├── ResolvedCreateModelAliasedQuery
│   │   ├── ResolvedDMLValue
│   │   ├── ResolvedDescriptor
│   │   ├── ResolvedExecuteImmediateArgument
│   │   ├── ResolvedExtendedCast
│   │   ├── ResolvedExtendedCastElement
│   │   ├── ResolvedFilterFieldArg
│   │   ├── ResolvedFunctionArgument
│   │   ├── ResolvedFunctionSignatureHolder
│   │   ├── ResolvedGeneralizedQuerySubpipeline
│   │   ├── ResolvedGeneratedColumnInfo
│   │   ├── ResolvedGraphDynamicLabelSpecification
│   │   ├── ResolvedGraphDynamicPropertiesSpecification
│   │   ├── ResolvedGraphElementIdentifier
│   │   ├── ResolvedGraphElementLabel
│   │   ├── ResolvedGraphElementProperty
│   │   ├── ResolvedGraphElementTable
│   │   ├── ResolvedGraphLabelExpr
│   │   │   ├── ResolvedGraphLabel
│   │   │   ├── ResolvedGraphLabelNaryExpr
│   │   │   └── ResolvedGraphWildCardLabel
│   │   ├── ResolvedGraphMakeArrayVariable
│   │   ├── ResolvedGraphNodeTableReference
│   │   ├── ResolvedGraphPathCost
│   │   ├── ResolvedGraphPathMode
│   │   ├── ResolvedGraphPathPatternQuantifier
│   │   ├── ResolvedGraphPathSearchPrefix
│   │   ├── ResolvedGraphPropertyDeclaration
│   │   ├── ResolvedGraphPropertyDefinition
│   │   ├── ResolvedGroupingCall
│   │   ├── ResolvedGroupingSetBase
│   │   │   ├── ResolvedCube
│   │   │   ├── ResolvedGroupingSet
│   │   │   ├── ResolvedGroupingSetList
│   │   │   ├── ResolvedGroupingSetProduct
│   │   │   └── ResolvedRollup
│   │   ├── ResolvedGroupingSetMultiColumn
│   │   ├── ResolvedIdentityColumnInfo
│   │   ├── ResolvedIndexItem
│   │   ├── ResolvedInlineLambda
│   │   ├── ResolvedInsertRow
│   │   ├── ResolvedLockMode
│   │   ├── ResolvedMakeProtoField
│   │   ├── ResolvedMatchRecognizePatternExpr
│   │   │   ├── ResolvedMatchRecognizePatternAnchor
│   │   │   ├── ResolvedMatchRecognizePatternEmpty
│   │   │   ├── ResolvedMatchRecognizePatternOperation
│   │   │   ├── ResolvedMatchRecognizePatternQuantification
│   │   │   └── ResolvedMatchRecognizePatternVariableRef
│   │   ├── ResolvedMatchRecognizeVariableDefinition
│   │   ├── ResolvedMeasureGroup
│   │   ├── ResolvedMergeWhen
│   │   ├── ResolvedModel
│   │   ├── ResolvedObjectUnit
│   │   ├── ResolvedOnConflictClause
│   │   ├── ResolvedOption
│   │   ├── ResolvedOrderByItem
│   │   ├── ResolvedOutputColumn
│   │   ├── ResolvedOutputSchema
│   │   ├── ResolvedPipeIfCase
│   │   ├── ResolvedPivotColumn
│   │   ├── ResolvedPrivilege
│   │   ├── ResolvedRecursionDepthModifier
│   │   ├── ResolvedReplaceFieldItem
│   │   ├── ResolvedReturningClause
│   │   ├── ResolvedSequence
│   │   ├── ResolvedSetOperationItem
│   │   ├── ResolvedSubpipeline
│   │   ├── ResolvedTableAndColumnInfo
│   │   ├── ResolvedUnnestItem
│   │   ├── ResolvedUnpivotArg
│   │   ├── ResolvedUpdateFieldItem
│   │   ├── ResolvedUpdateItem
│   │   ├── ResolvedUpdateItemElement
│   │   ├── ResolvedWindowFrame
│   │   ├── ResolvedWindowFrameExpr
│   │   ├── ResolvedWindowOrdering
│   │   ├── ResolvedWindowPartitioning
│   │   ├── ResolvedWithEntry
│   │   └── ResolvedWithPartitionColumns
│   ├── ResolvedExpr
│   │   ├── ResolvedArgumentRef
│   │   ├── ResolvedArrayAggregate
│   │   ├── ResolvedCast
│   │   ├── ResolvedCatalogColumnRef
│   │   ├── ResolvedColumnRef
│   │   ├── ResolvedConstant
│   │   ├── ResolvedDMLDefault
│   │   ├── ResolvedExpressionColumn
│   │   ├── ResolvedFilterField
│   │   ├── ResolvedFlatten
│   │   ├── ResolvedFlattenedArg
│   │   ├── ResolvedFunctionCallBase
│   │   │   ├── ResolvedFunctionCall
│   │   │   └── ResolvedNonScalarFunctionCallBase
│   │   │       ├── ResolvedAggregateFunctionCall
│   │   │       └── ResolvedAnalyticFunctionCall
│   │   ├── ResolvedGetJsonField
│   │   ├── ResolvedGetProtoField
│   │   ├── ResolvedGetProtoOneof
│   │   ├── ResolvedGetRowField
│   │   ├── ResolvedGetStructField
│   │   ├── ResolvedGraphGetElementProperty
│   │   ├── ResolvedGraphIsLabeledPredicate
│   │   ├── ResolvedGraphMakeElement
│   │   ├── ResolvedLiteral
│   │   ├── ResolvedMakeProto
│   │   ├── ResolvedMakeStruct
│   │   ├── ResolvedParameter
│   │   ├── ResolvedReplaceField
│   │   ├── ResolvedSubqueryExpr
│   │   ├── ResolvedSystemVariable
│   │   ├── ResolvedUpdateConstructor
│   │   └── ResolvedWithExpr
│   ├── ResolvedScan
│   │   ├── ResolvedAggregateScanBase
│   │   │   ├── ResolvedAggregateScan
│   │   │   ├── ResolvedAggregationThresholdAggregateScan
│   │   │   ├── ResolvedAnonymizedAggregateScan
│   │   │   └── ResolvedDifferentialPrivacyAggregateScan
│   │   ├── ResolvedAnalyticScan
│   │   ├── ResolvedArrayScan
│   │   ├── ResolvedAssertScan
│   │   ├── ResolvedBarrierScan
│   │   ├── ResolvedDescribeScan
│   │   ├── ResolvedExecuteAsRoleScan
│   │   ├── ResolvedFilterScan
│   │   ├── ResolvedGraphCallScan
│   │   ├── ResolvedGraphPathScanBase
│   │   │   ├── ResolvedGraphElementScan
│   │   │   │   ├── ResolvedGraphEdgeScan
│   │   │   │   └── ResolvedGraphNodeScan
│   │   │   └── ResolvedGraphPathScan
│   │   ├── ResolvedGraphRefScan
│   │   ├── ResolvedGraphScanBase
│   │   │   ├── ResolvedGraphLinearScan
│   │   │   └── ResolvedGraphScan
│   │   ├── ResolvedGraphTableScan
│   │   ├── ResolvedGroupRowsScan
│   │   ├── ResolvedJoinScan
│   │   ├── ResolvedLimitOffsetScan
│   │   ├── ResolvedLogScan
│   │   ├── ResolvedMatchRecognizeScan
│   │   ├── ResolvedOrderByScan
│   │   ├── ResolvedPipeCreateTableScan
│   │   ├── ResolvedPipeExportDataScan
│   │   ├── ResolvedPipeForkScan
│   │   ├── ResolvedPipeIfScan
│   │   ├── ResolvedPipeInsertScan
│   │   ├── ResolvedPipeTeeScan
│   │   ├── ResolvedPivotScan
│   │   ├── ResolvedProjectScan
│   │   ├── ResolvedRecursiveRefScan
│   │   ├── ResolvedRecursiveScan
│   │   ├── ResolvedRelationArgumentScan
│   │   ├── ResolvedSampleScan
│   │   ├── ResolvedSetOperationScan
│   │   ├── ResolvedSingleRowScan
│   │   ├── ResolvedStaticDescribeScan
│   │   ├── ResolvedSubpipelineInputScan
│   │   ├── ResolvedTVFScan
│   │   ├── ResolvedTableScan
│   │   ├── ResolvedUnpivotScan
│   │   ├── ResolvedUnsetArgumentScan
│   │   ├── ResolvedWithRefScan
│   │   └── ResolvedWithScan
│   └── ResolvedStatement
│       ├── ResolvedAbortBatchStmt
│       ├── ResolvedAlterObjectStmt
│       │   ├── ResolvedAlterAllRowAccessPoliciesStmt
│       │   ├── ResolvedAlterApproxViewStmt
│       │   ├── ResolvedAlterConnectionStmt
│       │   ├── ResolvedAlterDatabaseStmt
│       │   ├── ResolvedAlterEntityStmt
│       │   ├── ResolvedAlterExternalSchemaStmt
│       │   ├── ResolvedAlterIndexStmt
│       │   ├── ResolvedAlterMaterializedViewStmt
│       │   ├── ResolvedAlterModelStmt
│       │   ├── ResolvedAlterPrivilegeRestrictionStmt
│       │   ├── ResolvedAlterRowAccessPolicyStmt
│       │   ├── ResolvedAlterSchemaStmt
│       │   ├── ResolvedAlterSequenceStmt
│       │   ├── ResolvedAlterTableStmt
│       │   └── ResolvedAlterViewStmt
│       ├── ResolvedAlterTableSetOptionsStmt
│       ├── ResolvedAnalyzeStmt
│       ├── ResolvedAssertStmt
│       ├── ResolvedAssignmentStmt
│       ├── ResolvedAuxLoadDataStmt
│       ├── ResolvedBeginStmt
│       ├── ResolvedCallStmt
│       ├── ResolvedCloneDataStmt
│       ├── ResolvedCommitStmt
│       ├── ResolvedCreateDatabaseStmt
│       ├── ResolvedCreateRowAccessPolicyStmt
│       ├── ResolvedCreateStatement
│       │   ├── ResolvedCreateConnectionStmt
│       │   ├── ResolvedCreateConstantStmt
│       │   ├── ResolvedCreateEntityStmt
│       │   ├── ResolvedCreateFunctionStmt
│       │   ├── ResolvedCreateIndexStmt
│       │   ├── ResolvedCreateModelStmt
│       │   ├── ResolvedCreatePrivilegeRestrictionStmt
│       │   ├── ResolvedCreateProcedureStmt
│       │   ├── ResolvedCreatePropertyGraphStmt
│       │   ├── ResolvedCreateSchemaStmtBase
│       │   │   ├── ResolvedCreateExternalSchemaStmt
│       │   │   └── ResolvedCreateSchemaStmt
│       │   ├── ResolvedCreateSequenceStmt
│       │   ├── ResolvedCreateSnapshotTableStmt
│       │   ├── ResolvedCreateTableFunctionStmt
│       │   ├── ResolvedCreateTableStmtBase
│       │   │   ├── ResolvedCreateExternalTableStmt
│       │   │   ├── ResolvedCreateTableAsSelectStmt
│       │   │   └── ResolvedCreateTableStmt
│       │   └── ResolvedCreateViewBase
│       │       ├── ResolvedCreateApproxViewStmt
│       │       ├── ResolvedCreateMaterializedViewStmt
│       │       └── ResolvedCreateViewStmt
│       ├── ResolvedCreateWithEntryStmt
│       ├── ResolvedDefineTableStmt
│       ├── ResolvedDeleteStmt
│       ├── ResolvedDescribeStmt
│       ├── ResolvedDropFunctionStmt
│       ├── ResolvedDropIndexStmt
│       ├── ResolvedDropMaterializedViewStmt
│       ├── ResolvedDropPrivilegeRestrictionStmt
│       ├── ResolvedDropRowAccessPolicyStmt
│       ├── ResolvedDropSnapshotTableStmt
│       ├── ResolvedDropStmt
│       ├── ResolvedDropTableFunctionStmt
│       ├── ResolvedExecuteImmediateStmt
│       ├── ResolvedExplainStmt
│       ├── ResolvedExportDataStmt
│       ├── ResolvedExportMetadataStmt
│       ├── ResolvedExportModelStmt
│       ├── ResolvedGeneralizedQueryStmt
│       ├── ResolvedGrantOrRevokeStmt
│       │   ├── ResolvedGrantStmt
│       │   └── ResolvedRevokeStmt
│       ├── ResolvedImportStmt
│       ├── ResolvedInsertStmt
│       ├── ResolvedMergeStmt
│       ├── ResolvedModuleStmt
│       ├── ResolvedMultiStmt
│       ├── ResolvedQueryStmt
│       ├── ResolvedRenameStmt
│       ├── ResolvedRollbackStmt
│       ├── ResolvedRunBatchStmt
│       ├── ResolvedSetTransactionStmt
│       ├── ResolvedShowStmt
│       ├── ResolvedStartBatchStmt
│       ├── ResolvedStatementWithPipeOperatorsStmt
│       ├── ResolvedSubpipelineStmt
│       ├── ResolvedTruncateStmt
│       ├── ResolvedUndropStmt
│       └── ResolvedUpdateStmt
├── ResolvedNonScalarFunctionCallBaseEnums
├── ResolvedOnConflictClauseEnums
├── ResolvedOptionEnums
├── ResolvedOrderByItemEnums
├── ResolvedRecursiveScanEnums
├── ResolvedSampleScanEnums
├── ResolvedSetOperationScanEnums
├── ResolvedStatementEnums
├── ResolvedSubqueryExprEnums
├── ResolvedUpdateFieldItemEnums
├── ResolvedWindowFrameEnums
├── ResolvedWindowFrameExprEnums
├── ResultTable
├── RewriteOptions
├── ScriptException
├── ScriptExecutorState
├── SequenceRef
├── SimpleAnonymizationInfo
├── SimpleColumn
├── SimpleConnection
├── SimpleConstant
├── SimpleGraphElementDynamicLabel
├── SimpleGraphElementDynamicProperties
├── SimpleGraphElementLabel
├── SimpleGraphElementTable
├── SimpleGraphNodeTableReference
├── SimpleGraphPropertyDeclaration
├── SimpleGraphPropertyDefinition
├── SimpleModel
├── SimplePropertyGraph
├── SimpleSequence
├── SimpleTable
├── SimpleTokenList
├── SimpleValue
├── StateMachine
├── StringTypeParameters
├── StructField
├── StructType
├── TVFArgument
├── TVFConnection
├── TVFDescriptor
├── TVFGraph
├── TVFModel
├── TVFRelation
├── TVFRelationColumn
├── TVFSignature
├── TVFSignatureOptions
├── TableAlias
├── TableContent
├── TableData
├── TableFromProtoRequest
├── TableRef
├── TableValuedFunction
├── TableValuedFunctionOptions
├── TableValuedFunctionRef
├── TextEdit
├── TextToken
├── TimestampTypeParameters
├── Token
├── TypeModifiers
├── TypeParameters
├── UnprepareModifyRequest
├── UnprepareQueryRequest
├── UnprepareRequest
├── UnregisterRequest
├── UnsupportedFieldsEnum
├── Value
├── ValueWithType
├── Variable
├── WireFormatAnnotationEmptyMessage
└── ZetaSQLBuiltinFunctionOptions
```
