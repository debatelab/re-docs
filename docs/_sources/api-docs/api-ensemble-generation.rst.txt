.. _ensemble-generation-label:

Ensemble generation
===================

Ensemble Generation with the module :code:`rethon.ensemble_generation`

This module contains classes and methods that can be used to generate ensembles of reflective equilibrium
processes and save data of these ensemble in csv files. The behaviour of ensemble generation can be adapted by
implementing and subclassing the exisinting classes in this module, which have the following class hierarchy:

* :py:class:`AbstractEnsembleGenerator`: Base class for ensemble generation.
   * :py:class:`EnsembleGenerator`: Base class that can be used to generate independent model runs (with the possibiltiy to generate branches).
      * :py:class:`SimpleEnsembleGenerator`: Adds standard data items.
         * :py:class:`GlobalREEnsembleGenerator`: Adds data items for globally searching RE (:py:class:`GlobalReflectiveEquilibrium`).
         * :py:class:`LocalREEnsembleGenerator`: Adds items for locally searching RE (:py:class:`LocalReflectiveEquilibrium`).
   * :py:class:`MultiAgentEnsemblesGenerator`: Base class that can be used to generate multi-agent model runs.
      * :py:class:`SimpleMultiAgentEnsemblesGenerator`: Adds standard data item.


Methods in :code:`rethon.ensemble_generation`
---------------------------------------------

.. automodule:: rethon.ensemble_generation
   :members: create_random_argument_list, random_dialectical_structures, varied_alphas, standard_model_params_varied_alphas,
            local_re_model_params_varied_alphas, random_positions


:class:`AbstractEnsembleGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.AbstractEnsembleGenerator
   :members:
   :show-inheritance:


:class:`EnsembleGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.EnsembleGenerator
   :members:
   :show-inheritance:

:class:`SimpleEnsembleGenerator`
--------------------------------

.. autoclass:: rethon.ensemble_generation.SimpleEnsembleGenerator
   :members:
   :show-inheritance:

:class:`GlobalREEnsembleGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.GlobalREEnsembleGenerator
   :members:
   :show-inheritance:

:class:`LocalREEnsembleGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.LocalREEnsembleGenerator
   :members:
   :show-inheritance:

:class:`MultiAgentEnsemblesGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.MultiAgentEnsemblesGenerator
   :members:
   :show-inheritance:

:class:`SimpleMultiAgentEnsemblesGenerator`
--------------------------

.. autoclass:: rethon.ensemble_generation.SimpleMultiAgentEnsemblesGenerator
   :members:
   :show-inheritance:

