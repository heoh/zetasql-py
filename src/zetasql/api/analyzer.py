"""Analyzer helper class for common analysis operations.

Provides Java-style Analyzer with both instance and static methods
for simplified SQL analysis and AST manipulation.
"""

import zetasql.types
from typing import Optional, List
from zetasql.core.local_service import ZetaSqlLocalService


class Analyzer:
    """Helper class for common analysis operations.
    
    Equivalent to Java's Analyzer class with static and instance methods.
    Simplifies common SQL analysis tasks with convenient APIs.
    
    Example (instance usage):
        >>> analyzer = Analyzer(options, catalog)
        >>> stmt = analyzer.analyze_statement("SELECT * FROM Orders")
        >>> expr = analyzer.analyze_expression("price * quantity")
    
    Example (static usage):
        >>> stmt = Analyzer.analyze_statement_static(sql, options, catalog)
        >>> sql = Analyzer.build_statement(resolved_stmt, catalog)
    """
    
    def __init__(
        self,
        options: zetasql.types.AnalyzerOptions,
        catalog: Optional[zetasql.types.SimpleCatalog] = None,
        service: Optional[ZetaSqlLocalService] = None
    ):
        """Initialize Analyzer with options and catalog.
        
        Args:
            options: Analyzer options to use for all operations
            catalog: Optional catalog for name resolution
            service: Optional LocalService instance (uses singleton if not provided)
        
        Example:
            >>> options = AnalyzerOptions(language_options=lang_opts)
            >>> catalog = CatalogBuilder("db").add_table(table).build()
            >>> analyzer = Analyzer(options, catalog)
        """
        self.options = options
        self.catalog = catalog
        self.service = service or ZetaSqlLocalService.get_instance()
    
    def analyze_statement(self, sql: str) -> zetasql.types.ResolvedStatement:
        """Analyze SQL statement and return resolved AST.
        
        Args:
            sql: SQL statement to analyze
        
        Returns:
            Resolved statement AST (union type - concrete subclass determined at runtime)
        
        Raises:
            AnalyzerError: If analysis fails (syntax error, semantic error, etc.)
        
        Example:
            >>> stmt = analyzer.analyze_statement("SELECT id FROM Orders WHERE price > 100")
            >>> print(type(stmt).__name__)  # ResolvedQueryStmt
        """
        response = self.service.analyze(
            sql_statement=sql,
            options=self.options,
            simple_catalog=self.catalog
        )
        return response.resolved_statement
    
    def analyze_expression(self, expression: str) -> zetasql.types.ResolvedExpr:
        """Analyze SQL expression and return resolved AST.
        
        Args:
            expression: SQL expression to analyze (not a full statement)
        
        Returns:
            Resolved expression AST
        
        Raises:
            AnalyzerError: If analysis fails
        
        Example:
            >>> expr = analyzer.analyze_expression("price * 1.1")
            >>> expr = analyzer.analyze_expression("UPPER(name)")
        """
        response = self.service.analyze(
            sql_expression=expression,
            options=self.options,
            simple_catalog=self.catalog
        )
        return response.resolved_expression
    
    def analyze_next_statement(
        self,
        location: zetasql.types.ParseResumeLocation
    ) -> Optional[zetasql.types.ResolvedStatement]:
        """Analyze next statement in script, updating location.
        
        Args:
            location: ParseResumeLocation that tracks position in the input.
                     Its byte_position will be updated to point after the parsed statement.
        
        Returns:
            Resolved statement, or None if no more statements
        
        Side effects:
            Updates location.byte_position to point after parsed statement
        
        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt1 = analyzer.analyze_next_statement(location)
            >>> stmt2 = analyzer.analyze_next_statement(location)
        """
        response = self.service.analyze(
            sql_statement=location.input,
            parse_resume_location=location,
            options=self.options,
            simple_catalog=self.catalog
        )
        
        # Update location's byte position for next call
        if hasattr(response, 'resume_byte_position') and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position
        
        return response.resolved_statement if response.resolved_statement else None
    
    @staticmethod
    def analyze_statement_static(
        sql: str,
        options: zetasql.types.AnalyzerOptions,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ) -> zetasql.types.ResolvedStatement:
        """Static method for one-off statement analysis.
        
        Convenient for single-use analysis without creating an Analyzer instance.
        
        Args:
            sql: SQL statement
            options: Analyzer options
            catalog: Optional catalog
        
        Returns:
            Resolved statement AST
        
        Raises:
            AnalyzerError: If analysis fails
        
        Example:
            >>> stmt = Analyzer.analyze_statement_static(
            ...     "SELECT * FROM Orders",
            ...     options,
            ...     catalog
            ... )
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.analyze(
            sql_statement=sql,
            options=options,
            simple_catalog=catalog
        )
        return response.resolved_statement
    
    @staticmethod
    def analyze_expression_static(
        expression: str,
        options: zetasql.types.AnalyzerOptions,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ) -> zetasql.types.ResolvedExpr:
        """Static method for one-off expression analysis.
        
        Args:
            expression: SQL expression
            options: Analyzer options
            catalog: Optional catalog
        
        Returns:
            Resolved expression AST
        
        Raises:
            AnalyzerError: If analysis fails
        
        Example:
            >>> expr = Analyzer.analyze_expression_static("price + tax", options, catalog)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.analyze(
            sql_expression=expression,
            options=options,
            simple_catalog=catalog
        )
        return response.resolved_expression
    
    @staticmethod
    def build_statement(
        resolved_stmt: zetasql.types.ResolvedStatement,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ) -> str:
        """Convert resolved AST back to SQL string (unanalyze).
        
        Args:
            resolved_stmt: Resolved statement AST
            catalog: Optional catalog for type resolution
        
        Returns:
            SQL string generated from the AST
        
        Raises:
            ZetaSQLError: If SQL generation fails
        
        Example:
            >>> # Analyze then rebuild
            >>> stmt = Analyzer.analyze_statement_static(original_sql, options, catalog)
            >>> rebuilt_sql = Analyzer.build_statement(stmt, catalog)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.build_sql(
            resolved_statement=resolved_stmt,
            simple_catalog=catalog
        )
        return response.sql
    
    @staticmethod
    def build_expression(
        resolved_expr: zetasql.types.ResolvedExpr,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ) -> str:
        """Convert resolved expression AST back to SQL string.
        
        Args:
            resolved_expr: Resolved expression AST
            catalog: Optional catalog for type resolution
        
        Returns:
            SQL expression string generated from the AST
        
        Raises:
            ZetaSQLError: If SQL generation fails
        
        Example:
            >>> expr = Analyzer.analyze_expression_static("1 + 1", options, catalog)
            >>> sql = Analyzer.build_expression(expr, catalog)
            >>> print(sql)  # "1 + 1" (may be reformatted)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.build_sql(
            resolved_expression=resolved_expr,
            simple_catalog=catalog
        )
        return response.sql
    
    @staticmethod
    def analyze_next_statement_static(
        location: zetasql.types.ParseResumeLocation,
        options: zetasql.types.AnalyzerOptions,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ) -> Optional[zetasql.types.ResolvedStatement]:
        """Static method for analyzing next statement in script.
        
        Args:
            location: ParseResumeLocation that tracks position.
                     Its byte_position will be updated.
            options: Analyzer options
            catalog: Optional catalog
        
        Returns:
            Resolved statement, or None if no more statements
        
        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt = Analyzer.analyze_next_statement_static(location, options, catalog)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.analyze(
            sql_statement=location.input,
            parse_resume_location=location,
            options=options,
            simple_catalog=catalog
        )
        
        # Update location's byte position
        if hasattr(response, 'resume_byte_position') and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position
        
        return response.resolved_statement if response.resolved_statement else None
    
    @staticmethod
    def extract_table_names(sql: str) -> List[str]:
        """Extract table names from SQL without full analysis.
        
        Performs lightweight parsing to extract table references without
        semantic analysis. Useful for dependency tracking and quick inspection.
        
        Args:
            sql: SQL statement
        
        Returns:
            List of table names referenced in the statement
        
        Raises:
            ZetaSQLError: If extraction fails
        
        Example:
            >>> tables = Analyzer.extract_table_names(
            ...     "SELECT * FROM Orders JOIN Products ON Orders.product_id = Products.id"
            ... )
            >>> print(tables)  # ['Orders', 'Products']
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.extract_table_names_from_statement(
            sql_statement=sql
        )
        return response.table_name
    
    @staticmethod
    def extract_table_names_from_script(script: str) -> List['zetasql.types.ExtractTableNamesFromNextStatementResponse.TableName']:
        """Extract all table names from multi-statement script.
        
        Args:
            script: SQL script with multiple statements
        
        Returns:
            List of all table names across all statements
        
        Raises:
            ZetaSQLError: If extraction fails
        
        Example:
            >>> script = "SELECT * FROM T1; SELECT * FROM T2;"
            >>> tables = Analyzer.extract_table_names_from_script(script)
            >>> len(tables)  # 2
        """
        service = ZetaSqlLocalService.get_instance()
        all_tables = []
        location = zetasql.types.ParseResumeLocation(
            input=script,
            byte_position=0
        )
        
        while location.byte_position < len(script):
            try:
                response = service.extract_table_names_from_next_statement(
                    parse_resume_location=location
                )
                
                if response.table_name:
                    all_tables.extend(response.table_name)
                
                # Check for progress to avoid infinite loop
                if response.resume_byte_position <= location.byte_position:
                    break
                
                location.byte_position = response.resume_byte_position
                
            except Exception:
                # Stop on error (e.g., syntax error in script)
                break
        
        return all_tables
    
    @staticmethod
    def iterate_script(
        script: str,
        options: zetasql.types.AnalyzerOptions,
        catalog: Optional[zetasql.types.SimpleCatalog] = None
    ):
        """Iterate through statements in a script, yielding resolved ASTs.
        
        This is a generator that lazily analyzes each statement in the script.
        Similar to Java's Iterator<AnalyzedStatement> pattern.
        
        Args:
            script: SQL script with multiple statements
            options: Analyzer options
            catalog: Optional catalog
        
        Yields:
            ResolvedStatement for each statement in the script
        
        Raises:
            ZetaSQLError: If analysis fails for any statement
        
        Example:
            >>> script = "SELECT 1; SELECT 2; SELECT 3;"
            >>> for stmt in Analyzer.iterate_script(script, options, catalog):
            ...     print(type(stmt).__name__)
        """
        location = zetasql.types.ParseResumeLocation(
            input=script,
            byte_position=0
        )
        
        while location.byte_position < len(script):
            stmt = Analyzer.analyze_next_statement_static(location, options, catalog)
            
            if stmt is None:
                break
            
            yield stmt
