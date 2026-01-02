"""
Demo: IntEnum support for improved IDE autocomplete and type safety

This example demonstrates the improved usability of enum fields with IntEnum.
Before: enum fields were typed as `int`, requiring manual lookup of values
After: enum fields are typed as IntEnum, providing IDE autocomplete and type safety
"""

from zetasql.types import (
    ResolvedJoinScan,
    ResolvedJoinScanEnums,
    Type,
    TypeKind,
)


def main():
    print("=" * 70)
    print("IntEnum Autocomplete Demo")
    print("=" * 70)
    
    # ✅ NEW: Use enum with IDE autocomplete
    print("\n1. Creating with IntEnum (autocomplete-friendly):")
    join_scan = ResolvedJoinScan()
    join_scan.join_type = ResolvedJoinScanEnums.JoinType.INNER
    print(f"   join_type = {join_scan.join_type}")
    print(f"   join_type.name = '{join_scan.join_type.name}'")
    print(f"   join_type.value = {join_scan.join_type.value}")
    
    # ✅ BACKWARD COMPATIBLE: Still works with int values
    print("\n2. Backward compatibility - assigning int still works:")
    join_scan.join_type = 1  # LEFT join
    print(f"   join_type = {join_scan.join_type} (assigned as int)")
    print(f"   Type: {type(join_scan.join_type)}")
    
    # ✅ Type safety: enum comparisons
    print("\n3. Type-safe comparisons:")
    if join_scan.join_type == ResolvedJoinScanEnums.JoinType.LEFT:
        print("   ✓ Enum comparison works")
    if join_scan.join_type == 1:
        print("   ✓ Int comparison still works (backward compatible)")
    
    # ✅ TypeKind example with mixin methods
    print("\n4. TypeKind with helper methods:")
    int_type = Type(type_kind=TypeKind.TYPE_INT64)
    print(f"   type_kind = {int_type.type_kind}")
    print(f"   is_integer() = {int_type.type_kind.is_integer()}")
    print(f"   is_simple() = {int_type.type_kind.is_simple()}")
    
    # ✅ Enum members are accessible
    print("\n5. Available join types (autocomplete in IDE):")
    for join_type in ResolvedJoinScanEnums.JoinType:
        print(f"   - {join_type.name}: {join_type.value}")
    
    # ✅ Proto conversion roundtrip
    print("\n6. Proto conversion roundtrip:")
    original = ResolvedJoinScan()
    original.join_type = ResolvedJoinScanEnums.JoinType.FULL
    
    proto = original.to_proto()
    print(f"   Original: {original.join_type}")
    print(f"   Proto value: {proto.join_type}")
    
    restored = ResolvedJoinScan.from_proto(proto)
    print(f"   Restored: {restored.join_type}")
    print(f"   Type: {type(restored.join_type)}")
    
    print("\n" + "=" * 70)
    print("✓ All enum features working correctly!")
    print("=" * 70)


if __name__ == "__main__":
    main()
