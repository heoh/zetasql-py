from dataclasses import dataclass
from typing import List, Optional
from zetasql.core.types.proto_models import (
    SimpleCatalog as _GeneratedSimpleCatalog,
    Function,
    TableValuedFunction,
    SimpleConstant,
)


@dataclass
class SimpleCatalog(_GeneratedSimpleCatalog):
    """SimpleCatalog with Java-compatible convenience methods.
    
    Extends the generated SimpleCatalog ProtoModel with convenience methods
    for adding and retrieving functions, TVFs, and constants.
    
    Mirrors the Java SimpleCatalog API for consistency.
    """
    
    # === Function Operations ===
    
    def add_function(self, function: Function) -> None:
        """Add function to catalog.
        
        Args:
            function: Function ProtoModel (typically from FunctionBuilder)
        
        Examples:
            >>> from zetasql.api.builders import FunctionBuilder, SignatureBuilder
            >>> func = FunctionBuilder("MY_UDF").add_signature(...).build()
            >>> catalog.add_function(func)
        """
        self.custom_function.append(function)
    
    def get_function_list(self) -> List[Function]:
        """Get all custom functions in catalog.
        
        Returns:
            List of Function ProtoModels
        
        Examples:
            >>> functions = catalog.get_function_list()
            >>> for func in functions:
            ...     print(func.name_path)
        """
        return list(self.custom_function)
    
    def get_function_by_full_name(self, full_name: str) -> Optional[Function]:
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
    
    def get_function_name_list(self) -> List[str]:
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
        
        Examples:
            >>> from zetasql.api.builders import TVFBuilder
            >>> tvf = TVFBuilder("my_tvf").add_argument(...).build()
            >>> catalog.add_table_valued_function(tvf)
        """
        self.custom_tvf.append(tvf)
    
    def get_tvf_list(self) -> List[TableValuedFunction]:
        """Get all custom table-valued functions in catalog.
        
        Returns:
            List of TableValuedFunction ProtoModels
        
        Examples:
            >>> tvfs = catalog.get_tvf_list()
            >>> for tvf in tvfs:
            ...     print(tvf.name_path)
        """
        return list(self.custom_tvf)
    
    def get_tvf_by_full_name(self, full_name: str) -> Optional[TableValuedFunction]:
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
        # Normalize to lowercase for case-insensitive comparison
        target_name = full_name.lower()
        
        for tvf in self.custom_tvf:
            if tvf.name_path:
                tvf_name = tvf.name_path[-1]
                
                # Try matching just the name
                if tvf_name.lower() == target_name:
                    return tvf
        
        return None
    
    def get_tvf_name_list(self) -> List[str]:
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
        
        Examples:
            >>> from zetasql.api.builders import ConstantBuilder
            >>> const = ConstantBuilder("MAX_LIMIT").set_type(...).build()
            >>> catalog.add_constant(const)
        """
        self.constant.append(constant)
    
    def get_constant_list(self) -> List[SimpleConstant]:
        """Get all constants in catalog.
        
        Returns:
            List of SimpleConstant ProtoModels
        
        Examples:
            >>> constants = catalog.get_constant_list()
            >>> for const in constants:
            ...     print(const.name_path)
        """
        return list(self.constant)
    
    def get_constant(self, name: str) -> Optional[SimpleConstant]:
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
        # Normalize to lowercase for case-insensitive comparison (Java behavior)
        target_name = name.lower()
        
        for const in self.constant:
            if const.name_path:
                const_name = const.name_path[-1]
                if const_name.lower() == target_name:
                    return const
        
        return None
