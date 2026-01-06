from dataclasses import dataclass

from zetasql.types.proto_model.generated import (
    Function,
    SimpleConstant,
    SimpleTable,
    TableValuedFunction,
)
from zetasql.types.proto_model.generated import (
    SimpleCatalog as _GeneratedSimpleCatalog,
)


@dataclass
class SimpleCatalog(_GeneratedSimpleCatalog):
    """SimpleCatalog with Java-compatible convenience methods.

    Extends the generated SimpleCatalog ProtoModel with convenience methods
    for adding and retrieving functions, TVFs, and constants.

    Mirrors the Java SimpleCatalog API for consistency.
    """

    def _check_duplicate(self, items: list, name_path: list[str], item_type: str) -> None:
        """Check for duplicate items in catalog (case-insensitive)."""
        if not name_path:
            return
        new_name = name_path[-1].lower()
        for item in items:
            if item.name_path and item.name_path[-1].lower() == new_name:
                raise ValueError(f"{item_type} '{name_path[-1]}' already exists in catalog")

    def _find_by_name(self, items: list, target_name: str, use_name_path: bool = True) -> any:
        """Find item by name (case-insensitive)."""
        target_name = target_name.lower()
        for item in items:
            if use_name_path:
                if item.name_path:
                    item_name = item.name_path[-1]
                    if item_name.lower() == target_name:
                        return item
            else:
                if item.name and item.name.lower() == target_name:
                    return item
        return None

    # === Function Operations ===

    def add_function(self, function: Function) -> None:
        """Add function to catalog.

        Args:
            function: Function ProtoModel (typically from FunctionBuilder)

        Raises:
            ValueError: If function with same name already exists (case-insensitive)

        Examples:
            >>> from zetasql.api import FunctionBuilder, SignatureBuilder
            >>> func = FunctionBuilder("MY_UDF").add_signature(...).build()
            >>> catalog.add_function(func)
        """
        self._check_duplicate(self.custom_function, function.name_path, "Function")
        self.custom_function.append(function)

    def get_function_list(self) -> list[Function]:
        """Get all custom functions in catalog.

        Returns:
            List of Function ProtoModels

        Examples:
            >>> functions = catalog.get_function_list()
            >>> for func in functions:
            ...     print(func.name_path)
        """
        return list(self.custom_function)

    def get_function_by_full_name(self, full_name: str) -> Function | None:
        """Get function by full name (case-insensitive).

        Args:
            full_name: Full function name (e.g., "zetasql:MY_UDF" or "MY_UDF")

        Returns:
            Function if found, None otherwise

        Examples:
            >>> func = catalog.get_function_by_full_name("zetasql:MY_UDF")
            >>> if func:
            ...     print(f"Found: {func.name_path}")
        """
        # Normalize to lowercase for case-insensitive comparison (Java uses Ascii.toLowerCase)
        target_name = full_name.lower()

        for func in self.custom_function:
            # Construct full name from name_path and group
            # Format: "group:name" or just "name" if single part
            if func.name_path:
                func_name = func.name_path[-1]  # Last part is the name

                # Try matching with group prefix (e.g., "zetasql:MY_UDF")
                if func.group:
                    full_func_name = f"{func.group}:{func_name}"
                    if full_func_name.lower() == target_name:
                        return func

                # Also try matching just the name
                if func_name.lower() == target_name:
                    return func

        return None

    def get_function_name_list(self) -> list[str]:
        """Get list of all function names.

        Returns:
            List of function names

        Examples:
            >>> names = catalog.get_function_name_list()
            >>> print(names)  # ['MY_UDF', 'ANOTHER_FUNC']
        """
        names = []
        for func in self.custom_function:
            if func.name_path:
                names.append(func.name_path[-1])
        return names

    # === Table-Valued Function Operations ===

    def add_table_valued_function(self, tvf: TableValuedFunction) -> None:
        """Add table-valued function to catalog.

        Args:
            tvf: TableValuedFunction ProtoModel (typically from TVFBuilder)

        Raises:
            ValueError: If TVF with same name already exists (case-insensitive)

        Examples:
            >>> from zetasql.api import TVFBuilder
            >>> tvf = TVFBuilder("my_tvf").add_argument(...).build()
            >>> catalog.add_table_valued_function(tvf)
        """
        self._check_duplicate(self.custom_tvf, tvf.name_path, "Table-valued function")
        self.custom_tvf.append(tvf)

    def get_tvf_list(self) -> list[TableValuedFunction]:
        """Get all custom table-valued functions in catalog.

        Returns:
            List of TableValuedFunction ProtoModels

        Examples:
            >>> tvfs = catalog.get_tvf_list()
            >>> for tvf in tvfs:
            ...     print(tvf.name_path)
        """
        return list(self.custom_tvf)

    def get_tvf_by_full_name(self, full_name: str) -> TableValuedFunction | None:
        """Get TVF by full name (case-insensitive).

        Args:
            full_name: Full TVF name (e.g., "zetasql:my_tvf" or "my_tvf")

        Returns:
            TableValuedFunction if found, None otherwise

        Examples:
            >>> tvf = catalog.get_tvf_by_full_name("my_tvf")
            >>> if tvf:
            ...     print(f"Found: {tvf.name_path}")
        """
        return self._find_by_name(self.custom_tvf, full_name)

    def get_tvf_name_list(self) -> list[str]:
        """Get list of all TVF names.

        Returns:
            List of TVF names

        Examples:
            >>> names = catalog.get_tvf_name_list()
            >>> print(names)  # ['my_tvf', 'filter_table']
        """
        names = []
        for tvf in self.custom_tvf:
            if tvf.name_path:
                names.append(tvf.name_path[-1])
        return names

    # === Constant Operations ===

    def add_constant(self, constant: SimpleConstant) -> None:
        """Add constant to catalog.

        Args:
            constant: SimpleConstant ProtoModel (typically from ConstantBuilder)

        Raises:
            ValueError: If constant with same name already exists (case-insensitive)

        Examples:
            >>> from zetasql.api import ConstantBuilder
            >>> const = ConstantBuilder("MAX_LIMIT").set_type(...).build()
            >>> catalog.add_constant(const)
        """
        self._check_duplicate(self.constant, constant.name_path, "Constant")
        self.constant.append(constant)

    def get_constant_list(self) -> list[SimpleConstant]:
        """Get all constants in catalog.

        Returns:
            List of SimpleConstant ProtoModels

        Examples:
            >>> constants = catalog.get_constant_list()
            >>> for const in constants:
            ...     print(const.name_path)
        """
        return list(self.constant)

    def get_constant(self, name: str) -> SimpleConstant | None:
        """Get constant by name (case-insensitive).

        Args:
            name: Constant name

        Returns:
            SimpleConstant if found, None otherwise

        Examples:
            >>> const = catalog.get_constant("MAX_LIMIT")
            >>> if const:
            ...     print(f"Found: {const.name_path}")
        """
        return self._find_by_name(self.constant, name)

    # === Table Operations ===

    def get_table_list(self) -> list[SimpleTable]:
        """Get all tables in catalog.

        Returns:
            List of SimpleTable ProtoModels

        Examples:
            >>> tables = catalog.get_table_list()
            >>> for table in tables:
            ...     print(table.name)
        """
        return list(self.table)

    def get_table(self, name: str) -> SimpleTable | None:
        """Get table by name (case-insensitive).

        Args:
            name: Table name

        Returns:
            SimpleTable if found, None otherwise

        Examples:
            >>> table = catalog.get_table("Orders")
            >>> if table:
            ...     print(f"Found: {table.name}")
            >>>
            >>> # Case-insensitive
            >>> table = catalog.get_table("ORDERS")  # Same as "Orders"
        """
        return self._find_by_name(self.table, name, use_name_path=False)

    def get_table_name_list(self) -> list[str]:
        """Get list of all table names.

        Returns:
            List of table names

        Examples:
            >>> names = catalog.get_table_name_list()
            >>> print(names)  # ['Orders', 'Products', 'Customers']
        """
        return [table.name for table in self.table if table.name]
