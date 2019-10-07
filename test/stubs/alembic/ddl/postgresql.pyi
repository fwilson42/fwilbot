# Stubs for alembic.ddl.postgresql (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..autogenerate import render
from ..operations import ops, schemaobj
from ..operations.base import BatchOperations, Operations
from ..util import compat, sqla_compat
from .base import AlterColumn, ColumnComment, RenameTable, alter_column, alter_table, compiles, format_table_name, format_type
from .impl import DefaultImpl
from typing import Any, Optional

log: Any

class PostgresqlImpl(DefaultImpl):
    __dialect__: str = ...
    transactional_ddl: bool = ...
    def prep_table_for_batch(self, table: Any) -> None: ...
    def compare_server_default(self, inspector_column: Any, metadata_column: Any, rendered_metadata_default: Any, rendered_inspector_default: Any): ...
    def alter_column(self, table_name: Any, column_name: Any, nullable: Optional[Any] = ..., server_default: bool = ..., name: Optional[Any] = ..., type_: Optional[Any] = ..., schema: Optional[Any] = ..., autoincrement: Optional[Any] = ..., existing_type: Optional[Any] = ..., existing_server_default: Optional[Any] = ..., existing_nullable: Optional[Any] = ..., existing_autoincrement: Optional[Any] = ..., **kw: Any) -> None: ...
    def autogen_column_reflect(self, inspector: Any, table: Any, column_info: Any) -> None: ...
    def correct_for_autogen_constraints(self, conn_unique_constraints: Any, conn_indexes: Any, metadata_unique_constraints: Any, metadata_indexes: Any) -> None: ...
    def render_type(self, type_: Any, autogen_context: Any): ...

class PostgresqlColumnType(AlterColumn):
    type_: Any = ...
    using: Any = ...
    def __init__(self, name: Any, column_name: Any, type_: Any, **kw: Any) -> None: ...

def visit_rename_table(element: Any, compiler: Any, **kw: Any): ...
def visit_column_type(element: Any, compiler: Any, **kw: Any): ...
def visit_column_comment(element: Any, compiler: Any, **kw: Any): ...

class CreateExcludeConstraintOp(ops.AddConstraintOp):
    constraint_type: str = ...
    constraint_name: Any = ...
    table_name: Any = ...
    elements: Any = ...
    where: Any = ...
    schema: Any = ...
    kw: Any = ...
    def __init__(self, constraint_name: Any, table_name: Any, elements: Any, where: Optional[Any] = ..., schema: Optional[Any] = ..., _orig_constraint: Optional[Any] = ..., **kw: Any) -> None: ...
    @classmethod
    def from_constraint(cls, constraint: Any): ...
    def to_constraint(self, migration_context: Optional[Any] = ...): ...
    @classmethod
    def create_exclude_constraint(cls, operations: Any, constraint_name: Any, table_name: Any, *elements: Any, **kw: Any): ...
    @classmethod
    def batch_create_exclude_constraint(cls, operations: Any, constraint_name: Any, *elements: Any, **kw: Any): ...
