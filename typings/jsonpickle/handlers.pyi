"""
This type stub file was generated by pyright.
"""

import sys

"""
Custom handlers may be created to handle other objects. Each custom handler
must derive from :class:`jsonpickle.handlers.BaseHandler` and
implement ``flatten`` and ``restore``.

A handler can be bound to other types by calling
:func:`jsonpickle.handlers.register`.

"""
class Registry:
    def __init__(self) -> None:
        ...
    
    def get(self, cls_or_name, default=...): # -> None:
        """
        :param cls_or_name: the type or its fully qualified name
        :param default: default value, if a matching handler is not found

        Looks up a handler by type reference or its fully
        qualified name. If a direct match
        is not found, the search is performed over all
        handlers registered with base=True.
        """
        ...
    
    def register(self, cls, handler=..., base=...): # -> Callable[..., Any] | None:
        """Register the a custom handler for a class

        :param cls: The custom object class to handle
        :param handler: The custom handler class (if
            None, a decorator wrapper is returned)
        :param base: Indicates whether the handler should
            be registered for all subclasses

        This function can be also used as a decorator
        by omitting the `handler` argument::

            @jsonpickle.handlers.register(Foo, base=True)
            class FooHandler(jsonpickle.handlers.BaseHandler):
                pass

        """
        ...
    
    def unregister(self, cls): # -> None:
        ...
    


registry = ...
register = ...
unregister = ...
get = ...
class BaseHandler:
    def __init__(self, context) -> None:
        """
        Initialize a new handler to handle a registered type.

        :Parameters:
          - `context`: reference to pickler/unpickler

        """
        ...
    
    def flatten(self, obj, data):
        """
        Flatten `obj` into a json-friendly form and write result to `data`.

        :param object obj: The object to be serialized.
        :param dict data: A partially filled dictionary which will contain the
            json-friendly representation of `obj` once this method has
            finished.
        """
        ...
    
    def restore(self, obj):
        """
        Restore an object of the registered type from the json-friendly
        representation `obj` and return it.
        """
        ...
    
    @classmethod
    def handles(self, cls):
        """
        Register this handler for the given class. Suitable as a decorator,
        e.g.::

            @MyCustomHandler.handles
            class MyCustomClass:
                def __reduce__(self):
                    ...
        """
        ...
    
    def __call__(self, context): # -> Self:
        """This permits registering either Handler instances or classes

        :Parameters:
          - `context`: reference to pickler/unpickler
        """
        ...
    


class ArrayHandler(BaseHandler):
    """Flatten and restore array.array objects"""
    def flatten(self, obj, data):
        ...
    
    def restore(self, data): # -> array[Any]:
        ...
    


class DatetimeHandler(BaseHandler):
    """Custom handler for datetime objects

    Datetime objects use __reduce__, and they generate binary strings encoding
    the payload. This handler encodes that payload to reconstruct the
    object.

    """
    def flatten(self, obj, data): # -> str:
        ...
    
    def restore(self, data):
        ...
    


class RegexHandler(BaseHandler):
    """Flatten _sre.SRE_Pattern (compiled regex) objects"""
    def flatten(self, obj, data):
        ...
    
    def restore(self, data): # -> Pattern[Any]:
        ...
    


class QueueHandler(BaseHandler):
    """Opaquely serializes Queue objects

    Queues contains mutex and condition variables which cannot be serialized.
    Construct a new Queue instance when restoring.

    """
    def flatten(self, obj, data):
        ...
    
    def restore(self, data): # -> Queue[Any]:
        ...
    


class CloneFactory:
    """Serialization proxy for collections.defaultdict's default_factory"""
    def __init__(self, exemplar) -> None:
        ...
    
    def __call__(self, clone=...):
        """Create new instances by making copies of the provided exemplar"""
        ...
    
    def __repr__(self): # -> str:
        ...
    


class UUIDHandler(BaseHandler):
    """Serialize uuid.UUID objects"""
    def flatten(self, obj, data):
        ...
    
    def restore(self, data): # -> UUID:
        ...
    


class LockHandler(BaseHandler):
    """Serialize threading.Lock objects"""
    def flatten(self, obj, data):
        ...
    
    def restore(self, data): # -> Lock:
        ...
    


_lock = ...
class TextIOHandler(BaseHandler):
    """Serialize file descriptors as None because we cannot roundtrip"""
    def flatten(self, obj, data): # -> None:
        ...
    
    def restore(self, data):
        """Restore should never get called because flatten() returns None"""
        ...
    


if sys.version_info >= (3, 8):
    ...