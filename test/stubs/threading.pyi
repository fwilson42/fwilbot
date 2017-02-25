# Stubs for threading (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, List
from traceback import format_exc as _format_exc
from itertools import islice as _islice, count as _count
from collections import deque as _deque

ThreadError = ...  # type: Any

def setprofile(func): ...
def settrace(func): ...

Lock = ...  # type: Any


class _RLock:
    def __init__(self) -> None: ...
    def acquire(self, blocking=True, timeout=-1): ...
    __enter__ = ...  # type: Any
    def release(self): ...
    def __exit__(self, t, v, tb): ...

def RLock(*args, **kwargs) -> _RLock: ...

class Condition:
    acquire = ...  # type: Any
    release = ...  # type: Any
    def __init__(self, lock=None): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def wait(self, timeout=None): ...
    def wait_for(self, predicate, timeout=None): ...
    def notify(self, n=1): ...
    def notify_all(self): ...
    notifyAll = ...  # type: Any

class Semaphore:
    def __init__(self, value=1): ...
    def acquire(self, blocking=True, timeout=None): ...
    __enter__ = ...  # type: Any
    def release(self): ...
    def __exit__(self, t, v, tb): ...

class BoundedSemaphore(Semaphore):
    def __init__(self, value=1): ...
    def release(self): ...

class Event:
    def __init__(self) -> None: ...
    def is_set(self): ...
    isSet = ...  # type: Any
    def set(self): ...
    def clear(self): ...
    def wait(self, timeout=None): ...

class Barrier:
    def __init__(self, parties, action=None, timeout=None): ...
    def wait(self, timeout=None): ...
    def reset(self): ...
    def abort(self): ...
    @property
    def parties(self): ...
    @property
    def n_waiting(self): ...
    @property
    def broken(self): ...

class BrokenBarrierError(RuntimeError): ...

class Thread:
    def __init__(self, group=None, target=None, name=None, args=..., kwargs=None, *, daemon=None): ...
    def start(self) -> None: ...
    def run(self): ...
    def join(self, timeout=None): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name): ...
    @property
    def ident(self): ...
    def is_alive(self): ...
    isAlive = ...  # type: Any
    @property
    def daemon(self): ...
    @daemon.setter
    def daemon(self, daemonic): ...
    def isDaemon(self): ...
    def setDaemon(self, daemonic): ...
    def getName(self): ...
    def setName(self, name): ...

class Timer(Thread):
    interval = ...  # type: Any
    function = ...  # type: Any
    args = ...  # type: Any
    kwargs = ...  # type: Any
    finished = ...  # type: Any
    def __init__(self, interval: int, function: Callable, args: List[Any] = None, kwargs: Dict[str,Any] = None) -> None: ...
    def cancel(self): ...
    def run(self): ...

class _MainThread(Thread):
    def __init__(self): ...

class _DummyThread(Thread):
    def __init__(self): ...
    def join(self, timeout=None): ...

def current_thread() -> Thread: ...
def active_count(): ...
def enumerate(): ...
