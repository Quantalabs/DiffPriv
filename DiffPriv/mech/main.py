"""
The main module in the `mech` subpackage.
> All functions and classes in this module are automatically exported to 
> the main scope (i.e. they can be called directly from the `DiffPriv` 
> module).
"""

import math


class Mechanism(object):
    """The base class for all mechanisms"""

    def __init__(self, 
                 name, 
                 description,
                 mapping,
                 abbr=None,
                 epsilon=None,
                 delta=None,):
        """
        Initializes the `Mechanism` superclass.

        ## Parameters

        - name: 
            The name of the differential privacy mechanism

        - description: 
            A short (~1 sentence) description of the mechanism

        - mapping: 
            A function that takes in data, along with other (optional)
            parameters, and returns a privacy-preserving transformation
            of the data.
            > **NOTE:** The first parameter of the mapping function should be
            the one that takes in data.

        - abbr:
            A short abbreviation for the mechanism (used in docstring)

        - epsilon (`=None`): 
            A function that takes in the same parameters as the mapping
            function and returns the privacy budget (ε) of the 
            mechanism. If delta is not provided, the mechanism should 
            be (ε, 0)-differentially private for the given data and 
            parameters.

        - delta (`=None`): 
            A function that takes in the same parameters as the mapping
            function and returns a privacy budget (δ) of the mechanism. 
            If provided, the mechanism should be 
            (ε, δ)-differentially private for the given data and 
            parameters.

            > **NOTE:** This value will be ignored if epsilon is not also 
            > provided.

        """
        self.name = name
        self.description = description
        self.mapping = mapping
        self.epsilon = epsilon
        
        if epsilon is not None:
            self.delta = delta
        else:
            self.delta = None
        
        if abbr is None:
            self.abbr = name
        else:
            self.abbr = abbr

        self.__doc__ = f'''{self.abbr}
# {self.name}
---
## About: 
{self.description}
'''

        self.last_args = None

    def about(self):
        """
        Returns a docstring containing information about the mechanism.

        """
        return self.__doc__

    def __call__(self, data, *args, **kwargs):
        """
        Applies the mechanism to the given data.

        ## Parameters

        - data: 
            The data to be transformed by the mechanism.

        - *args: 
            Additional arguments to be passed to the mapping function.

        - **kwargs: 
            Additional keyword arguments to be passed to the mapping 
            function.

        """
        self.last_args = (data, args, kwargs)
        return self.mapping(data, *args, **kwargs)

    def index(self, data=None, *args, **kwargs):
        """
        Returns the differential privacy index of the mechanism.
        If no parameters are provided, the index is calculated using the
        last arguments provided to the mechanism.

        ## Parameters

        - data: 
            The data to be transformed by the mechanism.

        - *args: 
            Additional arguments to be passed to the mapping function.

        - **kwargs: 
            Additional keyword arguments to be passed to the mapping 
            function.

        """
        if data:
            return self.epsilon(data, *args, **kwargs), \
                   self.delta(data, *args, **kwargs)
        return self.epsilon(self.last_args[0], 
                            *self.last_args[1], 
                            **self.last_args[2]), \
               self.delta(self.last_args[0], 
                          *self.last_args[1], 
                          **self.last_args[2])

    def __repr__(self):
        """Python representation (for debugging purposes)"""
        return f'`DiffPriv.mech.Mechanism` object @ <{self.name}>'

    def __str__(self):
        """String representation (name)"""
        return self.name

    def __eq__(self, other):
        """
        Checks if two mechanisms are equal (the same).

        ## Parameters

        - other: 
            The mechanism to compare to.

        """
        if not isinstance(other, Mechanism):
            return False

        return (self.__repr__() == other.__repr__()) and \
               (self.mapping == other.mapping)
    
    def __ne__(self, other):
        """
        Checks if two mechanisms are not equal (the same).

        ## Parameters

        - other: 
            The mechanism to compare to.

        """
        return not (self == other)

    def __add__(self, other):
        """
        Adds two mechanisms together.

        ## Parameters

        - other: 
            The mechanism to add to the current one.

        """
        if not isinstance(other, Mechanism):
            raise TypeError(f'Cannot add {type(other)} to a '
                            f'`DiffPriv.mech.Mechanism` object')

        return Mechanism(
            name=f'{self.name} + {other.name}',
            description=f'{self.description} \n\n+\n\n {other.description}',
            mapping=lambda data, *args, **kwargs: \
                other.mapping(self.mapping(data, *args, **kwargs), *args, **kwargs),
            abbr=f'{self.abbr}+{other.abbr}',
            epsilon=None,  # TODO: Calculate delta sum
            delta=lambda data, *args, **kwargs: \
                self.delta(data, *args, **kwargs) + other.delta(data, *args, **kwargs)
        )

    def __mul__(self, scalar):
        """
        Multiplies a mechanism and a scalar.

        ## Parameters

        - scalar:
            A natural number representing the number of times to apply 
            the mechanism to itself.

        """

        if not isinstance(scalar, int):
            raise TypeError(f'Cannot multiply a `DiffPriv.mech.Mechanism` object '
                            f'by a {type(scalar)}')
        
        if scalar < 1:
            raise ValueError(f'Cannot multiply a `DiffPriv.mech.Mechanism` object '
                             f'by a negative or zero number')

        def mapping(data, *args, **kwargs):
            for _ in range(scalar):
                data = self.mapping(data, *args, **kwargs)
            return data

        return Mechanism(
            name=f'{scalar} * {self.name}',
            description=f'{scalar} x : \n{self.description}',
            mapping=mapping,
            abbr=f'{scalar}*{self.abbr}',
            epsilon=None,  # TODO: Calculate delta product
            delta=lambda data, *args, **kwargs: \
                self.delta(data, *args, **kwargs) * scalar
        )
