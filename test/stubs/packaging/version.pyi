# Stubs for packaging.version (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from collections import namedtuple

_Version = namedtuple('_Version', ['epoch', 'release', 'dev', 'pre', 'post', 'local'])

def parse(version): ...

class InvalidVersion(ValueError): ...

class _BaseVersion:
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __ne__(self, other): ...

class LegacyVersion(_BaseVersion):
    def __init__(self, version): ...
    @property
    def public(self): ...
    @property
    def base_version(self): ...
    @property
    def local(self): ...
    @property
    def is_prerelease(self): ...
    @property
    def is_postrelease(self): ...

VERSION_PATTERN = ...  # type: Any

class Version(_BaseVersion):
    def __init__(self, version): ...
    @property
    def public(self): ...
    @property
    def base_version(self): ...
    @property
    def local(self): ...
    @property
    def is_prerelease(self): ...
    @property
    def is_postrelease(self): ...
