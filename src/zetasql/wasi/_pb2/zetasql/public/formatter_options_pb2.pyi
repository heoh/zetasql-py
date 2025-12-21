from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FormatterOptionsProto(_message.Message):
    __slots__ = ("new_line_type", "line_length_limit", "indentation_spaces", "allow_invalid_tokens", "capitalize_keywords", "preserve_line_breaks", "expand_format_ranges", "enforce_single_quotes", "capitalize_functions", "format_structured_strings", "format_comments")
    NEW_LINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_LENGTH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INDENTATION_SPACES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INVALID_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CAPITALIZE_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_LINE_BREAKS_FIELD_NUMBER: _ClassVar[int]
    EXPAND_FORMAT_RANGES_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_SINGLE_QUOTES_FIELD_NUMBER: _ClassVar[int]
    CAPITALIZE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_STRUCTURED_STRINGS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    new_line_type: str
    line_length_limit: int
    indentation_spaces: int
    allow_invalid_tokens: bool
    capitalize_keywords: bool
    preserve_line_breaks: bool
    expand_format_ranges: bool
    enforce_single_quotes: bool
    capitalize_functions: bool
    format_structured_strings: bool
    format_comments: bool
    def __init__(self, new_line_type: _Optional[str] = ..., line_length_limit: _Optional[int] = ..., indentation_spaces: _Optional[int] = ..., allow_invalid_tokens: bool = ..., capitalize_keywords: bool = ..., preserve_line_breaks: bool = ..., expand_format_ranges: bool = ..., enforce_single_quotes: bool = ..., capitalize_functions: bool = ..., format_structured_strings: bool = ..., format_comments: bool = ...) -> None: ...

class FormatterRangeProto(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
