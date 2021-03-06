# Stubs for alembic.ddl.oracle (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import AddColumn, ColumnComment, ColumnDefault, ColumnName, ColumnNullable, ColumnType, alter_table, format_column_name, format_server_default, format_type
from .impl import DefaultImpl
from typing import Any


class OracleImpl(DefaultImpl):
    __dialect__: str = ...
    transactional_ddl: bool = ...
    batch_separator: str = ...
    command_terminator: str = ...

    def __init__(self, *arg: Any, **kw: Any) -> None:
        ...

    def emit_begin(self) -> None:
        ...

    def emit_commit(self) -> None:
        ...


def visit_add_column(element: Any, compiler: Any, **kw: Any):
    ...


def visit_column_nullable(element: Any, compiler: Any, **kw: Any):
    ...


def visit_column_type(element: Any, compiler: Any, **kw: Any):
    ...


def visit_column_name(element: Any, compiler: Any, **kw: Any):
    ...


def visit_column_default(element: Any, compiler: Any, **kw: Any):
    ...


def visit_column_comment(element: Any, compiler: Any, **kw: Any):
    ...


def alter_column(compiler: Any, name: Any):
    ...


def add_column(compiler: Any, column: Any, **kw: Any):
    ...
