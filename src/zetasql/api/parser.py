"""Parser helper class for SQL parsing operations.

Provides Java-style Parser with both instance and static methods
for simplified SQL parsing (syntax analysis only, no semantic analysis).

Parser returns parse tree AST (ASTStatement, ASTScript) without type checking
or name resolution, making it faster than Analyzer and suitable for:
- Syntax validation
- AST inspection and traversal
- Quick statement extraction

Use with ASTNodeVisitor for AST traversal.
"""

from __future__ import annotations

import zetasql.types
from zetasql.core.local_service import ZetaSqlLocalService


class Parser:
    """Helper class for SQL parsing operations (syntax only).

    Equivalent to Java's Parser class with static and instance methods.
    Performs syntax parsing only - returns parse tree without semantic analysis.
    Does not require a catalog.

    Unlike Analyzer which returns ResolvedStatement (with semantic analysis),
    Parser returns ASTStatement (parse tree only).

    Example (instance usage):
        >>> parser = Parser(options)
        >>> stmt = parser.parse_statement("SELECT * FROM Orders")
        >>> script = parser.parse_script("SELECT 1; SELECT 2;")

    Example (static usage):
        >>> stmt = Parser.parse_statement_static("SELECT 1")
        >>> script = Parser.parse_script_static("SELECT 1; SELECT 2;")

    Example (with ASTNodeVisitor):
        >>> from zetasql.api import Parser, ASTNodeVisitor
        >>> stmt = Parser.parse_statement_static("SELECT * FROM Orders")
        >>> visitor = MyCustomVisitor()
        >>> visitor.visit(stmt)
    """

    def __init__(
        self,
        options: zetasql.types.LanguageOptions | None = None,
        service: ZetaSqlLocalService | None = None,
    ):
        """Initialize Parser with language options.

        Args:
            options: Language options for parsing (optional, uses defaults if not provided)
            service: Optional LocalService instance (uses singleton if not provided)

        Example:
            >>> options = LanguageOptions()
            >>> options.set_enabled_language_features([...])
            >>> parser = Parser(options)
        """
        self.options = options
        self.service = service or ZetaSqlLocalService.get_instance()

    def parse_statement(self, sql: str) -> zetasql.types.ASTStatement:
        """Parse SQL statement and return AST.

        Args:
            sql: SQL statement to parse

        Returns:
            Parse tree AST (ASTStatement or subclass)

        Raises:
            ZetaSQLError: If parsing fails (syntax error)

        Example:
            >>> stmt = parser.parse_statement("SELECT id FROM Orders WHERE price > 100")
            >>> print(type(stmt).__name__)  # ASTQueryStatement
        """
        response = self.service.parse(sql_statement=sql, options=self.options)
        return response.parsed_statement

    def parse_script(self, sql: str) -> zetasql.types.ASTScript:
        """Parse SQL script and return AST.

        Parses multiple statements as a script. Allows procedural constructs
        like BEGIN/END blocks when language options permit.

        Args:
            sql: SQL script to parse (can contain multiple statements)

        Returns:
            Parse tree for script (ASTScript)

        Raises:
            ZetaSQLError: If parsing fails

        Example:
            >>> script = parser.parse_script("SELECT 1; SELECT 2; SELECT 3;")
            >>> print(len(script.statement_list_node.statement_list))  # 3
        """
        response = self.service.parse(sql_statement=sql, options=self.options, allow_script=True)
        return response.parsed_script

    def parse_next_statement(
        self,
        location: zetasql.types.ParseResumeLocation,
    ) -> zetasql.types.ASTStatement | None:
        """Parse next statement from location, updating byte_position.

        Args:
            location: ParseResumeLocation that tracks position in the input.
                     Its byte_position will be updated to point after the parsed statement.

        Returns:
            Parsed statement AST, or None if no more statements

        Side effects:
            Updates location.byte_position to point after parsed statement

        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt1 = parser.parse_next_statement(location)
            >>> stmt2 = parser.parse_next_statement(location)
        """
        # Check if we've reached the end of input
        if location.byte_position >= len(location.input):
            return None

        response = self.service.parse(
            sql_statement=location.input,
            parse_resume_location=location,
            options=self.options,
        )

        if hasattr(response, "resume_byte_position") and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position

        return response.parsed_statement if response.parsed_statement else None

    def parse_next_script_statement(
        self,
        location: zetasql.types.ParseResumeLocation,
    ) -> zetasql.types.ASTStatement | None:
        """Parse next script statement (allows procedural constructs).

        Like parse_next_statement but allows script-specific constructs
        like BEGIN/END, IF, WHILE when language options permit.

        Args:
            location: ParseResumeLocation that tracks position.
                     Its byte_position will be updated.

        Returns:
            Parsed statement AST, or None if no more statements

        Side effects:
            Updates location.byte_position

        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt = parser.parse_next_script_statement(location)
        """
        # Check if we've reached the end of input
        if location.byte_position >= len(location.input):
            return None

        response = self.service.parse(
            sql_statement=location.input,
            parse_resume_location=location,
            options=self.options,
            allow_script=True,
        )

        if hasattr(response, "resume_byte_position") and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position

        return response.parsed_statement if response.parsed_statement else None

    @staticmethod
    def parse_statement_static(
        sql: str,
        options: zetasql.types.LanguageOptions | None = None,
    ) -> zetasql.types.ASTStatement:
        """Static method for one-off statement parsing.

        Convenient for single-use parsing without creating a Parser instance.

        Args:
            sql: SQL statement to parse
            options: Optional language options

        Returns:
            Parse tree AST

        Raises:
            ZetaSQLError: If parsing fails

        Example:
            >>> stmt = Parser.parse_statement_static("SELECT * FROM Orders")
            >>> print(type(stmt).__name__)  # ASTQueryStatement
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.parse(sql_statement=sql, options=options)
        return response.parsed_statement

    @staticmethod
    def parse_script_static(
        sql: str,
        options: zetasql.types.LanguageOptions | None = None,
    ) -> zetasql.types.ASTScript:
        """Static method for one-off script parsing.

        Args:
            sql: SQL script to parse
            options: Optional language options

        Returns:
            Parse tree for script (ASTScript)

        Raises:
            ZetaSQLError: If parsing fails

        Example:
            >>> script = Parser.parse_script_static("SELECT 1; SELECT 2;")
            >>> print(len(script.statement_list_node.statement_list))  # 2
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.parse(sql_statement=sql, options=options, allow_script=True)
        return response.parsed_script

    @staticmethod
    def parse_next_statement_static(
        location: zetasql.types.ParseResumeLocation,
        options: zetasql.types.LanguageOptions | None = None,
    ) -> zetasql.types.ASTStatement | None:
        """Static method for parsing next statement in sequence.

        Args:
            location: ParseResumeLocation that tracks position.
                     Its byte_position will be updated.
            options: Optional language options

        Returns:
            Parsed statement AST, or None if no more statements

        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt = Parser.parse_next_statement_static(location)
        """
        # Check if we've reached the end of input
        if location.byte_position >= len(location.input):
            return None

        service = ZetaSqlLocalService.get_instance()
        response = service.parse(
            sql_statement=location.input,
            parse_resume_location=location,
            options=options,
        )

        if hasattr(response, "resume_byte_position") and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position

        return response.parsed_statement if response.parsed_statement else None

    @staticmethod
    def parse_next_script_statement_static(
        location: zetasql.types.ParseResumeLocation,
        options: zetasql.types.LanguageOptions | None = None,
    ) -> zetasql.types.ASTStatement | None:
        """Static method for parsing next script statement.

        Args:
            location: ParseResumeLocation that tracks position.
                     Its byte_position will be updated.
            options: Optional language options

        Returns:
            Parsed statement AST, or None if no more statements

        Example:
            >>> location = ParseResumeLocation(input=script, byte_position=0)
            >>> stmt = Parser.parse_next_script_statement_static(location)
        """
        # Check if we've reached the end of input
        if location.byte_position >= len(location.input):
            return None

        service = ZetaSqlLocalService.get_instance()
        response = service.parse(
            sql_statement=location.input,
            parse_resume_location=location,
            options=options,
            allow_script=True,
        )

        if hasattr(response, "resume_byte_position") and response.resume_byte_position is not None:
            location.byte_position = response.resume_byte_position

        return response.parsed_statement if response.parsed_statement else None

    @staticmethod
    def iterate_statements(
        script: str,
        options: zetasql.types.LanguageOptions | None = None,
    ):
        """Iterate through statements in a script, yielding parsed ASTs.

        This is a generator that lazily parses each statement in the script.
        Similar to Java's Iterator pattern.

        Args:
            script: SQL script with multiple statements
            options: Optional language options

        Yields:
            ASTStatement for each statement in the script

        Raises:
            ZetaSQLError: If parsing fails for any statement

        Example:
            >>> script = "SELECT 1; SELECT 2; SELECT 3;"
            >>> for stmt in Parser.iterate_statements(script):
            ...     print(type(stmt).__name__)
        """
        location = zetasql.types.ParseResumeLocation(input=script, byte_position=0)

        while location.byte_position < len(script):
            stmt = Parser.parse_next_statement_static(location, options)

            if stmt is None:
                break

            yield stmt
