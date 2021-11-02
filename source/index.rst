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

  * :code:`git clone git@git.scc.kit.edu:debatelab/re-python.git`

  * :code:`git clone git@git.scc.kit.edu:debatelab/re-model-description.git`

* and then installing the packages by running :code:`pip install -e .` from the local directories of
  the packages (e.g. :code:`local-path-to-repository/remodel`). Pip will install the packges by using the
  :code:`setup.py` file. (The :code:`-e`-option will install the packages in the editable mode, allowing you to
  change the source code.)

.. note:: Both packages require a python version >= 3.8. The package *remodel* further depends on the
    packages `bitarray <https://pypi.org/project/bitarray/>`_ and `PySat <https://github.com/pysathq/pysat>`_
    (which will be installed when installing *remodel* by using pip).


User Guide
----------

This part of the documentation provides step-by-step instructions for running and adapting the model.

.. toctree::
    :maxdepth: 1

    user/running_model
    user/extending_model

For further information consult the :ref:`API-docs <api-docs-label>` or have a look at
the various **notebook-examples** (todo templates).



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



