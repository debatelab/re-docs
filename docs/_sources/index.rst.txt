A Formal Model of Reflective Equilibrium
========================================

A Python implementation of a reflective equilibrium model based on [BBB]_, [Betz2010]_ and [Betz2012]_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
------------

The RE Model consists of two python packages -- *remodeldescription* and *remodel*.
If you want to use and/or extend the model implementation
you have to install both packages locally, by

* first git-cloning the repositories of both packages:

  * :code:`git clone git@github.com:debatelab/re-python.git`

  * :code:`git clone git@github.com:debatelab/re-model-description.git`

* and then installing the packages by running :code:`pip install -e .` from the local directories of
  the packages (e.g. :code:`local-path-to-repository/remodel`). Pip will install the packges by using the
  :code:`setup.py` file. (The :code:`-e`-option will install the packages in the editable mode, allowing you to
  change the source code.)

.. note:: Both packages require a python version >= 3.8. The package *remodel* further depends on the
    packages `bitarray <https://pypi.org/project/bitarray/>`_, `numba <https://numba.pydata.org/>`_ and `PySat <https://github.com/pysathq/pysat>`_
    (which will be installed when installing *remodel* by using pip).


Tutorials
---------

The are different `Jupyter notebooks <https://jupyter.org/>`_ that provide step-by-step instructions of running and adapting the model:

* `intro-repython.ipynb <https://github.com/debatelab/re-docs/blob/master/notebooks/intro-repython.ipynb>`_: Introduction of using
  re-python. Covering the following topics:
    + Running the model
    + Export to JSON
    + Extending the model
* `ensemble-generation-tutorial.ipynb <https://github.com/debatelab/re-docs/blob/master/notebooks/ensemble-generation-tutorial.ipynb>`_: A
  notebook that illustrates how to generate model ensembles with the :ref:`ensemble generation module <ensemble-generation-label>`.


API Documentation
-----------------

The RE Model consists of two python packages. One package (*remodeldescription*) describes the
methods as abstract classes and the other package (*remodel*) provides different implementations
of the model description.


.. toctree::
    :maxdepth: 3

    api-docs/api

Licence
-------

**ToDo**

References
----------

.. [BBB] Claus Beisbart, Gregor Betz and Georg Brun. 202x. **A Formal \
   Model of Reflective Equilibrium**. x, x:x-x.
.. [Betz2010] Betz, G. 2010, Theorie dialektischer Strukturen, Frankfurt a.M.: Klostermann.
.. [Betz2012] Betz, G. 2012, Debate Dynamics: How Controversy Improves Our Beliefs, Synthese Library, Dordrecht: Springer 2012.



