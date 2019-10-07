# Stubs for alembic.ddl.mysql (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..autogenerate import compare
from ..util.compat import string_types
from ..util.sqla_compat import _is_mariadb, _is_type_bound
from .base import AlterColumn, ColumnDefault, ColumnName, ColumnNullable, ColumnType, alter_table, format_column_name, format_server_default
from .impl import DefaultImpl
from typing import Any, Optional

class MySQLImpl(DefaultImpl):
    __dialect__: str = ...
    transactional_ddl: bool = ...
    def alter_column(self, table_name: Any, column_name: Any, nullable: Optional[Any] = ..., server_default: bool = ..., name: Optional[Any] = ..., type_: Optional[Any] = ..., schema: Optional[Any] = ..., existing_type: Optional[Any] = ..., existing_server_default: Optional[Any] = ..., existing_nullable: Optional[Any] = ..., autoincrement: Optional[Any] = ..., existing_autoincrement: Optional[Any] = ..., comment: bool = ..., existing_comment: Optional[Any] = ..., **kw: Any) -> None: ...
    def drop_constraint(self, const: Any) -> None: ...
    def compare_server_default(self, inspector_column: Any, metadata_column: Any, rendered_metadata_default: Any, rendered_inspector_default: Any): ...
    def correct_for_autogen_constraints(self, conn_unique_constraints: Any, conn_indexes: Any, metadata_unique_constraints: Any, metadata_indexes: Any) -> None: ...
    def correct_for_autogen_foreignkeys(self, conn_fks: Any, metadata_fks: Any) -> None: ...

class MySQLAlterDefault(AlterColumn):
    column_name: Any = ...
    default: Any = ...
    def __init__(self, name: Any, column_name: Any, default: Any, schema: Optional[Any] = ...) -> None: ...

class MySQLChangeColumn(AlterColumn):
    column_name: Any = ...
    nullable: Any = ...
    newname: Any = ...
    default: Any = ...
    autoincrement: Any = ...
    comment: Any = ...
    type_: Any = ...
    def __init__(self, name: Any, column_name: Any, schema: Optional[Any] = ..., newname: Optional[Any] = ..., type_: Optional[Any] = ..., nullable: Optional[Any] = ..., default: bool = ..., autoincrement: Optional[Any] = ..., comment: bool = ...) -> None: ...

class MySQLModifyColumn(MySQLChangeColumn): ...
