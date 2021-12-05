"""Validates mechanism params"""

class Regulator(object):
    """
    The `DiffPriv.validate.Regulator` object contains a set of rules 
    corresponding to a specific `DiffPriv.mech.Mechanism` object. When any 
    of these rules are violated, it triggers the appropriate error.

    """
    def __init__(self, Mechanism, params, regulators):
        """
        Initializes the `Regulator` object.

        ## Parameters

        - Mechanism:
            An object (or list of objects) of the type 
            `DiffPriv.mech.Mechanism` to regulate

        - params:
            A dictionary of differential privacy parameters.
            Each entry should be formatted as follows:
            ```python
            {
                'param1': regulator1,
                'param2': regulator2,
                'name': regulator_func,
                ...
            }
            ```

        - regulators:
            A list (corresponding to the `params` dictionary) of 
            functions that validate the differential privacy parameters.

        """
        self.Mechanism = Mechanism
        self.params = params  # TODO: Add support for optional parameters

        self.__doc__ = f'''reg#
# Regulator for {self.Mechanism}
---
## Parameters & Metadata:
{self.params}
'''

    def about(self):
        """
        Returns a docstring containing information about the mechanism.

        """
        return self.__doc__

    def __call__(self, params):
        """Validates params"""

        # Check if params is a dictionary
        if not isinstance(params, dict):
            raise TypeError('Parameters must be in dictionary format.')
        
        # Check if params is empty
        if not params:
            raise ValueError('Parameters cannot be empty.')

        # Validate params
        for param in self.params.items():

            # Check if required parameters are present
            if param[0] not in params.keys():
                raise ValueError(f'Parameter {param} is required.')

            # Find parameter
            param_value = None
            for lparam in params.items():
                if param[0] == lparam[0]:
                    param_value = lparam[1]                    

            # Run regulator function
            param[1](param_value)

        return True

    def __repr__(self):
        """Python representation (for debugging purposes)"""
        return f'`DiffPriv.validate.Regulator` object for <{self.Mechanism}>'

    def __eq__(self, other):
        """Equality operator"""
        return self.Mechanism == other.Mechanism and \
               self.params == other.params

    def __ne__(self, other):
        """Inequality operator"""
        return not self == other

    # TODO: Add operators (add, sub, mul, div, etc.)
