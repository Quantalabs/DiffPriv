"""Builtin mechanisms"""

from . import main
import numpy as np

def randresponse():
    """
    The Random Response Mechanism.

    The random response mechanism is a differential privacy mechanism with the 3 steps:
        1. Flip a coin
        2. If the coin is heads, return the original value
        3. If the coin is tails, flip again and return 0/false if heads and 1/true if tails. This program uses 0/1 instead of true/false.
    
    Returns: Mechanism class (see `mech.main` for more info on the class.)
    """
    def f(response_list):
        for i in response_list:
            b = np.random.randint(2)
            if b == 0: # pragma: no cover
                response_list[i] = 0

            if b == 1:
                b1 = np.random.randint(2)

                if b1 == 0: # pragma: no cover
                    response_list[i] = 0

                if b1 == 1: # pragma: no cover
                    response_list[i] = 1

        return response_list

    m = main.Mechanism("Random Response Mechanism", 
    "The random response differential privacy mechanism.",
    f,
    "randresponse")
    return m
