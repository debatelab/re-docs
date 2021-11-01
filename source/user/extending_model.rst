Extending the Model
===================

The easiest way to extend or change the model is to override existing methods
of the implemented classes by writing own classes that inherit the given classes.

The given implementations use a quadratic term for calculating account, systematicity and
faithfulness. Suppose you want to get rid of the quadratic form of e.g. account:

.. math::
    A(\mathcal{C}, \mathcal{T}):=\left( 1-\left(\frac{D_{0,0.3,1,1}(\mathcal{C}, \overline{\mathcal{T}})}{N}\right)^2 \right)

and use instead:

.. math::
    A(\mathcal{C}, \mathcal{T}):=\left( 1-\frac{D_{0,0.3,1,1}(\mathcal{C}, \overline{\mathcal{T}})}{N} \right)

This can simply done by overriding the account-function of the
:class:`SetBasedReflectiveEquilibrium` in the following way:

.. code:: python

    class NewSetBasedReflectiveEquilibrium(SetBasedReflectiveEquilibrium):
        def account(self, commitments: Position, theory: Position) -> float:
            return 1 - (self.hamming_distance(commitments, self.dialectical_structure.closure(theory), [0, 0.3, 1, 1]) /
                    self.dialectical_structure.n)


Now you can use the newly defined class to calculate the account of positions w.r.t. initial
positions or to find RE-states with this new class:

.. code:: python

    # instantiating new class
    new_setbased_re = NewSetBasedReflectiveEquilibrium(setbased_ds)
    print("New account value: ", new_setbased_re.account(SetBasedPosition({3,6}), SetBasedPosition({1})))
    setbased_result = new_setbased_re.re_process(SetBasedPosition({3,6}))
    print('Commitements of RE-state: {}'.format(setbased_result['commitments']))
    print('Theory of RE-state: {}'.format(setbased_result['theory']))



