"""
.. _ref_use_result_helpers:

Use Result Helpers to Load Custom Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The `Result` class which instances are created by the `Model` gives access to 
helpers to request results on specific mesh and time scopings.
With those helpers, working on a custom spatial and temporal subset of the 
model is straightforward.
"""
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# First, create a model object to establish a connection with an
# example result file
model = dpf.Model(examples.download_multi_stage_cyclic_result())
print(model)


###############################################################################
# Visualize specific mode shapes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Choose the modes to visualize
modes = [1,5,6]


disp = model.results.displacement.on_time_scoping(modes)

###############################################################################
# Choose a spatial subset
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Work only a named selection (or component)

###############################################################################
# Print the available named selection
print(model.metadata.available_named_selections)


###############################################################################
# Specify to the result that we work on a specific named selection
disp.on_named_selection('_STAG1_BASE_NOD')
op = disp()
op.inputs.read_cyclic(2)#expand cyclic 
results = op.outputs.fields_container()

#plot
for mode in modes:
    results[0].meshed_region.plot(results.get_fields_by_time_complex_ids(mode, 0)[0])
    
    


###############################################################################
# Specify to the result that we work on specific nodes
disp = model.results.displacement.on_time_scoping(modes)
disp.on_mesh_scoping(list(range(1, 200)))
op = disp()
op.inputs.read_cyclic(2)#expand cyclic 
results = op.outputs.fields_container()

#plot
for mode in modes:
    results[0].meshed_region.plot(results.get_fields_by_time_complex_ids(mode, 0)[0])
    
    