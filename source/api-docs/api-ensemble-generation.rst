.. _ensemble-generation-label:

Ensemble generation
===================

Ensemble Generation with the module :code:`rethon.ensemble_generation`

The methods in this module can be used to generate an ensemble of randomly generated runs of reflective equilibrium
processes. The generated data will be saved in a csv-file, with the following columns (all complex data-types are stored
as strings and have to be parsed if needed):


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

Methods in :code:`rethon.ensemble_generation`
---------------------------------------------

.. automodule:: rethon.ensemble_generation
   :members: create_random_argument_list, random_dialectical_structures, varied_alphas, standard_model_params_varied_alphas,
            local_re_model_params_varied_alphas, random_positions