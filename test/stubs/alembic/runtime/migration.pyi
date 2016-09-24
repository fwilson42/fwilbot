# Stubs for alembic.runtime.migration (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
#from sqlalchemy.engine import url as sqla_url
#from ..util.compat import callable as callable, EncodedIO as EncodedIO

log = ...  # type: Any

class MigrationContext:
    environment_context = ...  # type: Any
    opts = ...  # type: Any
    dialect = ...  # type: Any
    script = ...  # type: Any
    connection = ...  # type: Any
    as_sql = ...  # type: Any
    output_buffer = ...  # type: Any
    version_table = ...  # type: Any
    version_table_schema = ...  # type: Any
    impl = ...  # type: Any
    def __init__(self, dialect, connection, opts, environment_context=None): ...
    @classmethod
    def configure(cls, connection=None, url=None, dialect_name=None, dialect=None, environment_context=None, opts=None): ...
    def begin_transaction(self, _per_migration=False): ...
    def get_current_revision(self): ...
    def get_current_heads(self): ...
    def stamp(self, script_directory, revision): ...
    def run_migrations(self, **kw): ...
    def execute(self, sql, execution_options=None): ...
    @property
    def bind(self): ...
    @property
    def config(self): ...

class HeadMaintainer:
    context = ...  # type: Any
    heads = ...  # type: Any
    def __init__(self, context, heads): ...
    def update_to_step(self, step): ...

class MigrationStep:
    @property
    def name(self): ...
    @classmethod
    def upgrade_from_script(cls, revision_map, script): ...
    @classmethod
    def downgrade_from_script(cls, revision_map, script): ...
    @property
    def is_downgrade(self): ...
    @property
    def short_log(self): ...

class RevisionStep(MigrationStep):
    revision_map = ...  # type: Any
    revision = ...  # type: Any
    is_upgrade = ...  # type: Any
    migration_fn = ...  # type: Any
    def __init__(self, revision_map, revision, is_upgrade): ...
    def __eq__(self, other): ...
    @property
    def doc(self): ...
    @property
    def from_revisions(self): ...
    @property
    def from_revisions_no_deps(self): ...
    @property
    def to_revisions(self): ...
    @property
    def to_revisions_no_deps(self): ...
    def should_delete_branch(self, heads): ...
    def merge_branch_idents(self, heads): ...
    def unmerge_branch_idents(self, heads): ...
    def should_create_branch(self, heads): ...
    def should_merge_branches(self, heads): ...
    def should_unmerge_branches(self, heads): ...
    def update_version_num(self, heads): ...
    @property
    def delete_version_num(self): ...
    @property
    def insert_version_num(self): ...

class StampStep(MigrationStep):
    from_ = ...  # type: Any
    to_ = ...  # type: Any
    is_upgrade = ...  # type: Any
    branch_move = ...  # type: Any
    migration_fn = ...  # type: Any
    def __init__(self, from_, to_, is_upgrade, branch_move): ...
    doc = ...  # type: Any
    def stamp_revision(self, **kw): ...
    def __eq__(self, other): ...
    @property
    def from_revisions(self): ...
    @property
    def to_revisions(self): ...
    @property
    def from_revisions_no_deps(self): ...
    @property
    def to_revisions_no_deps(self): ...
    @property
    def delete_version_num(self): ...
    @property
    def insert_version_num(self): ...
    def update_version_num(self, heads): ...
    def merge_branch_idents(self, heads): ...
    def unmerge_branch_idents(self, heads): ...
    def should_delete_branch(self, heads): ...
    def should_create_branch(self, heads): ...
    def should_merge_branches(self, heads): ...
    def should_unmerge_branches(self, heads): ...
