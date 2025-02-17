"""
run
===
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "result" category
"""

class run(Operator):
    """Solve in mapdl a dat/inp file and returns a datasources with the rst file.

      available inputs:
        - mapdl_exe_path (str) (optional)
        - working_dir (str) (optional)
        - number_of_processes (int) (optional)
        - data_sources (DataSources)

      available outputs:
        - data_sources (DataSources)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.run()

      >>> # Make input connections
      >>> my_mapdl_exe_path = str()
      >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
      >>> my_working_dir = str()
      >>> op.inputs.working_dir.connect(my_working_dir)
      >>> my_number_of_processes = int()
      >>> op.inputs.number_of_processes.connect(my_number_of_processes)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.run(mapdl_exe_path=my_mapdl_exe_path,working_dir=my_working_dir,number_of_processes=my_number_of_processes,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_data_sources = op.outputs.data_sources()"""
    def __init__(self, mapdl_exe_path=None, working_dir=None, number_of_processes=None, data_sources=None, config=None, server=None):
        super().__init__(name="mapdl::run", config = config, server = server)
        self._inputs = InputsRun(self)
        self._outputs = OutputsRun(self)
        if mapdl_exe_path !=None:
            self.inputs.mapdl_exe_path.connect(mapdl_exe_path)
        if working_dir !=None:
            self.inputs.working_dir.connect(working_dir)
        if number_of_processes !=None:
            self.inputs.number_of_processes.connect(number_of_processes)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Solve in mapdl a dat/inp file and returns a datasources with the rst file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mapdl_exe_path", type_names=["string"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "working_dir", type_names=["string"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "number_of_processes", type_names=["int32"], optional=True, document="""Set the number of MPI processes used for resolution (default is 2)"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the input file.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::run")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRun 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRun 
        """
        return super().outputs


#internal name: mapdl::run
#scripting name: run
class InputsRun(_Inputs):
    """Intermediate class used to connect user inputs to run operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.run()
      >>> my_mapdl_exe_path = str()
      >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
      >>> my_working_dir = str()
      >>> op.inputs.working_dir.connect(my_working_dir)
      >>> my_number_of_processes = int()
      >>> op.inputs.number_of_processes.connect(my_number_of_processes)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
    """
    def __init__(self, op: Operator):
        super().__init__(run._spec().inputs, op)
        self._mapdl_exe_path = Input(run._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mapdl_exe_path)
        self._working_dir = Input(run._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._working_dir)
        self._number_of_processes = Input(run._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._number_of_processes)
        self._data_sources = Input(run._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)

    @property
    def mapdl_exe_path(self):
        """Allows to connect mapdl_exe_path input to the operator

        Parameters
        ----------
        my_mapdl_exe_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.run()
        >>> op.inputs.mapdl_exe_path.connect(my_mapdl_exe_path)
        >>> #or
        >>> op.inputs.mapdl_exe_path(my_mapdl_exe_path)

        """
        return self._mapdl_exe_path

    @property
    def working_dir(self):
        """Allows to connect working_dir input to the operator

        Parameters
        ----------
        my_working_dir : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.run()
        >>> op.inputs.working_dir.connect(my_working_dir)
        >>> #or
        >>> op.inputs.working_dir(my_working_dir)

        """
        return self._working_dir

    @property
    def number_of_processes(self):
        """Allows to connect number_of_processes input to the operator

        - pindoc: Set the number of MPI processes used for resolution (default is 2)

        Parameters
        ----------
        my_number_of_processes : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.run()
        >>> op.inputs.number_of_processes.connect(my_number_of_processes)
        >>> #or
        >>> op.inputs.number_of_processes(my_number_of_processes)

        """
        return self._number_of_processes

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: data sources containing the input file.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.run()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

class OutputsRun(_Outputs):
    """Intermediate class used to get outputs from run operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.run()
      >>> # Connect inputs : op.inputs. ...
      >>> result_data_sources = op.outputs.data_sources()
    """
    def __init__(self, op: Operator):
        super().__init__(run._spec().outputs, op)
        self._data_sources = Output(run._spec().output_pin(0), 0, op) 
        self._outputs.append(self._data_sources)

    @property
    def data_sources(self):
        """Allows to get data_sources output of the operator


        Returns
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.run()
        >>> # Connect inputs : op.inputs. ...
        >>> result_data_sources = op.outputs.data_sources() 
        """
        return self._data_sources

