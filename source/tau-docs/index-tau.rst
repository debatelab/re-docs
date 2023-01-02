.. _tau-docs-label:


tau
====


A Python package for dialectical structures.

The `tau` package provides different classes and methods to apply the theory of
dialectical structures (as introduced in [Betz2010]_ and [Betz2013]_).

Installation
------------

Using :code:`pip`
^^^^^^^^^^^^^^^^^

... to come ...

From the source code
^^^^^^^^^^^^^^^^^^^^

You can install the package locally, by

* first git-cloning the repository:

  * :code:`git clone git@github.com:debatelab/tau.git`

* and then installing the package by running ':code:`pip install -e .`' from the local directory of
  the package (e.g. :code:`local-path-to-repository/tau`) that contains the setup file :code:`setup.py`.
  (The :code:`-e`-option will install the package in the editable mode, allowing you to
  change the source code.)

.. note:: The package requires a python version >= 3.8 and depends on the
    packages `bitarray <https://pypi.org/project/bitarray/>`_, `numba <https://numba.pydata.org/>`_ and `PySat <https://github.com/pysathq/pysat>`_
    (which will be installed when installing *remodel* by using pip).


Documentation
-------------

A Jupyter notebook provides step-by-step instructions of using
the :code:`tau` package. Further details can be found in the :ref:`API documentation <tau-api-docs-label>`.

.. toctree::
    :hidden:

    Tutorials <tutorials/tau-tutorials>
    API documentation<api-docs/api>

Licence
-------

**ToDo**

References
----------

.. [Betz2010] Betz, G. 2010, |betz_2010|, Frankfurt a.M.: Klostermann.

.. [Betz2013] Betz, G. 2013, |betz_2013|, Synthese Library, Dordrecht: Springer 2013.


.. |betz_2010| raw:: html

   <a href="https://doi.org/10.5771/9783465136293" target="_blank">Theorie dialektischer Strukturen</a>

.. |betz_2013| raw:: html

   <a href="https://www.springer.com/de/book/9789400745988" target="_blank">Debate Dynamics: How Controversy Improves Our Beliefs</a>