"""
This type stub file was generated by pyright.
"""

def decode(string, backend=..., context=..., keys=..., reset=..., safe=..., classes=..., v1_decode=..., on_missing=..., handle_readonly=...): # -> str | list[Any] | dict[Any, Any] | set[Any] | tuple[Any, ...]:
    """Convert a JSON string into a Python object.

    :param backend: If set to an instance of jsonpickle.backend.JSONBackend, jsonpickle
        will use that backend for deserialization.

    :param context: Supply a pre-built Pickler or Unpickler object to the
        `jsonpickle.encode` and `jsonpickle.decode` machinery instead
        of creating a new instance. The `context` represents the currently
        active Pickler and Unpickler objects when custom handlers are
        invoked by jsonpickle.

    :param keys: If set to True then jsonpickle will decode non-string dictionary keys
        into python objects via the jsonpickle protocol.

    :param reset: Custom pickle handlers that use the `Pickler.flatten` method or
        `jsonpickle.encode` function must call `encode` with `reset=False`
        in order to retain object references during pickling.
        This flag is not typically used outside of a custom handler or
        `__getstate__` implementation.

    :param safe: If set to True, eval() is avoided, but backwards-compatible
        (pre-0.7.0) deserialization of repr-serialized objects is disabled.

    :param classes: If set to a single class, or a sequence (list, set, tuple) of
        classes, then the classes will be made available when constructing objects.
        If set to a dictionary of class names to class objects, the class object
        will be provided to jsonpickle to deserialize the class name into.
        This can be used to give jsonpickle access to local classes that are not
        available through the global module import scope, and the dict method can
        be used to deserialize encoded objects into a new class.

    :param v1_decode: If set to True it enables you to decode objects serialized in
        jsonpickle v1. Please do not attempt to re-encode the objects in the v1 format!
        Version 2's format fixes issue #255, and allows dictionary identity to be
        preserved through an encode/decode cycle.

    :param on_missing: If set to 'error', it will raise an error if the class it's
        decoding is not found. If set to 'warn', it will warn you in said case.
        If set to a non-awaitable function, it will call said callback function
        with the class name (a string) as the only parameter. Strings passed to
        `on_missing` are lowercased automatically.

    :param handle_readonly: If set to True, the Unpickler will handle objects encoded
        with 'handle_readonly' properly. Do not set this flag for objects not encoded
        with 'handle_readonly' set to True.


    >>> decode('"my string"') == 'my string'
    True
    >>> decode('36')
    36
    """
    ...

class _Proxy:
    """Proxies are dummy objects that are later replaced by real instances

    The `restore()` function has to solve a tricky problem when pickling
    objects with cyclical references -- the parent instance does not yet
    exist.

    The problem is that `__getnewargs__()`, `__getstate__()`, custom handlers,
    and cyclical objects graphs are allowed to reference the yet-to-be-created
    object via the referencing machinery.

    In other words, objects are allowed to depend on themselves for
    construction!

    We solve this problem by placing dummy Proxy objects into the referencing
    machinery so that we can construct the child objects before constructing
    the parent.  Objects are initially created with Proxy attribute values
    instead of real references.

    We collect all objects that contain references to proxies and run
    a final sweep over them to swap in the real instance.  This is done
    at the very end of the top-level `restore()`.

    The `instance` attribute below is replaced with the real instance
    after `__new__()` has been used to construct the object and is used
    when swapping proxies with real instances.

    """
    def __init__(self) -> None:
        ...
    
    def get(self): # -> None:
        ...
    
    def reset(self, instance): # -> None:
        ...
    


class _IDProxy(_Proxy):
    def __init__(self, objs, index) -> None:
        ...
    
    def get(self):
        ...
    


def loadclass(module_and_name, classes=...): # -> ModuleType | Any | None:
    """Loads the module and returns the class.

    >>> cls = loadclass('datetime.datetime')
    >>> cls.__name__
    'datetime'

    >>> loadclass('does.not.exist')

    >>> loadclass('builtins.int')()
    0

    """
    ...

def has_tag(obj, tag): # -> bool:
    """Helper class that tests to see if the obj is a dictionary
    and contains a particular key/tag.

    >>> obj = {'test': 1}
    >>> has_tag(obj, 'test')
    True
    >>> has_tag(obj, 'fail')
    False

    >>> has_tag(42, 'fail')
    False

    """
    ...

def getargs(obj, classes=...): # -> list[Any]:
    """Return arguments suitable for __new__()"""
    ...

class _trivialclassic:
    """
    A trivial class that can be instantiated with no args
    """
    ...


def make_blank_classic(cls): # -> _trivialclassic:
    """
    Implement the mandated strategy for dealing with classic classes
    which cannot be instantiated without __getinitargs__ because they
    take parameters
    """
    ...

def loadrepr(reprstr): # -> Any:
    """Returns an instance of the object from the object's repr() string.
    It involves the dynamic specification of code.

    >>> obj = loadrepr('datetime/datetime.datetime.now()')
    >>> obj.__class__.__name__
    'datetime'

    """
    ...

def has_tag_dict(obj, tag): # -> bool:
    """Helper class that tests to see if the obj is a dictionary
    and contains a particular key/tag.

    >>> obj = {'test': 1}
    >>> has_tag(obj, 'test')
    True
    >>> has_tag(obj, 'fail')
    False

    >>> has_tag(42, 'fail')
    False

    """
    ...

class Unpickler:
    def __init__(self, backend=..., keys=..., safe=..., v1_decode=..., on_missing=..., handle_readonly=...) -> None:
        ...
    
    def reset(self): # -> None:
        """Resets the object's internal state."""
        ...
    
    def restore(self, obj, reset=..., classes=...): # -> str | list[Any] | dict[Any, Any] | set[Any] | tuple[Any, ...]:
        """Restores a flattened object to its original python state.

        Simply returns any of the basic builtin types

        >>> u = Unpickler()
        >>> u.restore('hello world') == 'hello world'
        True
        >>> u.restore({'key': 'value'}) == {'key': 'value'}
        True

        """
        ...
    
    def register_classes(self, classes): # -> None:
        """Register one or more classes

        :param classes: sequence of classes or a single class to register

        """
        ...
    

