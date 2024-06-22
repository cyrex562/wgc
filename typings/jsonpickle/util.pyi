"""
This type stub file was generated by pyright.
"""

"""Helper functions for pickling and unpickling.  Most functions assist in
determining the type of an object.
"""
SEQUENCES = ...
SEQUENCES_SET = ...
PRIMITIVES = ...
FUNCTION_TYPES = ...
NON_REDUCIBLE_TYPES = ...
NON_CLASS_TYPES = ...
def is_type(obj): # -> bool:
    """Returns True is obj is a reference to a type.

    >>> is_type(1)
    False

    >>> is_type(object)
    True

    >>> class Klass: pass
    >>> is_type(Klass)
    True
    """
    ...

def has_method(obj, name): # -> bool:
    ...

def is_object(obj): # -> bool:
    """Returns True is obj is a reference to an object instance.

    >>> is_object(1)
    True

    >>> is_object(object())
    True

    >>> is_object(lambda x: 1)
    False
    """
    ...

def is_not_class(obj): # -> bool:
    """Determines if the object is not a class or a class instance.
    Used for serializing properties.
    """
    ...

def is_primitive(obj): # -> bool:
    """Helper method to see if the object is a basic data type. Unicode strings,
    integers, longs, floats, booleans, and None are considered primitive
    and will return True when passed into *is_primitive()*

    >>> is_primitive(3)
    True
    >>> is_primitive([4,4])
    False
    """
    ...

def is_enum(obj): # -> bool:
    """Is the object an enum?"""
    ...

def is_dictionary(obj): # -> bool:
    """Helper method for testing if the object is a dictionary.

    >>> is_dictionary({'key':'value'})
    True

    """
    ...

def is_sequence(obj): # -> bool:
    """Helper method to see if the object is a sequence (list, set, or tuple).

    >>> is_sequence([4])
    True

    """
    ...

def is_list(obj): # -> bool:
    """Helper method to see if the object is a Python list.

    >>> is_list([4])
    True
    """
    ...

def is_set(obj): # -> bool:
    """Helper method to see if the object is a Python set.

    >>> is_set(set())
    True
    """
    ...

def is_bytes(obj): # -> bool:
    """Helper method to see if the object is a bytestring.

    >>> is_bytes(b'foo')
    True
    """
    ...

def is_unicode(obj): # -> bool:
    """Helper method to see if the object is a unicode string"""
    ...

def is_tuple(obj): # -> bool:
    """Helper method to see if the object is a Python tuple.

    >>> is_tuple((1,))
    True
    """
    ...

def is_dictionary_subclass(obj): # -> bool:
    """Returns True if *obj* is a subclass of the dict type. *obj* must be
    a subclass and not the actual builtin dict.

    >>> class Temp(dict): pass
    >>> is_dictionary_subclass(Temp())
    True
    """
    ...

def is_sequence_subclass(obj): # -> bool:
    """Returns True if *obj* is a subclass of list, set or tuple.

    *obj* must be a subclass and not the actual builtin, such
    as list, set, tuple, etc..

    >>> class Temp(list): pass
    >>> is_sequence_subclass(Temp())
    True
    """
    ...

def is_noncomplex(obj): # -> bool:
    """Returns True if *obj* is a special (weird) class, that is more complex
    than primitive data types, but is not a full object. Including:

        * :class:`~time.struct_time`
    """
    ...

def is_function(obj): # -> bool:
    """Returns true if passed a function

    >>> is_function(lambda x: 1)
    True

    >>> is_function(locals)
    True

    >>> def method(): pass
    >>> is_function(method)
    True

    >>> is_function(1)
    False
    """
    ...

def is_module_function(obj): # -> bool:
    """Return True if `obj` is a module-global function

    >>> import os
    >>> is_module_function(os.path.exists)
    True

    >>> is_module_function(lambda: None)
    False

    """
    ...

def is_module(obj): # -> bool:
    """Returns True if passed a module

    >>> import os
    >>> is_module(os)
    True

    """
    ...

def is_picklable(name, value): # -> bool:
    """Return True if an object can be pickled

    >>> import os
    >>> is_picklable('os', os)
    True

    >>> def foo(): pass
    >>> is_picklable('foo', foo)
    True

    >>> is_picklable('foo', lambda: None)
    False

    """
    ...

def is_installed(module): # -> bool:
    """Tests to see if ``module`` is available on the sys.path

    >>> is_installed('sys')
    True
    >>> is_installed('hopefullythisisnotarealmodule')
    False

    """
    ...

def is_list_like(obj): # -> bool:
    ...

def is_iterator(obj): # -> bool:
    ...

def is_collections(obj): # -> bool:
    ...

def is_reducible_sequence_subclass(obj): # -> bool:
    ...

def is_reducible(obj): # -> bool:
    """
    Returns false if of a type which have special casing,
    and should not have their __reduce__ methods used
    """
    ...

def is_cython_function(obj): # -> bool:
    """Returns true if the object is a reference to a Cython function"""
    ...

def is_readonly(obj, attr, value): # -> bool:
    ...

def in_dict(obj, key, default=...): # -> bool:
    """
    Returns true if key exists in obj.__dict__; false if not in.
    If obj.__dict__ is absent, return default
    """
    ...

def in_slots(obj, key, default=...): # -> bool:
    """
    Returns true if key exists in obj.__slots__; false if not in.
    If obj.__slots__ is absent, return default
    """
    ...

def has_reduce(obj): # -> tuple[Literal[False], Literal[False]] | tuple[Literal[False], Literal[True]] | tuple[Literal[True], Literal[True]] | tuple[Any | bool, Any | bool]:
    """
    Tests if __reduce__ or __reduce_ex__ exists in the object dict or
    in the class dicts of every class in the MRO *except object*.

    Returns a tuple of booleans (has_reduce, has_reduce_ex)
    """
    ...

def translate_module_name(module): # -> str:
    """Rename builtin modules to a consistent module name.

    Prefer the more modern naming.

    This is used so that references to Python's `builtins` module can
    be loaded in both Python 2 and 3.  We remap to the "__builtin__"
    name and unmap it when importing.

    Map the Python2 `exceptions` module to `builtins` because
    `builtins` is a superset and contains everything that is
    available in `exceptions`, which makes the translation simpler.

    See untranslate_module_name() for the reverse operation.
    """
    ...

def untranslate_module_name(module): # -> str:
    """Rename module names mention in JSON to names that we can import

    This reverses the translation applied by translate_module_name() to
    a module name available to the current version of Python.

    """
    ...

def importable_name(cls): # -> str:
    """
    >>> class Example(object):
    ...     pass

    >>> ex = Example()
    >>> importable_name(ex.__class__) == 'jsonpickle.util.Example'
    True
    >>> importable_name(type(25)) == 'builtins.int'
    True
    >>> importable_name(None.__class__) == 'builtins.NoneType'
    True
    >>> importable_name(False.__class__) == 'builtins.bool'
    True
    >>> importable_name(AttributeError) == 'builtins.AttributeError'
    True

    """
    ...

def b64encode(data): # -> str:
    """
    Encode binary data to ascii text in base64. Data must be bytes.
    """
    ...

def b64decode(payload): # -> bytes:
    """
    Decode payload - must be ascii text.
    """
    ...

def b85encode(data): # -> str:
    """
    Encode binary data to ascii text in base85. Data must be bytes.
    """
    ...

def b85decode(payload): # -> bytes:
    """
    Decode payload - must be ascii text.
    """
    ...

def itemgetter(obj, getter=...): # -> str:
    ...

def items(obj): # -> Generator[tuple[Any, Any], Any, None]:
    """
    TODO: Replace all calls to this with plain dict.items()
    """
    ...
