Running the Model
=================

Importing libraries: The are two implementations of the model description - an implementation which
represent positions as sets of integers and an implementation which represents positions as
bitarrays.


.. code:: python

    # importing libraries
    from remodel.set_implementation import SetBasedPosition, SetBasedDialecticalStructure, SetBasedReflectiveEquilibrium
    from remodel.bitarray_implementation import BitarrayPosition, BitarrayDialecticalStructure, BitarrayReflectiveEquilibrium
    from remodeldescription.basics import Position
    from bitarray import bitarray

Creating Dialectical Structures from Scratch
--------------------------------------------

Dialectical structures can be instantiated by defining a list of arguments.
Each argument is represented by a list of integers - the last integer of the list representing
the conclusion and the other the premises. Negations are indicated by negative numbers.

The following examples are taken from [BBB]_.

.. code:: python

    arguments = [[1, 3],
                 [1, 4],
                 [1, 5],
                 [1, -6],
                 [2, -4],
                 [2, 5],
                 [2, 6],
                 [2, 7]]

Instantiating a dialectical structure further requires to decide the used sentencepool by
fixing the number of unnegated sentences :code:`n`.

As a set-based dialectical structure:

.. code:: python

 setbased_ds = SetBasedDialecticalStructure(n = 7, initial_arguments = arguments)

As a bitarray-based dialectical structure:

.. code:: python

    bitarray_ds = BitarrayDialecticalStructure(n = 7, initial_arguments = arguments)

Running the model
-----------------

Running the model (for finding RE-states or global opitma) requires

* instantiating the reflective equilibrium class,
* defining initial commitments :math:`\mathcal{C}_0` as a :code:`Position` and
* calling respective methods of the RE-instance.

With the set-based implementation:

.. code:: python

    setbased_re = SetBasedReflectiveEquilibrium(setbased_ds)
    setbased_initial_position_A = SetBasedPosition({3, 4, 5})
    setbased_result = setbased_re.re_process(setbased_initial_position_A)

With the bitarray-based implementation:

.. code:: python

    bitarray_re = BitarrayReflectiveEquilibrium(bitarray_ds)
    bitarray_initial_position_A = BitarrayPosition({3, 4, 5}, n)
    bitarray_result = bitarray_re.re_process(bitarray_initial_position_A)

The results of the process can be accessed via the returned
result as :class:`ReflectiveEquilibrium.Results`, e.g.:

.. code:: python

    print('Commitments of RE-state: {}'.format(setbased_result['commitments']))
    print('Theory of RE-state: {}'.format(setbased_result['theory']))



Using Different Weights for the Achievement Function
----------------------------------------------------

The achievement function uses default values for different weighing and
penalty parameters, which can be adjusted. E.g.:

.. code:: python

    setbased_re = SetBasedReflectiveEquilibrium(setbased_ds)
    setbased_re.set_weights(account = 0.2, systematicity = 0.2, faithfulness = 0.6)
    setbased_re.set_account_penalties(d0 = 0, d1 = 1, d2 = 2, d3 = 2)
    setbased_re.set_faithfulness_penalties(d0 = 0, d1 = 1, d2 = 2, d3 = 2)



For further information consult the :ref:`API-docs <api-docs-label>` or have
a look at the various **notebook-examples** (todo: templates).

