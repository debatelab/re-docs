De-/serialization of RE objects
===============================

The module :mod:`remodel.util` provides some convenient methods that enable JSON de-/serialization of objects
by utilizing the :mod:`json`-python package.

Serializing RE objects
----------------------

You can serialize

* classes that implement :class:`Position`, :class:`DialecticalStructure`, :class:`REState` and :class:`ReflectiveEquilibrium`, or
* any compounds thereof as long as the :mod:`json` python module can handle them (e.g., lists, dictionaries).


For instance, the following code will serialize a position:

.. code:: python

    from rethon.util import re_dumps, re_dump
    from rethon.model import StandardPosition

    # serializing a position as JSON String
    pos_json_str = re_dumps(StandardPosition.from_set({1,2},4),
                            indent=4)
    print(pos_json_str)

    # serializing a list of positions
    pos_list = [StandardPosition.from_set({1,2},4),
                StandardPosition.from_set({1,3},4),
                StandardPosition.from_set(set(),0)]
    print(re_dumps(pos_list, indent=4))

    # serializing a list of position into a file
    output_file_path = 'path-to-file/file-name.json'
    with open(file=output_file_path, mode='w') as output_file:
        re_dump(pos_list, output_file, indent=4)


If important, you can save the implementation details (module name and class name), which can be considered
later to deserialize the objects:

.. code:: python

    from rethon.util import re_dumps
    from rethon.set_implementation import SetBasedPosition

    # serializing a position as JSON String
    pos_json_str = re_dumps(StandardPosition.from_set({1,2},4),
                            indent=4,
                            serialize_implementation=True)
    print(pos_json_str)

Deserializing RE objects
------------------------

The deserialization of RE objects is similarly simple. The implementation details can either be taken from
the json file or can be explicitly given via parameters.

.. code:: python

    from rethon.util import re_dumps, re_loads, re_load
    from rethon.set_implementation import SetBasedPosition
    from rethon.bitarray_implementation import BitarrayPosition

    # serializing a position as JSON String
    pos_json_str = re_dumps(SetBasedPosition.from_set({1,2},4),
                            indent=4,
                            serialize_implementation=True)
    # deserializing it
    position = re_loads(pos_json_str, use_json_specified_type = True )

    # deserializing it and using another implementation
    position = re_loads(pos_json_str,
                        position_module = 'rethon.bitarray_implementation',
                        position_class = 'BitarrayPosition' )



    # deserializing re objects from a file
    input_file_path = 'path-to-file/file-name.json'
    with open(file=input_file_path, mode='r') as input_file:
        obj = re_load(input_file)
